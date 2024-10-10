# Routes

```
키워드

라우터란?
React Router
- Browswer Router
- Route
- Memory Router
```

## React Router

> [React Router](https://reactrouter.com/)

`Client Side Routing`을 가능하도록 한다.

기존의 웹 사이트는 `Server`에 문서를 요청하고, CSS와 JavaScript를 다운로드 평가 후, 페이지에 대한 프로세스가 시작된다.(SSR)

하지만 `CSR`은  새로운 문서를 요청하거나 CSS 및 JavaScript 자산을 다시 평가할 필요가 없음에 따라, 더 빠른 사용자 경험을 제공할 수 있다.

### Routes

> [Routes](https://reactrouter.com/en/main/components/routes)

> [Route](https://reactrouter.com/en/main/route/route)

```bash
npm i react-router-dom
```

```typescript
// App.tsx
import { Routes, Route } from 'react-router-dom';

function App() {
    return (
        <div>
            <Header />
            <main>
                <Routes>
                    <Route path="/" element={<HomePage />} />
                    <Route path="/about" element={<AboutPage />} />
                </Routes>
            </main>
            <Footer />
        </div>
    );
}
```

> 테스트 환경에서 BrowserRouter를 사용하면 실패한다.

```typescript
// main.tsx
import { BrowserRouter } from 'react-router-dom';

root.render((
    <BrowserRouter>
        <App />
    </BrowserRouter>
));
```

테스트환경에서는 메모리 라우터를 사용하면 된다.

```typescript
import {render} from '@testing-library/react'
import { MemoryRouter } from "react-router-dom";
import App from './App';

const context = describe;

describe('App', () => {
    function renderApp(path: string) {
        render((
            <MemoryRouter initialEntries={[path]}>
                <App />
            </MemoryRouter>
        ));
    }

    context('when the current path is “/”', () => {
        it('renders the home page', () => {
            renderApp('/');

            screen.getByText(/Hello/);
        });
    });

    context('when the current path is “/about”', () => {
        it('renders the about page', () => {
            renderApp('/about');

            screen.getByText(/About/);
        });
    });
});
```
