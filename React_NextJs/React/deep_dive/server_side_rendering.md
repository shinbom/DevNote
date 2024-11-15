# 서버 사이드 렌더링

## 싱글 페이지 어플리케이션

싱글 페이지 어플리케이션(Single Page Application:SPA)는 렌더링과 라우팅에 필요한 기능을 `브라우저의 자바스크립트에 의존`하는 방식이다.

최초에 첫 페이지에서 데이터를 모두 불러온 이후, 페이지 전환을 위한 모든 작업이 자바스크립트와 브라우저의 `history.pushState`와 `history.replaceState`로 이뤄짐.

자바스크립트의 리소스가 커지는 단점이 있지만, 로딩 이후에는 서버를 거쳐 리소스를 받아올 일이 적어짐으로 `사용자에서 훌륭한 UX/UI`를 제공함.

### 전통 방식 어플리케이션 vs 싱글 페이지 어플리케이션

### 전통 방식 어플리케이션

- 서버 사이드로 동작
- 페이지 전환이 발생할 때마다 새로운 페이지를 요청, HTML 다운로드 후 파싱

### 싱글 페이지 어플리케이션

- 최초 한번 모든 리소스를 다운로드
- 추가 리소스 다운로드 불필요
- 경우에 따라, 페이지 일부 영역만 리렌더링

## 서버 사이드 렌더링(Server Side Rendering)

최초에 사용자에게 보여줄 페이지를 서버에서 렌더링해 빠르게 사용자에게 제공하는 방식

> 웹페이지의 렌더링 책임을 어디에 두느냐에 따라, 싱글 페이지 어플리케이션과 서버 사이드 렌더링이 나뉜다.<br/><br/>
> - 싱글 페이지 어플리케이션
>   - 자바스크립트 번들
>   - 사용자 기기의 성능에 영향을 받음
> 
> - 서버 사이드 렌더링
>   - 서버에서 수행
>   - 서버에서 제공하여 비교적 안정적

## 서버사이드 렌더링의 장점과 단점

### 장점

- 최초 페이지 진입이 비교적 빠름
  - 최초 페이지에 진입했을 때 페이지에 유의미한 정보가 그려지는 `FCP(First Contentful Paint)`이 더 빨라짐
- 검색 엔진, SNS 공유 등 메타데이터 제공이 쉬움
  - `검색 엔진 로봇`이 페이지에 진입 해, HTML을 다운받고(자바스크립트 코드 미실행) 페이지 내부의 `오픈 그래프(Open Graph)`와 `메타(meta) 태그` 정보를 기반으로 페이지의 검색정보를 가져오고 검색엔진에 저장
- 누적 레이아웃 이동이 적음
  - 누적 레이아웃 이동(Cumulative Layout Shift)이란, 사용자에게 페이지를 보여준 이후 뒤늦게 HTML 정보가 추가되거나 삭제되어 화면이 덜컥 거리는 것과 같은 현상을 말함
  - API 요청이 모두 완료된 이후 완성된 페이지를 제공하므로 `위 문제에서 비교적 자유로움`

    > SPA의 경우, API의 속도가 모두 달랐을 때 서버 사이드 요청이 모두 완료되기 전까지 렌더링되지 않을 수 있으므로, 최초 페이지 다운로드가 느려질 수 있음.<br/>
    > 리액트 18에서 등장항 스트림으로 해결됨
- 사용자의 디바이스 성능에 비교적 자유로움
  - 자바스크립트 리소스 실행은 사용자의 디바이스에서만 실행됨에 따라, 사용자 디바이스 성능에 의존적임
  - 서버 사이드 렌더링은 부담을 서버에 나눌 수 있으므로, 사용자의 디바이스 성능으로 부터 조금 더 자유로움
    > 인터넷 속도가 느리거나, 사용자 방문이 폭증해 서버에 부담이 가중된다면 서버사이드 렌더링도 충분히 느려질 수 있음.<br>
    > `서버에 부담이 가중 시, 적절한 처리가 필요함.`
- 보안에 좀 더 안전함
  - 브라우저의 개발자 도구를 사용하면 웹사이트에서 일어나는 거의 대부분의 작업을 파악할 수 있음.
  - 서버 사이드 렌더링은 `인증 혹은 민감한 작업을 서버에서 수행하고, 결과만 브라우저에 제공`하여 보안에서 좀 더 안전하다.

### 단점

- 소스코드를 작성할 때 항상 서버를 고려해야 함
  - 브라우저에만 있는 전역 객체 (`window`, `sessionStorage`)와 같은 코드가 서버사이드에 실행되지 않도록 해야 함
    > 라이브러리도 동일
- 적절한 서버가 구축되어 있어야 함.
- 서비스 지연에 따른 문제
  - 사용자에게 보여줄 페이지의 렌더링 작업이 끝나기까지 사용자에게 어떤 정보도 제공할 수 없어, 요청이 얽혀 `병목 현상`이 심해지면 서버사이드 렌덜이이 더 안 좋은 사용자 경험을 제공할 수 있다.

## SPA와 SSR을 모두 알아야 하는 이유

- 서버사이드 렌더링 역시 만능이 아님
  - 웹 페이지의 설계와 목적, 우선순위에 따라 싱글 페이지 어플리케이션이 더 효율적일 수 있음.

- 싱글 페이지 어플리케이션과 서버 사이드 렌더링 어플리케이션
  - 뛰어난 싱글 페이지 어플리케이션은 뛰어난 멀티 페이지 어플리케이션보다 낫다.
    - 최초 페이지 진입 시, 보여줘야 할 정보만 최적화해 요청해서 렌더링
    - 중요성이 떨어지는 리소스는 게으른 로딩`(Lazy Loading)` 렌더링에 방해되지 않도록 처리
    - 코드 분할`(Code Splitting)`을 통해 불필요한 자바스크립트 리소스 다운로드 및 실행을 방지
    - 라우팅이 발생하면 필요한 영역만 교체하여 `사용자의 피로감을 최소화`

- 평균적인 싱글 페이지 어플리케이션은 평균적인 멀티 페이지 어플리케이션보다 느림
  - 멀티 페이지 어플리케이션은 매범 서버에 렌더링 요청을 하며, 서버는 안정적인 리소스를 기반으로 비슷한 성능의 렌더링을 수행
  - 싱글 페이지 어플리케이션은 렌더링과 라우팅이 최적화 되어있지 않다면, 사용자 기기에 따라 성능이 들쑥 날쑥할 수 있음

> 싱글 페이지 어플리케이션과 멀티 페이지 어플리케이션 모두 상황에 따라 유효한 방법이다.