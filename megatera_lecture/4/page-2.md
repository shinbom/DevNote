# Fetch API

```
 키워드

- Fetch API 란
- Promise
- ReableStream
- Unicode
- CORS 란
```

## Fetch API

> [Fetch API](https://developer.mozilla.org/ko/docs/Web/API/Fetch_API)

> [Fetch 사용하기](https://developer.mozilla.org/ko/docs/Web/API/Fetch_API/Using_Fetch)

> [ReadableStream](https://developer.mozilla.org/ko/docs/Web/API/ReadableStream)

> [텍스트 디코더와 텍스트 인코더](https://ko.javascript.info/text-decoder)

네트워크 통신을 포함한 리소스 취득을 위한 인터페이스

HTTP Request, Response, Headers를 추상화하는 인터페이스와, 비동기적 리소스 요청을 시작하기 위한 fetch() 메서드

모든 API가 Promise에 기반함.typescript

```typescript
fetch('http://localhost:3000/products') // Promise

await fetch('http://localhost:3000/products') // Response  


const response = await fetch('http://localhost:3000/products');
// response.body는 ReadableStream

// JSON을 기본 지원한다.
const data = await response.json()


fetch(url, {
method : 'POST' | 'GET' | 'PUT' | 'DELETE' 등
...
})
```

###

### ReadableStream

Readable streams는 어떠한 data가 소비되는 것에 대한 추상화

```typescript
cosnt response = await fetch('http://localhost:3000/products');

const reader = response.body.getReader();
const chunk = await reader.read();
// chunk.value는 Uint8Array 타입.
// 원래는 chunk.done이 true일 때까지 반복해야 한다.

const body = new TextDecoder().decode(chunk.value);

const data = JSON.parse(body);
```

###

### Unit8Array

**`Uint8Array`** 형식화 배열(TypedArray)은 플랫폼의 바이트 순서를 따르는 8비트 부호 없는 정수의 배열

![ArrayBuffer](C:\BOM\BOM_WEB\megatera\frontend-survival\lecture\4\src\unit8array.png)

###

### Text Decoder

이진 데이터가 문자열이라면 어떨지 생각해봅시다. 예를 들어 텍스트 데이터가 있는 파일을 받았다고 가정하겠습니다.

내장 객체, [TextDecoder](https://encoding.spec.whatwg.org/#interface-textdecoder)는 주어진 버퍼와 인코딩으로 값을 실제 자바스크립트 문자열로 읽을 수 있게 해줍니다.

---

[Fetch: Download progress](https://javascript.info/fetch-progress)

 [[모던JS: 심화] 네트워크 요청  (velog.io)](https://velog.io/@longroadhome/%EB%AA%A8%EB%8D%98JS-%EC%8B%AC%ED%99%94-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EC%9A%94%EC%B2%AD-1)

```javascript
// ReadableStream 객체의 내장 메서드 getReader() 호출
const reader = response.body.getReader();

// 무한 반복문을 돌면서 reader 객체로부터 계속 내용을 읽어옴
while(true) {
  // 마지막 청크가 도착할 때 done = true
  // value는 청크 바이트의 Uint8Array 형태
  const { done, value } = await reader.read();

  if (done) {
    break;
  }

  console.log(`수신 : ${value.length} bytes`);
}
```

`Uint8Array` 타입은 나중에 자세히 다룰 예정이다. 간단하게만 짚고 넘어가면 `ArrayBuffer` 객체의 일종으로 원시(`raw`) 이진 데이터에 액세스하기 위한 메커니즘을 제공해 배열 최적화를 수행하는데 기여한다.

`await reader.read()` 의 호출 결과는 두개의 프로퍼티를 가지고 있는 객체를 반환하는데, 각각의 프로퍼티는 위 코드에서 쓰이고 있는 것과 같다.

- `done` : 읽기가 끝난 경우 `true`, 아니면 `false`
- `value` : 바이트를 나타내는 형식화 배열(`Uint8Array`)

> `ReadableStream` 객체는 `Stream API`에 명시되어 있는데, 해당 `API`는 명세에 따르면 비동기 반복자가 가능하다. 따라서 무한 반복문 말고 `for await ... of` 반복문을 사용할 수 있다. 그렇지만 이는 아직 모든 브라우저에서 지원되지 않기에 보통 `while`을 이용한 무한 루프를 사용한다.

###

### Fetch ReadableStream Step

```javascript
// Step 1 : fetch 응답 수신 후 reader 객체 생성
let response = await fetch('https://api.github.com/repos/javascript-tutorial/en.javascript.info/commits?per_page=100');

const reader = response.body.getReader();

// Step 2 : 헤더정보를 통해 전체 크기 구하기
const contentLength = +response.header.get('Content-Length');

// Step 3 : 청크 단위로 데이터 읽기
let receivedLength = 0;
let chunks = [];

while(true) {
  const { done, value } = await reader.read();

  if (done) {
    break;
  }

  chunks.push(value);
  receivedLength += value.length;

  console.log(`수신: ${receivedLength} of ${contentLength}`);
}

// Step 4 : chunks 배열을 단일 Uint8Array 형태로 변환
let chunksAll = new Uint8Array(receivedLength);
let position = 0;

for(let chunk of chunks) {
  chunksAll.set(chunk, position);
  position += chunk.length;
}

// Step 5 : 문자열로 디코딩
let result = new TextDecoder('utf-8').decode(chunksAll);

// Step 6 : 결과 출력
let commits = JSON.parse(result);
```

1. `fetch` 메서드를 호출하고 응답을 받는다. 그리고 `response.body.getReader()`를 호출해서 `Stream API`를 처리할 수 있는 `reader` 객체를 생성한다.

2. 데이터를 읽기에 앞서 `Content-Length` 헤더를 통해 응답 전체의 크기를 미리 구한다. 이는 `CORS` 이슈로 접근이 불가할 수도 있는데 보통의 경우 문제없이 크기를 구할 수 있다.

3. 데이터를 `await reader.read()`를 통해 순차적으로 읽는다. 응답 청크를 `chunks` 배열에 차례대로 삽입한다. 일단 응답을 한 번 소비하고 나면 `response.json()`과 같은 다른 메서드를 사용할 수 없기 때문에 해당 배열을 가지고 원하는 응답 본문에 접근할 것이다.

4. 모든 데이터를 읽으면 그 값을 가지고 있는 `chunks` 배열이 만들어진다. 이 배열을 다시 `Uint8Array` 형식화 배열로 변환한다. 우리가 필요한 것은 단일화 된 데이터 형태인데, 안타깝게도 `chunks` 배열을 단번에 `Uint8Array`로 변환하기 위한 단일 메서드는 없다. 따라서 반복문을 통해 순회하며 변환작업을 수행하자.

5. `chunksAll` 변수에는 변환이 완료된 결과가 들어있다. 이는 아직 문자열이 아닌 바이트 배열이기 때문에 이를 다시 문자열로 변환해주어야 한다. 이는 `TextDecoder`를 통해 수행할 수 있다.

6. 최종적으로 `TextDecoder`를 통해 변환된 결과를 다시 `JSON.parse()` 메서드를 통해 `JSON`으로 변환하면 원하는 응답 본문에 `commits`에   접근할 수 있다.

### Unicode

유니코드(Unicode)는 전 세계의 모든 문자를 다루도록 설계된 표준 문자 전산 처리 방식

---

## Promise

**`Promise`** 객체는 비동기 작업이 맞이할 미래의 완료 또는 실패와 그 결과 값을 나타냅니다.

- 대기(*pending)*: 이행하지도, 거부하지도 않은 초기 상태.
- 이행(*fulfilled)*: 연산이 성공적으로 완료됨.
- 거부(*rejected)*: 연산이 실패함.

 ![](C:\BOM\BOM_WEB\megatera\frontend-survival\lecture\4\src\promise.png)

### then

```javascript
p.then(onFulfilled, onRejected);

p.then(function (value) {
    // 이행
}, function(reason) {
    // 거부
})
```

Promise를 리턴하고 두개의 콜백 함수를 인수로 받았을 때, 이행 or 거부를 위한 콜백함수

### async & await

```javascript
async function f() {
    return 1;
}


f().then(alert); // 1
```

funciton 앞에 async를 붙이면, 함수는 항상 Promise를 반환

```javascript
async function f() {

  let promise = new Promise((resolve, reject) => {
    setTimeout(() => resolve("완료!"), 1000)
  });

  let result = await promise; // 프라미스가 이행될 때까지 기다림 (*)

  alert(result); // "완료!"
}

f();
```

awiat 키워드를 만나면, Promise가 처리될때까지 기다림

> `await`는 `promise.then`보다 좀 더 세련되게 프라미스의 `result` 값을 얻을 수 있도록 해주는 문법입니다. `promise.then`보다 가독성 좋고 쓰기도 쉽습니다.

```javascript
async function f() {

  try {
    let response = await fetch('http://유효하지-않은-주소');
  } catch(err) {
    alert(err); // TypeError: failed to fetch
  }
}
```

**에러핸들링**은 try, catch를 이용하여 할 수 있다.

try...catch가 없을 경우, Promise는 거부상태가 됨

---

## CORS(CrossOrigin)

> [동일 출처 정책](https://developer.mozilla.org/ko/docs/Web/Security/Same-origin_policy)

> [CORS](https://developer.mozilla.org/ko/docs/Web/HTTP/CORS)

![URL](C:\BOM\BOM_WEB\megatera\frontend-survival\lecture\4\src\origin.png)

웹 브라우저는 Same Origin Policy에 따라 웹 페이지와 리소스를 요청한 곳(여기서는 REST API 서버)이 서로 다른 출처(포트까지 포함)일 때 서버에서 얻은 결과를 사용할 수 없게 막는다.

출처는 `Protocol`과 `Host`, 그리고 위 그림에는 나와있지 않지만 `:80`, `:443`과 같은 포트 번호까지 모두 합친 것을 의미한다.

포트 번호까지 모두 일치해야 같은 출처라고 인정된다.

### SOP(Same-Origin Policy)

> “같은 출처에서만 리소스를 공유할 수 있다”라는 규칙

> 리소스 요청은 출처가 다르더라도 허용하기로 했는데, 그 중 하나가 “CORS 정책을 지킨 리소스 요청”

****

**출처를 비교하는 로직은 서버에 구현된 스펙이 아니라 브라우저에 구현되어 있는 스펙이다.**

[CORS는 왜 이렇게 우리를 힘들게 할까](https://evan-moon.github.io/2020/05/21/about-cors/)

---

서버에 요청하고 응답을 받아오는 것까지는 이미 진행이 다 된 상황이란 점에 주의!

REST API 서버에서 Headers에 **“Access-Control-Allow-Origin”** 속성을 추가하면 된다.

Express에선 그냥 [CORS 미들웨어](https://expressjs.com/en/resources/middleware/cors.html)를 설치해서 사용하면 됨.

패키지 설치

```bash
npm i cors npm i -D @types/cors
```

​

CORS 미들웨어 사용

```javascript
import express from 'express';
import cors from 'cors';

const app = express(); 
app.use(cors());
```

> 일정상 작업하고 백엔드 API가 안나왔을 때, Express를 이용하여, 작업할 수 있다.
