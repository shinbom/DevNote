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
