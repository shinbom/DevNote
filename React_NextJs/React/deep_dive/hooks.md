# 리액트 훅

함수형 컴포넌트가 상태를 사용하거나 클래스형 컴포넌트의 생명주기 메서드를 대체하는 등의 다양한 작업을 하기 위해 추가됨.

## 훅의 규칙

- 최상위에서만 훅을 호출
  - 반복문, 조건문, 중첩된 함수 내에서 훅 실행할 수 없음
  - 리액트 함수형 컴포넌트, 사용자 정의 훅에서만 호출할 수 있음


## useState

함수형 컴포넌트 내부에서 상태를 정의하고, 상태를 관리할 수 있게 해주는 훅

```tsx
import { useState } from 'react'

const [ state, setState ] = useState(initialState)
```

### useState의 내부의 모습을 구현한 모습

```js

const React = function () {
  const global = {}
  let index = 0

  function useState(initialState) {
    if(!global.states) {
      global.states = []
    }

    const currentState = global.states[index] || initialState

    global.states[index] = currentState

    const setState = (function () {
      // Closer
      let currentIndex = index
      return function (value) {
        global.states[currentIndex] = value
      }
    })
  }()

  index = index + 1

  return [currentState, setState]
}
```

> 작동 자체만 구현되었고, 실제 구현은 `useReducer`를 이용하여 구현되어 있다.

### 게으른 초기화

useState에 변수 대신 `함수를 넘기는 것`을 `게으른 초기화(lazy initialization)`라고 한다.

```jsx
// 일반적인 useState
const [count, setCount] = useState(0)

// 게으른 초기화
const [count, setCount] = useState( () => 0 )
```

> useState의 초깃값이 복잡하거나 무거운 연산을 포함하고 있을 때 사용<br/>
> 초기화 함수는 오로지 `state가 처음 만들어질 때`만 사용<br/>

---

## useEffect

- useEffect 두개의 인수를 받음
- 첫 번째는 콜백
- 두 번쨰는 의존성 배열
- 두 번째 의존성 배열이 변경되면 첫 번째 인수인 콜백을 실행
- 의존성 배열에 `빈 배열[]`을 넣으면 컴포넌트가 `마운트 될 때만 실행`
- useEffect는 `클린업 함수를 반환`, 컴포넌트가 `언마운트 될 때만 실행`

> 생명주기(LifeCycle) 메서드를 대체하기 위해 만들어진 훅이 아님

```jsx
function Component () {
  useEffect(() => {

  }, [props, state])
}
```

> 렌더링 할 때마다 의존성에 있는 값을 보면서, 의존성의 값이 이전과 다른 게 하나라도 있으면 부수 효과(SideEffect)를 실행하는 함수


```jsx
useEffect(() => {
  function addMouseEvent() {
    console.log(counter);
  }

  window.addEventListener("click", addMouseEvent);

  return () => {
    // 클린업
    window.removeEventListener("click", addMouseEvent);
  };
}[counter]);
```

클린업 함수는 새로운 값을 기반으로 렌더링 뒤에 실행되지만, 변경된 값을 읽는 것이 아니라 함수가 정의되었을 당시에 선언됐던 이전 값을 보고 실행

useEffect는 콜백이 실행될 때마다 이전의 클린업 함수가 존재했다면 `클린업 함수를 실행한 뒤에 콜백을 실행`

> 언마운트는 특정 컴포넌트가 DOM에서 사라진다는 것을 의미하는 클래스형 컴포넌트의 용어

**클린업 함수는 언마운트라기보다 `함수형 컴포넌트가 리렌더링됐을 때 의존성 변화가 있었을 당시 이전의 값을 기준으로 실행되고, 이전 상태를 청소해준다고 볼 수 있음`**

### 의존성 배열

- 빈배열을 둘 경우[] : 비교할 의존성이 없다고 판단해 최초 렌더링 직후에만 실행

```jsx
useEffect(() => {}, []);
```

- 아무런 값이 없는 경우 : 의존성을 비교할 필요 없이 렌더링 할 때마다 실행

```jsx
function Component () => {
  // 서버 사이드 렌더링의 경우, 서버에서도 실행
  // 무거운 작업일 경우 렌더링을 방해하므로 성능에 악 영향이 미칠 수 있음.
  console.log('rendering')
}


function Component () => {
  useEffect( () => {
    // 클라이언트 사이드에서 실행되는 것을 보장함.
    // 컴포넌트의 렌더링이 완료된 이후 실행
    console.log('rendering')
  })
}
```

> useEffect는 `컴포넌트가 렌더링된 후 컴포넌트의 사이드 이펙트(부수효과)`를 일으키고 싶을 때 사용하는 훅

- 의존성 배열을 넣은 경우 : 의존성 배열의 값이 변경될 때마다 실행

### useEffect 구현

```javascript
const MyReact = function () {
  const global = {};
  let index = 0;

  function useEffect(callback, dependencies) {
    const hooks = global.hooks;

    let previousDependencies = hooks[index];

    let isDependenciesChanged = previousDependencies
      ? dependencies.some(
          (value, index) => !Object.is(value, previousDependencies[idx])
        )
      : true;

    if (isDependenciesChanged) {
      callback();
    }

    hooks[index] = dependencies;

    index++;
  }

  reutrn { useEffect }
};
```

> 의존성 배열의 이전값과 현재값의 얕은 비교가 핵심

### useEffect 주의할 점

- `의존성 []`을 선언 시, 최초에 함수형 컴포넌트가 마운트됐을 때만 콜백함수가 실행이 필요한지 검토
- 첫번쨰 인수에 함수명을 부여

  - useEffect의 코드가 복잡하고 많아질수록 무슨 일을 하는 useEffect코드인지 파악이 어려움
  - `기명함수`로 변경하여, `useEffect의 목적`을 알 수 있도록 함

  ```jsx
  useEffect(
    function logActivateUser() {
      logging(user.id);
    },
    [user.id]
  );
  ```

- 거대한 useEffect를 만들지 마라
- 불필요한 외부 함수를 만들지 마라

#### useEffect의 콜백 인수로 비동기 함수 넣기

```jsx
useEffect(async () => {
  const response = await fetch('http://....')
  const result = await response.json()
  setData(result)
})
```

> useEffect의 인수로 비동기 함수가 사용가능하다면 비동기 함수의 응답 속도에 따라 결과가 이상하게 나올 수 있다.<br/>
> 극단적으로 state 기반의 응답이 `10초`가 걸리고, 바뀐 state 기반의 응답이 `1초 뒤`에 있다면 `이전 state` 기반으로 결과가 나와버리는 불상사가 생길 수 있음.<br/>
> **`useEffect의 경쟁상태`가 발생할 수 있음.**

인수로 비동기 함수를 지정할 수 없는 것이지, 비동기 함수 실행 자체가 문제가 되는 것은 아니다.

```jsx
useEffect(() => {
  let shouldIgnore = false

  async function fetchData () {
    const response = await fetch('http://.....')
    const result = await response.json()
    if(!shouldIgnore) {
      setData(result)
    }
  }

  fetchData()

  return () => {
    shouldIgnore = true
  }
}, [])
```

> 의존성 배열에 값이 존재하는 상태에서 비동기 함수가 useEffect 내부에 존재하게 되면,  useEffect 내부에서 비동기 함수가 생성되고 실행되는 것을 반복할 수 있음.<br/>
> 그러므로, 클린업 함수에서 이전 비동기 함수에 대한 클린업 처리를 하는 것이 좋다.<br/>
> fetch의 경우 abortController 사용
> 위 예제의 경우, shouldIgnore를 이용하여 state의 변경을 차단(리렌더링 방지)

## useMemo

비용이 큰 연산에 대한 결과를 저장`(메모이제이션)`하여, 이 저장된 값을 반환하는 훅

```jsx
import { useMemo } from 'react'

const memoizedValue = useMemo( () => expensiveComputations(a, b), [a, b])
```

- 첫 번째 인수는 값을 반환하는 생성 함수
- 두 번째 인수는 함수가 의존하는 값의 배열을 전달

> 렌더링 발생 시 의존성 배열의 값이 변경되지 않았으면 함수를 재실행하지 않고 이전에 기억해 둔 값을 반환<br/>
> 의존성 값이 변경됐다면, 첫 번째 인수의 함수를 실행한 후 그 값을 반환하고 그 값을 다시 기억함.<br/>
> `값뿐만 아니라 컴포넌트도 가능`

```jsx
function ExpensiveComponent({value}) {
  useEffect( () => {
    console.log('rendering')
  })
  return <span>{value}</span>
}

function App() {
  ...

  const MemoizedComponent = useMemo( 
    () => <ExpensiveComponent value={value}/>, 
    [value]
  )
}
```

## useCallback

useMemo가 값을 기억한다면, `useCallback은 인수로 넘겨받은 콜백 자체를 기억`

특정 함수를 새로 만들지 않고 다시 재사용

```jsx
const ChildComponent = memo( ({ name, value, onChange }) => {
  useEffect(() => {
    console.log('rendering')
  })
  ...
})

function Add() {
  ...
  return (
    <>
      <ChildComponent name="1"/>
    </>
  )
}
```

name, value, onChange의 값을 모두 기억함. 이 값이 변경되지 않았을 때에는 렌더링 되지 않음.

- 첫 번째 인수는 함수
- 두 번째 인수는 의존성 배열을 삽입

>  useCallback에 기명함수를 넘겨주면, `크롬 메모리 탭`에서 디버깅이 용이해진다.

### useMemo를 이용하여 useCallback 구현

```javascript
  export const useCallback(callback, args) {
    currentHook = 8
    return useMemo( () => callback, args )
  }
```

## useRef

`useRef`와 `useState`모두 컴포넌트 내부에서 렌더링이 일어나도 변경 가능한 상태값을 저장

- 반환값인 객체 내부에 있는 current 값에 접근 또는 변경이 가능함
- useRef는 값이 변해도 `렌더링이 발생하지 않음`

```jsx
function RefComponent () {
  const count = useRef(0)

  function handleClick() {
    count.current ++
  }

  return <button onClick={handleClick}>{count.current}</button>
}
```

가장 일반적인 사용 예로 `DOM`에 접근하는 것이 있음

useRef는 최초에 넘겨받은 기본값을 가지고 있음

useRef의 최초 기본 값은 return 문에 정의해 둔 DOM이 아닌 useRef()로 넘겨받은 인수

useRef가 선언된 당시에는 컴포넌트가 렌더링 되기 전이므로, return으로 컴포넌트가 반환되기 전임에 따라 `undefined`

### useRef 구현

```javascript
export const useRef(initialValue) {
  currentHook = 5
  return useMemo( () => { current : initialValue }, [])
}
```

## useContext

### Context란

`Props Drilling` : props를 하위 컴포넌트로 필요한 위치까지 계속해서 내려주는 기법

컴포넌트의 깊이가 깊을수록 드릴링이 깊어짐에 따라, `Context(콘텍스트)`가 생김

```jsx
const Context = createContext<{hello : string} | undefined> ()

function ParentComponent() {
  return (
    <>
      <Context.Provieder value={{ hello : 'react'}}>
        <Context.Provieder value={{ hello : 'javascript'}}>
          <ChildComponent/>
        </Context.Provieder>
      </Context.Provider>
    </>
  )
}


function ChildComponent () {
  const value = useContext(Context)

  return <>{value && value.hello}</>
}
```

`useContext`를 사용 시, 상위 컴포넌트에 선언된 `<Context.Provider>`에서 제공한 값을 사용할 수 있다.

여러개의 `Provider`가 있다면, `가장 가까운 Provider의 값`을 가져옴

## 상위 콘텍스트 존재 여부 체크

```jsx
const MyContext = createContext<{hello : string } | undefined>(undefined)


function ContextProvider({
  children,
  text
} : PropWithChildren<{ text : string }>) {
  return (
    <MyContext.Provider value={{ hello : text }}>{children}</MyContext.Provider>
  )
}

function useMyContext() {
  // useContext를 전달하는 컴포넌트에서 값을 체크 후 반환한다.
  const context = useContext(MyContext)
  if (!context) {
    throw new Error("useContext는 ContextProvider 내부에서만 사용할 수 있습니다.");
  }
  return context
}

function ChildComponent () {
  const {hello} = useMyContext()
  return <>{hello}</>
}

function ParentComponent() {
  return (
    <>
      <ContextProvider text='react'>
        <ChildComponent/>
      </ContextProvider>
    </>
  )
}

```

### useContext 주의할 점

useContext가 있는 컴포넌트는 눈으로 보이지 않는 Provider와 의존성을 가지게 됨

이를 방지하기 위해서는 useContext를 사용하는 컴포넌트를 최대한 작게 하거나 혹은 재사용되지 않을 만한 컴포넌트에서 사용해야 함.

> useContext로는 주입된 상태를 사용할 수 있을 뿐, 그 자체로는 렌더링 최적화에 아무 도움이 되지 않음.<br/>
> 최적화를 위해서는 `React.memo`를 사용해야 함. 

## useReducer

- 인수값(2~3개)
  - reducer : action을 정의하는 함수
  - initialState 
    - useReducer의 초깃값
    - init이 없는 경우, 기본값으로 사용

  - init`(필수값이 아님)`
    - useState의 인수로 함수로 넘겨줄 때처럼 지연해서 생성시키고 싶을 때 사용하는 함수
    - 인수로 넘겨주는 함수가 존재할 경우, useState와 동일하게 `게으른 초기화`가 일어나고, initialState를 인수로 init함수가 실행

- 반환값
  - state : 현재 reducer가 가지고 있는 값
  - dispatcher : state를 업데이트하는 함수
    - action을 넘겨줌(state를 변경할 수 있는 액션)
    - useState는 `값`만 넘겨주지만 useReducer는 `action`을 넘겨줌

```jsx
type State = {
  count : number
}

type Action = { type : 'up' | 'down' | 'reset', payload?: State }

function init ( count : State ) : State {
  return count
}

// 초깃값

const initialState : State = { count : 0 }

function reducer( state : State, action : Action ) : State {
  switch ( action.type ) {
    case 'up' : 
      return { count : state.count++ }
    case 'down' :
      return { count : state.count - 1 > 0 ? state_count-- : 0 }
    case 'reset' :
      return init(action.payload || { count : 0 })
    default :
      throw new Error(`Unexpected action type ${action.type}`)
  }
}

export default function App() {
  const [ state, dispatcher ] = useReducer(reducer, initialState, init)

  const handleUpButtonClick = () => {
    dispatch({ type : 'up' })
  }

  const handleDownButtonClick = () => {
    dispatch({ type : 'down' })
  }

  const handleResetButtonClick = () => {
    dispatch({ type : 'reset', payload : { count : 1} })
  }

  ...
}

```

### useReducer의 목적

> **목적** : state를 변경하는 시나리오를 제한적으로 두고, 변경을 빠르게 확인할 수 있도록 하는 것

- 복잡한 형태의 state를 사전에 정의된 dispatcher로만 수정할 수 있게 만듬 

  - state에 대한 접근은 컴포넌트에서만 가능
  - 업데이트 방법 상세정의는 컴포넌트 밖에 둠
  - state의 업데이트를 미리 정의해 둔 dispatcher로만 제한

### useReducer 구현

```javascript
function reducer(prevState, newState) {
  return typeof newState === 'function' ? newState(prevState) : newState
}

function init(initialArg : Initializer) {
  return typeof initialArg === 'function' ? initialArg() : initialArg
}

function useStaet(initialArg) {
  return useReducer(reducer, initialArg, init)
}

const useReducer = (reducer, initialArg, init) => {
  const [ state, setState ] = useState(
    init ? () => init(initialArg) : initialArg,
  )

  const dispatcher = useCallback(
    (action) => setState( (prev) => reducer(prev, action) )
    [reducer]
  )

  return useMemo( () => [state, dispatch], [sate, dispatch] )
}
```

## useLayoutEffect

모든 DOM의 변경 후에 useLayoutEffect의 콜백 함수 실행이 `동기적`으로 발생

```jsx
const [count, setCount] = useState(0)

useLayoutEffect( () => {
  console.log('useLayoutEffect', count)
}, [count])
```

### useLayoutEffect 실행순서

1. 리액트가 DOM 업데이트
2. useLayoutEffect를 실행
3. 브라우저에 변경 사항을 반영
4. useEffect를 실행

> useLayoutEffect의 실행이 종료될 때까지 기다린 다음에 화면을 그림<br/>
> useLayoutEffect가 완료될 때까지 리액트 컴포넌트는 기다리므로, 일시 중지되거나 성능에 문제가 발생할 수 있음

DOM은 계산됐지만 면에 반영되기 전에 하고 싶은 작업이 있을 때 사용하는 것이 좋음

---

## 사용자 정의 훅

서로 다른 컴포넌트 내부에서 같은 로직을 공유하고 할 때 사용

**사용자 정의 훅(Custom Hook) 이름은 `use`로 시작해야 함**

```jsx
function useOnlineStatus() {
  const [isOnline, setIsOnline] = useState(true);
  useEffect(() => {
    function handleOnline() {
      setIsOnline(true);
    }
    function handleOffline() {
      setIsOnline(false);
    }
    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);
    return () => {
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    };
  }, []);
  return isOnline;
}

import { useOnlineStatus } from './useOnlineStatus.js';

function StatusBar() {
  const isOnline = useOnlineStatus();
  return <h1>{isOnline ? '✅ 온라인' : '❌ 연결 안 됨'}</h1>;
}
...
```

## 고차 컴포넌트

- 고차 컴포넌트(HOC, High Order Component)
  - 컴포넌트 자체의 로직을 재사용하기 위한 방법

**고차 컴포넌트 훅 이름은 `with`로 시작해야 함**

```javascript
// 고차 함수 예제
function add(a) {
  return function (b) {
    return a + b
  }
}
```

```jsx
interface LoginProps { 
  loginRequired ?: boolean
}

function withLoginComponent<T>( Component : ComponentType<T> ) {
  return function (props : T & LoginProps) {
    const { loginRequired, ...restProps } = props

    if (loginRequired) {
      return <>로그인이 필요합니다.</>
    }

    return <Component {...(restProps as T)} />
  }
}

const Component = withLoginComponent( (props : {value : string}) => {
  return <h3>{props.value}</h3>
})

export default function App () {
  const isLogin = true
  return <Component value='text' loginRequired={isLogin}/>
}
```

### 고차 컴포넌트 사용 시, 주의할 점

- 부수효과를 최소화 해야 함
  - 컴포넌트의 props를 임의로 수정, 추가, 삭제하는 일이 없어야 함.
- 여러개의 고차 컴포넌트로 컴포넌트를 감쌀 경우 복잡성이 커짐

## 사용자 정의 훅과 고차 컴포넌트 중 선택 방법

### 사용자 정의 훅을 사용하는 경우

단순히 `useEffect, useState`를 사용하여, 공통 로직을 격리할 경우

### 고차 컴포넌트를 사용하는 경우

함수형 컴포넌트의 반환값, 즉 렌더링의 결과물에도 영향을 미치는 공통 로직일 경우