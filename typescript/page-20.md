# 함수 타입의 호환성

특정 함수 타입을 다른 함수 타입으로 취급해도 괜찮은가를 판단하는 것

1. 반환값의 타입이 호환되는지
2. 매개변수의 타입이 호환되는지

두 가지의 기준이 함수타입에 호환된다고 볼 수 있음.

## 반환값의 타입이 호환되는 경우

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

## 매개변수의 타입이 호환되는 경우

### 매개변수의 개수가 같을 떄

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

### 매개변수의 개수가 다를 때

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
