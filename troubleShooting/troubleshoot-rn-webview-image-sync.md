# 📱 작업 기록: RN-WebBridge 이미지 업로드 제한 및 동기화

    Note: 과거 위치 정보(Geolocation) 및 카메라 제어 등의 앱브릿지 구현 경험을 바탕으로, 이번에는 웹과 네이티브 간의 이미지 개수 상태 동기화 로직을 설계하고 검증하였습니다.

> **배경:** 웹뷰(WebView) 환경에서 이미지 업로드 시, 전체 제한 개수를 초과하지 않도록 `웹(React)`의 상태를 `네이티브(RN)`에 전달하고, 이를 `시뮬레이터` 환경에서 검증한 기록입니다.

---

## 🏗️ 1. 시스템 아키텍처 (Bridge Protocol)

웹과 앱 간의 안정적인 데이터 송수신을 위해 다음과 같은 통신 규격을 정의했습니다.

### [Web → RN] : 이미지 피커 호출 요청

```json
{
  "type": "PICK_IMAGE",
  "payload": {
    "currentCount": 3,
    "maxLimit": 10
  }
}

```

### [RN → Web] : 결과 전달 (Base64 인코딩)

```json
{
  "type": "PICK_IMAGE_SUCCESS",
  "payload": {
    "images": [
      { "fileName": "img1.jpg", "type": "image/jpeg", "data": "base64_string..." }
    ]
  }
}

```

---

## 💻 2. 단계별 구현 로직

### 🌐 React (Web) 측 제한 로직

웹에서는 현재 상태를 관리하며, 브릿지 호출 전 **1차 필터링**을 수행합니다.

```javascript
const ImageUploader = () => {
  const [images, setImages] = useState([]); 
  const MAX_IMAGE_COUNT = 5; 

  const handleOpenPicker = () => {
    const currentCount = images.length;

    // 1차 방어: 이미 최대치라면 브릿지 호출 차단
    if (currentCount >= MAX_IMAGE_COUNT) {
      alert(`최대 ${MAX_IMAGE_COUNT}장까지만 업로드 가능합니다.`);
      return;
    }

    // 2차: RN에 현재 개수 정보를 담아 전송
    window.ReactNativeWebView?.postMessage(JSON.stringify({
      type: 'PICK_IMAGE',
      payload: { currentCount, maxLimit: MAX_IMAGE_COUNT }
    }));
  };
};

```

### 📱 React Native (App) 측 처리 로직

전달받은 정보를 바탕으로 네이티브 피커의 **선택 제한(selectionLimit)**을 동적으로 설정합니다.

```javascript
const onMessage = async (event) => {
  const { type, payload } = JSON.parse(event.nativeEvent.data);

  if (type === 'PICK_IMAGE') {
    // 잔여 슬롯 계산
    const remainingSlots = payload.maxLimit - payload.currentCount;

    try {
      const selectedImages = await ImagePicker.openPicker({
        multiple: true,
        maxFiles: remainingSlots, // 네이티브 단에서 선택 개수 강제 제한
        includeBase64: true,      // 웹뷰 미리보기를 위한 인코딩 설정
        compressImageQuality: 0.8 // 메모리 확보를 위한 압축
      });
      
      // 결과 전송 로직...
    } catch (e) { console.log(e); }
  }
};

```

## 🚀 2. [Detailed Troubleshooting] iOS WebView 이미지 미출력 해결

### ❌ 문제 상황 (Issue)

 조회한 API의 이미지가  웹(React)에 정상적으로 도달했음에도 불구하고, **iOS WebView에서만 이미지가 렌더링되지 않거나 UI(Swiper 등)가 갱신되지 않는 현상** 발생. (Android는 정상)

### 🔍 원인 분석: 전송 편의성을 고려한 데이터 분리 (The Initial Approach)

초기 설계 시, 추후 서버 전송을 위한 **`formData` 구성을 효율적으로 하기 위해** 데이터를 미리 두 가지 필드로 나누어 관리했습니다.

* **`attachmentFiles`**: API 전송을 위한 실제 파일/블롭 데이터.
* **`previewImages`**: 화면 렌더링을 위한 프리뷰 전용 데이터 (Base64).

**결과적으로** 이러한 데이터 파편화가 iOS의 **WKWebView 렌더링 엔진**에서 상태 업데이트와 UI 라이브러리(Swiper, Hook Form) 사이의 동기화를 어긋나게 하는 원인이 되었습니다. 특히 구조가 서버 규격과 다를 때 렌더링 큐에서 누락되는 현상이 빈번했습니다.

### ✅ 해결 방법: 데이터 스키마 단일화 (Schema Unification)

데이터를 미리 분리하지 않고, **서버 응답 규격(images 필드 구조)과 100% 일치하는 더미 데이터**를 생성하여 상태를 업데이트하도록 변경했습니다.

```javascript
// [해결] 서버 응답 규격(attachmentFiles, reviewImages 등)과 동일하게 Mocking
const handlePickImageSuccess = (rnPayload) => {
  const serverStyleImage = {
    id: `temp_${Date.now()}`,       // 서버 규격의 ID 모킹
    fileName: rnPayload.fileName,
    uri: `data:image/jpeg;base64,${rnPayload.base64}`,
    order: images.length,           // 순서값 부여
    rawFile: rnPayload.file         // 전송용 원본은 객체 내부에 은닉
  };

  // 형태를 맞추니 별도 필드 없이도 iOS에서 즉각적으로 렌더링됨
  setImages(prev => [...prev, serverStyleImage]);
};

```

> **Insight:** `formData` 가공의 편의성보다 **브라우저 엔진이 신뢰할 수 있는 일관된 데이터 구조**를 유지하는 것이 렌더링 안정성 측면에서 훨씬 유리함을 확인했습니다.

---

## 🧪 3. 검증 및 인사이트

* **테스트 환경:** RN 시뮬레이터 (iOS Simulator / Android Emulator) 활용
* **핵심 성과:**
* **동적 제한:** 시뮬레이터 앨범 UI에서 웹의 상태에 따라 선택 가능 개수가 실시간으로 차단되는 것을 확인.
* **구조적 교훈:** 

| 항목 | 내용 |
| --- | --- |
| **테스트 도구** | iOS Simulator (iPhone 15), Android Emulator |
| **인코딩 방식** | **Base64** (웹뷰 내 즉각적인 프리뷰 확인 용이) |
| **중점 확인** | 1. 잔여 개수만큼만 선택되는가 <br> 2. 하이브리드 환경에서는 전송 로직의 편의성보다 **렌더링 엔진의 특성(Data Structure)**을 최우선으로 고려해야 함.

<br> 2. 대용량 이미지 전송 시 딜레이 여부 |

> 💡 **시뮬레이터 활용 팁**
> `react-native-image-crop-picker`는 시뮬레이터의 기본 앨범과 연동되므로, 별도의 실기기 없이도 `maxFiles` 옵션이 UI 상에서 정상 작동하는지(이미지 선택 비활성화 등) 충분히 검증 가능했습니다.

---
---

**기록을 마치며:** 이번 작업은 단순히 기능을 구현하는 것을 넘어, 서버-앱-웹을 잇는 전체 데이터 파이프라인을 일관되게 설계하는 법을 배우는 계기가 되었습니다.


## 💡 인사이트 & 결론

* **이중 방어 (Double-Check):** 웹에서 1차로 흐름을 제어하고, RN에서 2차로 UI를 제한하여 **데이터 정합성**과 **UX(사용자 경험)**를 동시에 잡았습니다.
* **이미지 최적화:** Base64 전송 시 발생할 수 있는 메모리 문제를 방지하기 위해 RN 단에서 `compressImageQuality`를 적용하여 성능 부하를 줄였습니다.
* **성장 포인트:** 단순히 기능을 만드는 것을 넘어, 웹과 앱 사이의 **상태 동기화(State Sync)** 관점에서 브릿지 설계를 고민해 본 유의미한 작업이었습니다.

---