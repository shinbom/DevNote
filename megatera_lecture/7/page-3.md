# Router

```\
키워드

- ReactRouter 
- RouterProvider
```

React Router 버전 6.4부터 지원하는, 라우터 객체를 만들어 사용하는 방법

```typescript
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

import routes from './routes';

const router = createBrowserRouter(routes);

root.render((
    <React.StrictMode>
        <RouterProvider router={router} />
    </React.StrictMode>
));
```

### createBrowserRouter

[createBrowserRouter v6.20.0 | React Router](https://reactrouter.com/en/main/routers/create-browser-router)

DOM History API를 사용하여 URL을 업데이트하고 기록 스택을 관리한다.

### RouterProvider

Router구성요소를 전달하고 활성화함.

---

메모리 라우터 만들어서 테스트를 진행한다.

```typescript

```
