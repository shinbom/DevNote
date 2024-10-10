# Global Style

```
키워드

Reset CSS
box-sizing 속성
word-break 속성
Theme
ThemeProvider
```

## Reset CSS

> [Reset Css](https://meyerweb.com/eric/tools/css/reset/)
>

> [styled-reset](https://github.com/zacanger/styled-reset)
>

브라우저마다 초깃값이 달랏었기 때문에, 초기화하는 기법이 생겼다.

패키지 설치.

```bash
npm i styled-reset
```

​
App 컴포넌트에서 사용.

```typescript
import { Reset } from 'styled-reset';

export default function App() {
 return (
  <>
   <Reset />
   <Greeting />
  </>
 );
}
```

## Global Style
>
> [createGlobalStyle](https://styled-components.com/docs/api#createglobalstyle)
>

> [대체 CSS box model](https://developer.mozilla.org/ko/docs/Learn/CSS/Building_blocks/The_box_model#대체_css_box_model)
>

> [box-sizing](https://developer.mozilla.org/ko/docs/Web/CSS/box-sizing)
>

> [The 62.5% Font Size Trick](https://www.aleksandrhovhannisyan.com/blog/62-5-percent-font-size-trick/)
>

> [keep-all-villain](https://twitter.com/keepallvillain)
>

> [word-break](https://developer.mozilla.org/ko/docs/Web/CSS/word-break)
>

전역 스타일 지정.

```typescript
import { createGlobalStyle } from 'styled-components';

const GlobalStyle = createGlobalStyle`
 html {
  box-sizing: border-box;
 }
 
 *,
 *::before,
 *::after {
  box-sizing: inherit;
 }
 
 html {
  font-size: 62.5%;
 }
 
 body {
  font-size: 1.6rem;
 }
 
 :lang(ko) {
  h1, h2, h3 {
   word-break: keep-all;
  }
 }
`;

export default GlobalStyle;
```

```typescript

import { Reset } from 'styled-reset';

import GlobalStyle from './styles/GlobalStyle';

export default function App() {
 return (
  <>
   <Reset />
   <GlobalStyle />
   <Greeting />
  </>
 );
}
```
