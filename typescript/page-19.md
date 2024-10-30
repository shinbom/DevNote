# 함수 타입 표현식과 호출 시그니쳐

## 함수 타입 표현식 (Function Type Expression)

```typescript
type Operation = (a: number, b: number) => number;

const add: Operation = (a, b) => a + b;
const sub: Operation = (a, b) => a - b;
const multiply: Operation = (a, b) => a * b;
const divide: Operation = (a, b) => a / b;

const add2: (a: number, b: number) => number = (a, b) => a + b;
```

중복될 경우, 함수타입 표현식을 이용하여 공용적으로 사용할 수 있다.

## 호출 시그니쳐(콜 시그니쳐)

```typescript
type Operation2 = {
  (a: number, b: number): number;
};

const add: Operation2 = (a, b) => a + b;
const sub: Operation2 = (a, b) => a - b;
const multiply: Operation2 = (a, b) => a * b;
const divide: Operation2 = (a, b) => a / b;
```

## 하이브리드 타입

호출 시그니쳐 아래에 프로퍼티를 추가 정의한 경우

```typescript
type Operation2 = {
  (a: number, b: number): number;
  name: string;
};

const add2: Operation2 = (a, b) => a + b;
(...)

add2(1, 2);
add2.name;
```
