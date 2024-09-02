# Node.js와 브라우저의 차이점

> 브라우저와 Node.js 모두 JavaScript를 프로그래밍 언어로 사용

브라우저에 있는 `document, window`가 Node.js에는 존재하지 않음.

## 모듈 시스템

모듈을 불러올 때, 브라우저는 ECMA스크립트 표준 모듈을 사용
`import` 를 사용하고, node.js는 `CommonJS` 모듈 시스템을 사용하여 require()를 사용