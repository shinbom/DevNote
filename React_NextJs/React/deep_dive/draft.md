# 임시 저장

## useEffect 중간

## 클린업 함수의 목적

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

## 의존성 배열

- 빈배열을 둘 경우[] : 비교할 의존성이 없다고 판단해 최초 렌더링 직후에만 실행

```jsx
useEffect(() => {}, []);
```

- 아무런 값이 없는 경우 : 의존성을 비교할 필요 없이 렌더링 할 때마다 실행

```jsx
// 1
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

## useEffect 구현

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

## useEffect 주의할 점

- `의존성 []`을 선언 시, 최초에 함수형 컴포넌트가 마운트됐을 때만 콜백함수가 실행이 필요한지 검토
- 첫번쨰 인수에 함수명을 부여

  - useEffect의 코드가 복잡하고 많아질수록 무슨 일을 하는 useEffect코드인지 파악이 어려움
  - `기명함수`로 변경하여, `useEffect의 목적`을 알 수 있도록 함

  ```javascript
  useEffect(
    function logActivateUser() {
      logging(user.id);
    },
    [user.id]
  );
  ```

- 거대한 useEffect를 만들지 마라
- 불필요한 외부 함수를 만들지 마라
