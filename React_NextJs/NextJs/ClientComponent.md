# Client Component

> 'use client'

전체 페이지 로드(Full page load)와 이후 탐색(Subsequent navigation)은 차이가 있다.

---

## Full Page Load or  페이지 처음 접속

> ServerComponent Rendering과 유사함.

전체 페이지 로드란 사용자가 웹사이트를 처음 방문할 때, 서버로부터 HTML 파일을 다운로드하고 브라우저가 이 HTML을 렌더링하는 과정


1. 서버 측 렌더링(SSR)

- 서버는 Next.js를 사용하여 페이지의 초기 HTML을 생성합니다.
- HTML 파일이 브라우저로 전송됩니다.

2. 클라이언트 측 렌더링(CSR):

- 브라우저는 서버로부터 전송된 HTML을 렌더링합니다.
- RSC Payload가 사용됨(reconcile `재조정`)
- use client가 선언된 클라이언트 사이드 컴포넌트는 CSR을 통해 브라우저에서 렌더링됩니다.

### 세부 과정

 - RSC Payload 사용: React Server Components(RSC) payload가 브라우저로 전송되어, 클라이언트에서 이를 재조정(reconcile)하여 UI를 구성합니다.

  - CSR 처리: use client가 선언된 컴포넌트는 브라우저에서 CSR을 통해 렌더링되며, 이는 초기 HTML에 포함되지 않기 때문에 JavaScript가 로드된 후 렌더링이 시작됩니다.

---

## Subsequent Navigation

1. 서버 렌더링 없음
  - 서버로부터 새로운 HTML을 받지 않습니다.
  - 클라이언트 사이드에서 페이지 전환이 이루어집니다.

2. 클라이언트 측 번들링 및 렌더링
  - 클라이언트 측에서 필요한 JavaScript 번들을 로드하여 렌더링합니다.
  - 클라이언트 측에서 페이지 전환이 발생할 때는 새로운 데이터를 가져와 DOM을 업데이트합니다.

### 세부 과정

  - 기존 HTML DOM Node와 비교: 클라이언트 측 네비게이션에서는 서버로부터 새로운 HTML을 받지 않고, 기존 DOM과 새로운 상태를 비교하여 필요한 부분만 업데이트합니다.

  - 다른 초기화 과정: 서버에서의 초기화 과정(예: 데이터 페칭, 컴포넌트 초기화 등)을 거치지 않지만, 클라이언트 측에서는 필요한 데이터를 비동기로 가져오고, 이를 바탕으로 UI를 업데이트합니다.


## 요약

- Full Page Load

  - 초기 페이지 로드 시 서버 측 렌더링(SSR)을 통해 HTML 생성.
  - 클라이언트 측에서 JavaScript를 로드하고, use client 컴포넌트를 CSR로 렌더링.
  - RSC payload를 사용하여 클라이언트에서 재조정.

- Subsequent Navigation

  - 클라이언트 측 네비게이션으로 서버 렌더링 없이 페이지 전환.
  - 필요한 JavaScript 번들을 로드하여 클라이언트 측에서 렌더링.
  - 기존 DOM과 새로운 상태를 비교하여 업데이트.