# 온라인 쇼핑몰 주문, 결제

## 우편번호 검색

[Daum 우편번호 서비스] (https://postcode.map.daum.net/guide)

```html
<script src="https://t1.daumcdn.net/mapjsapi/bundle/postcode/prod/postcode.v2.js"></script>
```

전역으로 얻는 daum 객체의 타입을 알 수 있도록 daum.postcode.d.ts 파일 생성

```typescript
declare namespace daum {
  export type PostcodeResult = {
    address: string;
    zonecode: string;
  }

  export class Postcode {
    constructor({ oncomplete, width, height }: {
      oncomplete: (data: PostcodeResult) => void;
      width: string;
      height: string;
    });

    embed(element: HTMLElement | null);
  }
}
```

---

## declare

Typescript declare란 컴파일러에게 declare로 선언된 변수 또는 함수들을 이미 존재한다고 알리는 것이다.

declare로 선언된 부분은 javascript로 컴파일되지 않음.

코드 외부에 존재하는 변수 타입을 지정하기 위해 `declare` 키워드를 사용할 수 있다.

### 기본 선언 방법

```typescript
declare let someExternalVariable : string
```

### 모듈 선언

```typescript
declare module 'my-module' {
    export function foo(): string;
}


// 다른 파일에서 사용

import {foo} from 'my-module';
```


### 전역 변수 선언

전역 변수 `window 등`를 다룰 때, 다음과 같이 사용한다.

```typescript
declare global {
  interface Window {
    GlobalVariable : number
  }
}
```

### 사용 이유

1. 호환성 : TypeScript 코드가 타입 오류 없이 JavaScript 라이브러리와의 상호 운용될 수 있도록 하기 위함.

2. 안전성 : 정확한 타입 선언을 제공하여, 런타임 전에 잠재적인 타입 오류를 포착할 수 있도록 할 수 있음.

3. 문서화 : 라이브러리 함수에서 기대할 수 있는 타입을 알려주는 문서의 형태로 동작함.

---

## 포트원 통합 결제 솔루션

> [포트원](https://portone.io/korea/ko)

> [결제 연동하기](https://portone.gitbook.io/docs/console/guide/connect)

> [API Keys](https://portone.gitbook.io/docs/console/guide/api-keys)

> [인증결제 연동하기](https://portone.gitbook.io/docs/auth/guide)

> [JavaScript SDK](https://portone.gitbook.io/docs/sdk/javascript-sdk)

---

### 결제 프로세스

1. 결제 요청 (F/E에서 요청) → 우리가 자주 보는 결제창이 뜬다.
2. 결제 결과 확인 (F/E에서 결과 받음)
3. 결제 금액 위변조 검증 → B/E로 결제 결과를 전송하면 B/E에서 처리
4. 결제 완료 → B/E에서 성공하면 F/E는 주문 완료 페이지로 이동.

---

### 환경 변수 관리

> .env

자주 사용하는 값들은 환경변수로 선언하여 사용하면 편리하다.

```bash
API_BASE_URL=https://shop-demo-api-03.fly.dev
PORTONE_IMP=<가맹점 식별코드>
PORTONE_PG_CODE=<PG사 코드>.<PG상점아이디>
```

