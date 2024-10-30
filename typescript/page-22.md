# 사용자 정의 타입 가드(Custom Type Guard)

```typescript
type Dog = {
  name: string;
  isBark: boolean;
};

type Cat = {
  name: string;
  isScratch: boolean;
};

type Animal = Dog | Cat;

function warning(animal: Animal) {
  if ("isBark" in animal) {
    // 강아지
  } else if ("isScratch" in animal) {
    // 고양이
  }
}
```

프로퍼티의 이름을 기준으로 타입을 좁히면 직관적으로 별로 안좋고, 프로퍼티가 이름이 바뀌기라도 하면 타입이 잘 안좁혀지기도 함.

이를 해결하기 위해 타입을 정의하는 함수를 선언한다.

```typescript
function isDog(animal: Animal) {
  return (animal as Dog).isBark !== undefined;
}

function warning(animal: Animal) {
  if (isDog) {
    // 강아지
    animal; // (parameter) animal : Animal - 타입이 잘 좁혀지지 않음.
  } else if ("isScratch" in animal) {
    // 고양이
  }
}
```

직접 만든 함수의 반환값을 가지고는 타입을 잘 좁혀주지 않음

그래서 반환값에 대한 타입을 정의해준다.

```typescript
function isDog(animal: Animal): animal is Dog {
  return (animal as Dog).isBark !== undefined;
}

function isCat(animal: Animal): animal is Cat {
  return (animal as Cat).isScratch !== undefined;
}

function warning(animal: Animal) {
  if (isDog) {
    // 강아지
    animal; // (parameter) animal : Dog - Dog타입으로 잘 추론되고 있음.
  }

  if (isCat) {
    // 고양이
    animal; // (parameter) animal : Cat - Cat타입으로 잘 추론되고 있음.
  }
}
```
