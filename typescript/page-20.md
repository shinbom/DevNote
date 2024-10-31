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

## 인터페이스 확장

```typescript
interface Animal {
  name: string;
  color: string;
}

interface Dog extends Animal {
  isBark: boolean;
}

const dog: Dog = {
  name: "",
  color: "",
  isBark: true,
};

interface Cat extends Animal {
  isScratch: boolean;
}

interface Chicken extends Animal {
  isFly: boolean;
}
```

`extends`를 통해, 인터페이스를 확장

### 인터페이스 확장 - 타입의 재정의

```typescript
interface Animal {
  name: string;
  color: string;
}

interface Dog extends Animal {
  name: "hello"; // hello string literal
  isBark: boolean;
}

// Dog 인터페이스를 통해 name 타입을 재정의

cosnt dog : Dog = {
  name :'',  // ''형식은 'hello'형식에 할당할 수 없습니다.
  color :'',
  isBark :true
}
```

인터페이스 타입의 재정의 규칙은 다음과 같다.

> 재정의 하는 타입이 원본 타입의 서브 타입이어야만 함.

```typescript
type Animal = {
  name: string;
  color: string;
};

interface Dog extends Animalk {
  isBark: boolean;
}
```

타입 별칭이어도 확장이 가능하다.

### 다중 확장

```typescript
interface DogCat extends Dog, Cat {}

const dogCat: DogCat = {
  name: "",
  color: "",
  isBark: true,
  isScratch: true,
};
```

여러개의 인터페이스를 확장할 수도 있다.

## 인터페이스 선언 합치기

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
