# JSX 자바스크립트 변환

```bash
@babel/plugin-transform-react-jsx
```

이 플러그인을 통해 JSX구문을 자바스크립트가 이해할 수 있는 형태로 변환함.

## JSX 변환 전

```JSX
const ComponentA = <A required={true}>Hello World</A>

const componentB = <>Hello World</>

const ComponentC = = (
  <div>
    <span>Hello World</span>
  </div>
)
```

## JSX 변환 후

```javascript

'use strict'

var ComponentA = React.createElement(
  A,
  {
    required : true
  },
  'Hello World'
)

const ComponentB = React.createElement(
  React.Fragment,
  null,
  'Hello World'
)

const ComponentC = React.createElement(
  'div',
  null,
  React.createElement(
    'span',
    null,
    React.createElement('span', null, 'hello World')
  )
)
```

### JSX 변환 후(자동 런타임 트랜스파일한 결과)

```javascript
'use strict'

var _jsxRuntime = require('custom-jsx-library/jsx-runtime')

var ComponentA = (0, _jsxRuntime.jsx)(A, {
  required : true,
  children : 'Hello World'
})

var ComponentB = (0, _jsxRuntime.jsx)(_jsxRuntime.Fragment, {
  children : 'Hello World'
})

var ComponentC = (0, _jsxRuntime.jsx)('div', {
  children : (0, _jsxRuntime.jsx)('span', {
    children : 'hello World'
  })
})
```

#### 공통점

- JSXElement를 첫번째 인수로 선언해 요소를 정의함.
- 옵셔널인 JSXChildren, JSXAttributes, JSXStrings는 이후 인수로 넘김.
