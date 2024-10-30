# 인터페이스

타입에 이름을 지어주는 또 다른 문법

> 상호간에 약속된 규칙<br/>
> 객체의 구조를 정의하는데 특화된 문법<br/>
> (상속, 합침 등의 특수한 기능을 제공함)

```typescript
interface A {
  a: string;
  b: number;
}
```

```typescript
interface PersonWithReadonly {
  readonly name: string;
  age?: number;
}

const personReadonly: PersonWithReadonly = {
  name: "신봄",
};

person.name = "신봄2"; // 읽기전용 속성이므로 name에 할당할 수 없습니다.
```

`readonly`를 이용하여, 읽기전용 프로퍼티로 만들어 줄 수 있음.

```typescript
interface PersonWithMethod {
  readonly name: string;
  age?: number;
  sayHi: () => void;
  // sayHi() : void 로도 할 수 있다.
}

const person: PersonWithMethod = {
  name: "신봄",
  sayHi: function () {
    console.log("Hi");
  },
};
```

## 함수 오버로드 시그니처를 사용할 때

```typescript
interface PersonWithSayHi {
  readonly name: string;
  age?: number;
  sayHi: () => void;
  sayHi: (a: number, b: number) => void; // Duplicate identifier 'sayHi' (Error)
}
```

```typescript
interface Person {
  readonly name: string;
  age?: number;
  sayHi(): void;
  sayHi(a: number, b: number): void;
}
```
