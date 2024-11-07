# 조건부 타입

## 조건부 타입 소개

조건에 따라 타입을 결정하는 문법

```typescript
type A = number extends string ? string : number; // false - number - number는 string의 서브 타입이 아님

type ObjectA = {
  a: number;
};

type ObjectB = {
  a: number;
  b: number;
};

type B = ObjectB extends ObjectA ? number : string; // true - number
```

## 제네릭과 조건부 타입

> 조건부 타입은 제네릭과 함께 쓰면 위력이 발휘된다.

```typescript
type StringnumberSwitch<T> = T extends number ? string : number;

let varA: StringNumberSwitch<number>; // true - string
let varB: StringNumberSwitch<string>; // false - number

// AS_IS
function removeSpaces(text: string | undefined | null) {
  return text.replaceAll(" ", "");
}

let result = removeSpaces('hi typescript")
result.toUpperCase() // undefined 이거나 null이면 타입 오류가 발생


// 해결방안 1 - 타입 좁히기

function removeSpaces(text: string | undefined | null) {
  if(typeof text !== 'string') {
    return undefined
  }
  return text.replaceAll(" ", "");
}

// 해결방안 2 - 타입단언
let result = removeSpaces('hi typescript') as string

// 해결방안 3 - 조건부 타입 사용
function removeSpaces<T>(text: T): T extends string ? string : undefined;

function removeSpaces(text: any) {
  if (typeof text === "string") {
    return text.replaceAll(" ", "");
  } else {
    return undefined;
  }
}
```

## 분산적인 조건부 타입

```typescript
type StringNumberSwitch<T> = T extends number ? string : number;

let c: StringNumberSwitch<number | string>; // 유니온으로 하였을 경우, 조건부 타입이 동작하지 않음
// StringNumberSwitch<number> | StringNumberSwitch<string> 유니온으로 선언된 것으로 처리 됨. - number | string

let d: StringNumberSwitch<boolean | number | string>;
// 1단계
// StringNumberSwitch<boolean> |
// StringNumberSwitch<number> |
// StringNumberSwitch<string>

// 2단계
// number |
// string |
// number

// 결과
// number | string
```

### 실용적인 예제

```typescript
type Exclude<T, U> = T extends U ? never : T;

type A = Exclude<number | string | boolean, string>;
// 1단계
// Exclude<number, string>
// Exclude<string, string>
// Exclude<boolean, string>

// 2단계
// number
// never
// booelan

// 3단계
// number | never | boolean - 유니온은 타입간의 합칩합을 만듬
// never는 공집합이므로 사라짐

// 최종
// number | boolean

type Extract<T, U> = T extends U ? T : never;

type B = Extracg<number | string | boolean, string>;
// 1단계
// Extract<number, string>
// Extract<string, string>
// Extract<boolean, string>

// 2단계
// never
// string
// never

// 3단계
// never | string
// never 는 사라짐

// 최종
// string
```

## infer(Inference - 추론) : 조건부 타입 내에서 타입 추론

```typescript
type FuncA = () => string;

type FuncB = () => number;

type ReturnType<T> = T extends () => infer R ? R : never;
// `R`은 타입 변수라고 생각하면 된다.
// infer와 함께 쓴 `R`타입은 조건식을 참으로 추론하도록 한다.

type A = ReturnType<FuncA>;
// 그래서 string으로 추론

type B = ReturnType<FuncB>;
// 그래서 number로 추론

type C = ReturnType<number>;
// () => infer R를 추론할 수 없기 때문에, 추론이 불가능해져 never
```

### infer 예제

```typescript
type PromiseUnpack<T> = T extends Promise<infer R> ? R : never;
// 1. T는 Promise타입
// 2. Promise 타입의 결과값 다입을 반환

type PromiseA = PromiseUnpack<Promise<number>>;
// number

type PromiseB = PromiseUnpack<Promise<string>>;
// string
```
