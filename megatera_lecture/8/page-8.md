# Theme

> [Theming](https://styled-components.com/docs/advanced#theming)
>

> [Create a declarations file](https://styled-components.com/docs/api#create-a-declarations-file)
>

디자인 시스템의 근간을 마련하는데 활용. 잘 정의하면 다크 모드 등에 대응하기 쉬움. 눈에 보이는 단편적인 정보를 넘어서, “의미”에 집중할 수 있게 됨.

```typescript
// Set Default Theme

const defaultTheme = {
 colors: {
  background: '#FFF',
  text: '#000',
  primary: '#F00',
  secondary: '#00F',
 },
};

export default defaultTheme;


// Theme Type Define

import defaultTheme from "./defaultTheme";

type Theme = typeof defaultTheme

export default Theme;

`typeof를 이용하여 type을 추출`

// Set Dark Theme
import Theme from "./Theme";

const darkTheme : Theme = {
  colors: {
   background: '#FFF',
   text: '#000',
   primary: '#F00',
   secondary: '#00F',
  },
 };

 export default darkTheme;

```

``` typescript
// App.tsx

import { ThemeProvider } from 'styled-components';

import { Reset } from 'styled-reset';

import defaultTheme from './styles/defaultTheme';

import GlobalStyle from './styles/GlobalStyle';

export default function App() {
 return (
  <ThemeProvider theme={defaultTheme}>
   <Reset />
   <GlobalStyle />
   <Greeting />
  </ThemeProvider>
 );
}
```

``` typescript
//props.theme 사용

import { createGlobalStyle } from 'styled-components';

const GlobalStyle = createGlobalStyle`
 body {
  background: ${(props) => props.theme.colors.background};
  color: ${(props) => props.theme.colors.text};
 }
 
 a {
  color: ${(props) => props.theme.colors.text};
 }
 
 button,
 input,
 select,
 textarea {
  background: ${(props) => props.theme.colors.background};
  color: ${(props) => props.theme.colors.text};
 }
`;

export default GlobalStyle;
```

```typescript

//styled.d.ts

import 'styled-components';

declare module 'styled-components' {
 export interface DefaultTheme extends Theme {
  colors: {
   background: string;
   text: string;
   primary: string;
   secondary: string;
  }
 }
}
```

타입을 정의하고 defaultTheme을 맞추는 게 불편하니, 반대로 defaultTheme에서 타입을 추출

``` typescript
import defaultTheme from './defaultTheme';

type Theme = typeof defaultTheme;

export default Theme;
```

```typescript
// 위에서 typeof를 통해 추출한 타입을 styled.d.ts에 적용

import 'styled-components';

import Theme from './Theme';

declare module 'styled-components' {
 export interface DefaultTheme extends Theme {}
}
```

## 다크 모드 적용

```typescript
import { useDarkMode } from 'usehooks-ts';

import { ThemeProvider } from 'styled-components';

import { Reset } from 'styled-reset';

import defaultTheme from './styles/defaultTheme';
import darkTheme from './styles/darkTheme';

import GlobalStyle from './styles/GlobalStyle';

import Greeting from './components/Greeting';
import Button from './components/Button';

export default function App() {
const { isDarkMode, toggle } = useDarkMode();

const theme = isDarkMode ? darkTheme : defaultTheme;

return (
 <ThemeProvider theme={theme}>
  <Reset />
  <GlobalStyle />
  <Greeting />
  <Button onClick={toggle}>
   Dark Theme Toggle
  </Button>
 </ThemeProvider>
 );
}
```

Jest 테스트 쪽에서 “window.matchMedia” 문제 발생.

> [Mocking methods which are not implemented in JSDOM](https://jestjs.io/docs/manual-mocks#mocking-methods-which-are-not-implemented-in-jsdom)
>

`src/setupTests.ts` 파일에 공식 문서에 나온 코드를 넣으면 해결된다.

```typescript
Object.defineProperty(window, 'matchMedia', {
 writable: true,
 value: jest.fn().mockImplementation((query) => ({
  matches: false,
  media: query,
  onchange: null,
  addListener: jest.fn(), // deprecated
  removeListener: jest.fn(), // deprecated
  addEventListener: jest.fn(),
  removeEventListener: jest.fn(),
  dispatchEvent: jest.fn(),
 })),
});
```

### 참고

- <https://code.visualstudio.com/api/references/theme-color>
- <https://getbootstrap.com/docs/5.3/customize/color/>
