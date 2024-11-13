# 서버 사이드 렌더링을 위한 리액트 API

- Node.js 서버 환경에서 실행
- `react-dom/server.js`에 소스가 있음.
  - [server.node.js](https://github.com/facebook/react/blob/main/packages/react-dom/server.node.js)

## renderToString

인수로 넘겨받은 리액트 컴포넌트를 렌더링하여 `HTML 문자열로 반환`하는 함수

```javascript
import { renderToString } from 'react-dom/server';

const html = renderToString(<App />);
```