# 서버 사이드 렌더링을 위한 리액트 API

- Node.js 서버 환경에서 실행
- `react-dom/server.js`에 소스가 있음.
  - [server.node.js](https://github.com/facebook/react/blob/main/packages/react-dom/server.node.js)

## renderToString

인수로 넘겨받은 리액트 컴포넌트를 렌더링하여 `HTML 문자열로 반환`하는 함수

```javascript
// App.jsx
export const App = () => {
  function handleClick = () => {
    console.log('hello')
  }

  return (
    <p>Hi Render</p>
  )
}
```

```javascript
// nodeJs, express사용
import express from "express";
import React from "react";
import ReactDOMServer from "react-dom/server";
import App from "../src/App";

const app = express();

app.get("/*", (req, res) => {
  const appHtml = ReactDOMServer.renderToString(<App />);
  res.send(renderFullPage(appHtml));
});

function renderFullPage(html) {
  return `
    <!doctype html>
    <html>
      <head>
        <title>My Page</title>
      </head>
      <body>
        <div id="root" data-reactroot="">${html}</div>
        <script src="/bundle.js"></script>
      </body>
    </html>
  `;
}

app.listen(3000);
```

> handleClick, useEffect과 같은 훅, 이벤트 핸들러는 포함되지 않음.

`renderToString`은 인수로 주어진 리액트 컴포넌트를 기준으로 브라우저가 렌더링할 HTML을 제공하는 목적인 함수이므로, 클라이언트에서 실행되는 자바스크립트 코드를 포함시키거나 렌더링하는 역할까지는 해주지 않음.

`data-reactroot`속성은 리액트 컴포넌트의 루트 엘리먼트가 무엇인지 식별하는 역할이다.<br/>
이 속성은 이후, 자바스크립트를 실행하기 위한 `hydrate함수`에서 루트를 식별하는 기준이 된다.

## renderToStaticMarkup

`renderToString`과 동일하게 HTML문자열을 만든다는 점에서는 동일함
하지만, 루트 요소에 추가한 `data-reactroot`와 같은 리액트에서만 사용하는 추가적인 DOM속성을 만들지 않는다.

이 함수는 브라우저 API를 절대로 실행할 수 없다.

> useEffect, 이벤트 핸들러등 사용 불가

순수한 HTML만 만들때 사용된다.

## renderToNodeStream

스트림을 활용하여 브라우저에 제공해야 할 큰 HTML을 작은 단위로 쪼개 연속적으로 작성하여, 리액트 어플리케이션을 렌더링하는 `node.js서버의 부담을 덜 수 있음.`

### renderToNodeStream과 renderToString의 차이점

- renderToNodeStream은 node.js 환경에 의존하고 있음.
- renderToString은 브라우저에서 실행할 수 있지만, renderToNodeStream은 브라우저에서는 실행할 수 없음
- renderToString의 반환값은 `string`
- renderToNodeStream의 반화값은 `ReadableStream`
  - utf-8로 인코딩된 바이트 스트림으로, Node.js환경에서만 사용할 수 있음.

## renderToStaticNodeStream

renderToNodeStream에 제공하는 결과물은 동일하지만, renderToStaticMarkup과 마찬가지로 순수한 HTML만 만들 때 사용한다.

---

## hydrate

정적으로 생성된 HTML에 이벤트와 핸들러를 붙여 완전한 웹 페이지 결과물을 만드는 함수

이미 렌더링된 HTML이 있단 가정하에 작업이 수행되고, 이 렌더링된 HTML을 기준으로 이벤트를 붙이는 작업만 실행

hydrate 작업이 단순히 이벤트나 핸들러는 추가하는 것 이외에도 렌더링을 한 번 수행하면서 hydrate가 수행한 렌더링 결과물 HTML과 인수로 넘겨받은 HTML을 비교하는 작업을 수행한다.

이 비교를 통해, 불일치가 발생하면 hydrate에러가 발생하게 되고 불일치가 발생하면 hydrate가 렌더링한 기준으로 웹페이지를 그리게 된다.

> 이렇게 hydrate가 렌더링되는것은 서버와 클라이언트에서 렌더링이 두번 발생하게 되고, 서버 사이드 렌더링의 장점을 포기하는 것이 된다.
