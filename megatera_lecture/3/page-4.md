# React State

``` text
키워드

- React state란?
- DRY 원칙
- SSOT(Single Source of Truth)
- useState
- 1급 객체(first-class object)란?
- Lifting State Up
```

## Thinking in React

> [Thinking in React](https://beta.reactjs.org/learn/thinking-in-react)

- Step 3: 최소한이지만 UI 상태의 완전한 표현 찾기
- Step 4: 상태의 식별 위치 확인
- Step 5: 역 데이터 흐름 추가

## React State

"변경"을 다루기 위한 요소

"Re-rendering"이란 주제에서 다뤄진다.

컴포넌트의 state가 변경되면, 해당 컴포넌트와 하위 컴포넌트를 다시 렌더링하게 된다.

일관성과 효율성을 위해 DRY원칙을 따르는 SSOT를 만든다.

### DRY(Don't Repeat Yourself)

중복 배제(Don't Repeat Yourself)는 모든 형태의 정보 중복을 지양하는 원리이다.

### SSOT(Single Source of Truth)

단일 진실 공급원(Single Source of Truth)은 정보 모형과 관련된 모든 데이터 요소를 한 곳에서만 제어 또는 편집하도록 조직 하는 관례를 말한다.

### State의 조건

1. 변경돼야 함. 변경되지 않는 건 state로 다룰 가치가 없다.
2. 부모 컴포넌트가 props를 통해 전달한다면 state가 아님.
3. 다른 state나 props를 이용해 계산 가능하다면 state가 아님.

다루는 상태가 너무 많으면 복잡해지며, TypeScript를 잘 쓰면 직접 관리하는 상태의 수를 줄여줄 수 있다.

> (React만 쓴다면) 해당 상태에 의존적인 컴포넌트를 모두 포함하는 컴포넌트가 상태를 소유해야 함.

#### useEffect 의 잘못된 사용 예시

```tsx
// 잘못된 코드
const [fullName, setFullName] = useState('');
useEffect( () => {
 setFullName(firstName + '' + lastName)
}, [firstName, lastName])
```

```tsx
// 올바른 코드
const [firstName, setFirstName] = useState('Taylor');
const [lastName, setlastName] = useState('Swift');
const fullName = firstName + '' + lastName
```

- [“Lifting State Up”](https://ko.reactjs.org/docs/lifting-state-up.html)
- [Sharing State Between Components](https://beta.reactjs.org/learn/sharing-state-between-components)

### Lifting State Up(State 끌어올리기)

동일한 데이터에 대한 변경사항을 여러 컴포넌트에 반영해야 할 때, 가장 가까운 공통 조상으로 state를 끌어올리는 것이 좋다.

### Inverse Data Flow

하위 컴포넌트의 props로 함수를 전달. 흔히 콜백함수라고 부름.

TypeScript(정확히는 JavaScript)는 함수가 일급(first-class) 객체다.
즉, 어떤 함수를 다른 함수에 인자로 넘겨주거나, 어떤 함수를 리턴값으로 사용할 수 있다. 익명함수, 클로저 등과 함꼐 사용하면 시너지가 큼.

### [일급 함수](https://developer.mozilla.org/ko/docs/Glossary/First-class_Function)

함수가 변수처럼 다뤄지는 경우를 말한다.

- 함수를 특정 변수에 할당할 수 있다.
- 함수 호출의 인자로 함수를 넘길 수 있다.
- 함수를 반환할 수 있다.
