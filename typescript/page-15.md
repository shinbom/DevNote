# 타입 단언(Type Assertion)

## 필요한 상황

```typescript
type Person = {
  name: string;
  age: number;
};

let person: Person = {};

// Person으로 미리 타입을 선언했을 때에는 초깃값에 name, age가 없으므로 타입 오류가 발생됨.
person.name = "신봄";
person.age = 23;
```

```typescript
let person = {};
// 아래와 같이 나중에 속성을 추가하기 위해 person에 아무런 타입을 제공하지 않으면, 타입의 초깃값이 {}로 처리됨에 따라, 아래코드가 타입오류가 발생되게 된다.
person.name = "신봄";
person.age = 23;
```

이를 해결하기 위해 `타입 단언` 을 사용한다.<br/>
타입 단언을 사용하는 방법은 `as`를 사용하면 된다.

```typescript
let person = {} as Person;
person.name = "신봄";
person.age = 23;
```

```typescript
type Dog = {
  name: string;
  color: string;
};

let dog: Dog = {
  name: "돌돌이",
  color: "brown",
  bread: "진도", // bread 타입 오류 발생
};

let dog: Dog = {
  name: "돌돌이",
  color: "brown",
  bread: "진도",
} as Dog;

// 위처럼 타입 단언을 하게 되면 초과 타입 검사가 발생하지 않는다.
```

## 타입 단언의 조건

> 아래 두가지 조건 중 한가지를 반드시 만족해야 함.

- A가 B의 슈퍼 타입이다.
- A가 B의 서브 타입이다.

## 다중 단언

```typescript
let num3 = 10 as unknown as string;
// 이렇게 하면 타입을 두번 단언하므로, 타입 오류는 사라지게 된다.
```

> 절대 좋은 방법은 아니다. 꼭 필요한 상황에서만 이용하기를 권장한다.

## const 단언

변수 const로 선언한 것처럼 타입이 변경됨

```typescript
let number4 = 10 as const;

let cat = {
  name: "겨울이",
  color: "white",
} as const;

cat.name = // 읽기전용 속성으로 name에 할당할 수 없음 (타입 오류 발생)
```

## Non Null 단언

타입스크립트에 null이거나 undefined 가 아님을 알려주는 단언

```typescript
type Post = {
  title: string;
  author?: string;
};

let post: Post = {
  title: "게시글",
  author: "신봄",
};

const length: number = post.author?.length; // number | undefined 으로 할당할 수 없다고 하는 타입에러 발생

const length: number = post.author!.length;
```

> !을 사용하여, null이나 undefined가 아님을 단언한다.
