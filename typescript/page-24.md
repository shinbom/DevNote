# 인터페이스 확장

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

## 인터페이스 확장 - 타입의 재정의

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

## 다중 확장

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
