# 타입 좁히기

조건문등을 이용하여 넓은 타입에서 좁은 타입으로 타입을 상황에 따라 좁히는 방법

```typescript
function func(value: number | string) {
  value.toFixed(); // type error
  value.toUpperCase();
}
```

```typescript
// 타입가드를 이용하여 타입 좁히기
function fuc(value: number | string) {
  if (typeof value === "number") {
    return value.toFixed();
  }

  if (typeof value === "string") {
    return value.toUpperCase();
  }
}
```

- 클래스

```typescript
function func(value: number | string | Date | null) {
  if (typeof value === "number") {
    console.log(value.toFixed());
  } else if (typeof value === "string") {
    console.log(value.toUpperCase());
  } else if (value instanceof Date) {
    console.log(value.getTime());
  }
}
```

- 직접 만든 타입

```typescript
type Person = {
  name: string;
  age: number;
};

function func(value: number | string | Date | null | Person) {
  if (typeof value === "number") {
    console.log(value.toFixed());
  } else if (typeof value === "string") {
    console.log(value.toUpperCase());
  } else if (value instanceof Date) {
    console.log(value.getTime());
  } else if (value && "age" in value) {
    console.log(`${value.name}은 ${value.age}살 입니다`);
  }
}
```

## 타입가드

조건문과 함께 사용해 타입을 좁히는 표현

1. typeof
2. instanceof
3. in
