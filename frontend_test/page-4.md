# 목 객체

테스트 하는 대상은 웹 API자체가 아니라, 취득한 데이터에 대한 처리를 위해 데이터 대역으로 `목 객체(테스트 더블)`을 사용한다.


## 용어

- `스텁(stub)`
  - 의존 중인 컴포넌트의 대역
  - 정해진 값을 반환하는 용도
  - 테스트 대상에 할당하는 입력 값

- `스파이(spy)`
  - 함수나 메서드의 호출 기록
  - 호출된 횟수나 실행시 사용한 인수 기록
  - 테스트 대상의 출력 확인

> Jest는 `목 모듈(jest.mock)` or `목 함수(jest.fn, jest.spyOn)` API를 사용

## 스텁을 만드는 방법

> 구현이 완성되어 있지 않거나, 수정이 필요한 모듈을 의존 중인 경우, 모듈을 대체하여 테스트할 수 있게 한다.


```typescript
// greet.ts
export const greet(name : string) => {
  return `Hello! ${name}`
}
```

```typescript
import {greet} from './greet'

jest.mock('./greet')
//  jest.mock을 이용하여 import되던 greet을 대체한다.
//  undefined를 반환하게 됨.
```

```typescript
jest.mock('./greet', () => ({
  sayGoodBye : (name : string) => `잘가, ${name}`,
}))
// sayGoodBye함수를 대체함.


test('작별 인사를 반환한다.', () => {
  const message = `${sayGoodBye("봄")} 또 봐!`;
  expect(message).toBe('잘가, 봄. 또 봐!')
})
```

> 실제로 구현되지 않은 `sayGoodBye`함수(모듈)을 스텁으로 대체하여 테스트가 통과된다.

## 모듈 일부를 스텁으로 대체하기

`jest.requireActual`을 이용하여 원래 모듈의 구현을 `import`할 수 있다.

```typescript
import {greet, sayGoodBye} from './greet'

jest.mock('./greet', () => ({
  ...jset.requireActual('./greet'),
  sayGoodBye : (name : string) => `잘 가, ${name}`
}))

// sayGoodBye함수만 대체하고,실제 동작을 import한다.
```

## 라이브러리 대체하기

```typescript
jest.mock('next/router', () => require('next-router-mock'))
```

`next/router`를 `next-router-mock` 라이브러리로 대체하였다.
