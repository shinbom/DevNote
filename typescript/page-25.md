# 인터페이스 선언 합치기

```typescript
type Person = {
  name: string;
};

type Person = {
  age: number;
};
```

`type`의 경우, 식별자가 중복되면 오류가 발생한다.

```typescript
interface Person {
  name: string;
}

interface Person {
  age: number;
}

const person: Person = {
  name: "",
  age: 27,
};
```

`interface`의 경우, 에러가 발생하지 않는다.<br/>
이 이유로는 `동일한 이름으로 정의한 인터페이스들은 병합되어 정의`된다.

## 주의할 점

```typescript
interface Person {
  name: string;
}

interface Person {
  name: number;
  age: number;
}
```

동일한 이름의 인터페이스들이 동일한 이름의 프로퍼티를 서로 다른 타입으로 정의한다면 오류가 발생

일한 프로퍼티의 타입을 다르게 정의한 상황을 `충돌` 이라고 표현하며 선언 합침에서 이런 충돌은 허용되지 않음

## 모듈 보강시 사용

```typescript
// Lib 라는 라이브러리가 있을 때,
interface Lib {
  a: number;
  b: number;
}

interface Lib {
  c: string;
}

const lib: Lib = {
  a: 1,
  b: 2,
  c: "hello",
};
```

불러오는 라이브러리, 모듈들의 인터페이스, 타입을 합칠때 사용하곤 한다.
