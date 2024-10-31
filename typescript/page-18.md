# 함수 타입

```typescript
// 함수
function func(a: number, b: number): number {
  return a + b;
}
```

```typescript
// 화살표 함수
const add = (a: number, b: number): number => a + b;
```

```typescript
// 매개변수
function introduce(name = "신봄", age: number, tall?: number) {
  if (typeof tall === "number") {
    console.log(`tall ${tall}`);
  }
}
```

`?:` 선택적 매개변수를 이용한 경우, `if문`을 이용하여, 타입을 좁혀주어야 한다.

선택적 매개변수는 필수적 매개변수 뒤에 배치해야 한다.

## Rest Parameter

```typescript
function getSum(...rest: number[]) {
  let sum = 0;
  rest.forEach((it) => (sum += it));
  return sum;
}

getSum(1, 2, 3, 4, 5);

// 타입 갯수 제한
function getSum(...rest: [number, number, number]) {
  let sum = 0;
  rest.forEach((it) => (sum += it));
  return sum;
}
// 매개변수 3개까지만 받을 수 있음

getSum(1, 2, 3);
```

## 함수 타입 표현식과 호출 시그니쳐

### 함수 타입 표현식 (Function Type Expression)

```typescript
type Operation = (a: number, b: number) => number;

const add: Operation = (a, b) => a + b;
const sub: Operation = (a, b) => a - b;
const multiply: Operation = (a, b) => a * b;
const divide: Operation = (a, b) => a / b;

const add2: (a: number, b: number) => number = (a, b) => a + b;
```

중복될 경우, 함수타입 표현식을 이용하여 공용적으로 사용할 수 있다.

### 호출 시그니쳐(콜 시그니쳐)

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

## 함수 타입의 호환성

특정 함수 타입을 다른 함수 타입으로 취급해도 괜찮은가를 판단하는 것

1. 반환값의 타입이 호환되는지
2. 매개변수의 타입이 호환되는지

두 가지의 기준이 함수타입에 호환된다고 볼 수 있음.

### 반환값의 타입이 호환되는 경우

```typescript
type A = () => number; // return number type
type B = () => 10; // return number literal

let a: A = () => 10;
let b: B = () => 20; // type Error
let c: B = () => 10; // type number literal

a = c;
c = a; // 다운 캐스팅은 안됨.
```

A 반환값 타입이 B 반환값 타입의 슈퍼타입이라면 두 타입은 호환됨.

### 매개변수의 타입이 호환되는 경우

#### 매개변수의 개수가 같을 떄

```typescript
type C = (value: number) => void;
type D = (value: number) => void;
type E = (value: 10) => void;

let c: C = (value) => {};
let d: D = (value) => {};

c = d;
d = c;
c = e; // type Error
```

매개변수를 기준으로 타입을 평가할 때에는 다운 캐스팅은 허용되고, 업캐스팅은 허용되지 않음

```typescript
type Animal = {
  name: string;
};

type Dog = {
  name: string;
  color: string;
};

let animalFunc = (animal: Animal) => {
  console.log(animal.name);
};
let dogFunc = (dog: Dog) => {
  console.log(dog.name);
  console.log(dog.color);
};

animalFunc = dogFunc; // TypeError
```

> 객체 개념으로 생각하면, 이해하기가 쉽다.

#### 매개변수의 개수가 다를 때

```typescript
type Func1 = (a: number, b: number) => void;
type Func2 = (a: number) => void;

let func1: Func1 = (a, b) => {};
let func2: Func2 = (a) => {};

func1 = func2;
func2 = func1; // Type Error
```

> 타입이 같은 매개변수가 있을 때

할당하려고하는 쪽은 매개변수의 갯수가 더 적을 때에만 호환이 된다.

## 함수 오버로딩

함수를 매개변수의 개수나 타입에 따라 여러가지 버전으로 정의하는 방법

```typescript
// 오버로드 시그니처
function func(a: number): void; // version 1
function func(a: number, b: number, c: number): void; // version 2
```

```typescript
// 구현 시그니처
function func() {}

func(); // typeError
func(1); // 오버로드 시그니처 1번 버전과 맞음
func(1, 2); // typeError
func(1, 2, 3); // 오버로드 시그니처 2번 버전과 맞음
```

오버로드 시그니처를 가지고 있으면, 함수를 호출할 때 인수들의 타입이 실제 구현부에 정의된 매개변수의 갯수를 따르지 않고, 오버로드 시그니처를 따라감.

---

```typescript
// 오버로드 시그니처
function func(a: number): void; // version 1
function func(a: number, b: number, c: number): void; // version 2
```

```typescript
// 구현 시그니처
function func(a : number, b : number; c : number) {}
```

이렇게 사용했을 때, 오버로드 시그니처 `version 1`이 오류가 발생한다.
왜냐하면 구현 시그니처에서 매개변수 3개를 필수 매개변수로 정의함에 따라, 첫번째 오버로드 시그니처의 의미가 없어지도록 만들어지게 된다.

```typescript
// 구현 시그니처
function func(a : number, b ?: number; c ?: number) {
  if(typeof b === 'number' && typeof c === 'number') {
    return console.log(a + b + c)
  }
  console.log(a * 20)
}
```

그래서, 매개변수들을 옵셔널로 만들어 `모든 오버로드 시그니처`가 의미가 있도록 만들어 줘야 한다.
