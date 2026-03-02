---
title: TypeScript
description: 
created: 2024-10-12
modified: 2024-10-11
tags: []
---

# TypeScript

```text
키워드

- REPL
- TypeScript
    - Interface vs Type
    - 타입 추론
    - Union Type vs Intersection Type
    - Optional Parameter
```

REPL
> Read-Eval(evaluation)-Print Loop

사용자가 특정 코드를 입력하면 그 코드를 평하가고 코드의 실행결과를 출력해주는 것을 반복해주는 환경

--- 

## TypeScript

🚀 [**TypeScript 공식문서**](https://www.typescriptlang.org/ko/)

- [TypeScript for the New Programmer](https://www.typescriptlang.org/ko/docs/handbook/typescript-from-scratch.html)

- [TypeScript for JavaScript Programmers](https://www.typescriptlang.org/ko/docs/handbook/typescript-in-5-minutes.html)

```bash
npx ts-node
```

간단하게 REPL을 쓰고 싶다면 ts-node를 실행하면 된다.

### 변수에 대한 타입을 선언

```typescript
  let name : string

  let human : {
    name : string;
    age : number;
  }
```

## 타입정의하기

- [타입정의하기](https://www.typescriptlang.org/ko/docs/handbook/typescript-in-5-minutes.html#%ED%83%80%EC%9E%85-%EC%A0%95%EC%9D%98%ED%95%98%EA%B8%B0-defining-types)

- [타입과 인터페이스의 차이점](https://www.typescriptlang.org/ko/docs/handbook/2/everyday-types.html#%ED%83%80%EC%9E%85-%EB%B3%84%EC%B9%AD%EA%B3%BC-%EC%9D%B8%ED%84%B0%ED%8E%98%EC%9D%B4%EC%8A%A4%EC%9D%98-%EC%B0%A8%EC%9D%B4%EC%A0%90)

```typescript
type Human = {
  name : string;
  age : number;
}

interface Person {
  name : string;
  age : number;
} 
```

- 매개변수에도 타입을 선언할 수 있음.

- 사람에 따라 interface와 type의 선호도가 다름

```typescript
  function add(x : number, y : number) : number{
    return x + y
  }
```

- 함수의 return값에도 타입을 지정할 수 있음.

- Type이 맞지 않으면 오류가 발생됨.

### 정해진 값으로 타입을 지정

정해진 값으로도 타입을 정할 수 있음.

정해진 값만 들어갈 수 있음.

Union에서 자주 사용됨.

```typescript
let category : 'food'
```

### 배열

```typescript
let numbers : number[];
numbers =[1,2,3]
```

### Tuple

배열보다 깐깐하게 타입을 관리할 때 사용

```typescript
let pair : [string,  number];
pair = ['hp', 256]
```

### any

아무거나 다 됨.

```typescript
let a : any;
a = 1
```

### 타입추론

```typescript
const name = '홍길동';
```

타입을 선언해 주지 않아도, 자동으로 타입을 추론함.

### Union Type

여러 타입 중 하나

```typescript
type MyBool = true | false;
```

bool은 true | false

매개변수를 제한하거나 할 때, 유용하게 사용할 수 있음.

```typescript
  type Category = 'food' | 'toy' | 'bag'

  let c : Category;
  c = 'desk' // error
```

undefined를 쓸 일은 없고, 함수 매개변수(parameters)에서 사용되곤 한다. 하지만 이보다는 물음표 기호(?)를 써서 Optional Parameter로 처리하는 걸 추천

```typescript
function greeting({name?: string}) : string {
  return `Hello ${name || 'world'}`
}
```

기본값을 선언해주면 더 좋음

```typescript
function greeting({name :string = 'world'}){
  return name;
}
```

type으로 따로 빼서 사용 가능

```typescript
type Person = {
  name : string;
  age?: number
}

function greeting({name, age} : Person) {
  return `${name}, ${age}` 
}
```

### Intersection Type

- [교집합](https://www.typescriptlang.org/ko/docs/handbook/typescript-in-5-minutes-func.html#%EA%B5%90%EC%A7%91%ED%95%A9)

- [IntersectionType](https://www.typescriptlang.org/docs/handbook/2/objects.html#intersection-types)

### Generics, Utility Types, and Tips

- [Generics](https://www.typescriptlang.org/docs/handbook/2/generics.html)
- [Utility Types](https://www.typescriptlang.org/docs/handbook/utility-types.html)
- [더 좋은 타입스크립트 프로그래머로 만드는 11가지 팁](https://velog.io/@lky5697/11-tips-that-help-you-become-a-better-typescript-programmer)

### 타입스크립트 팁

- [DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped)
- [DefinitelyTyped/types](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types)
- [DefinitelyTyped/types/react](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/react)