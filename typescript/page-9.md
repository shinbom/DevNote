# Void타입과 Never타입

## Void

아무것도 없음을 의미하는 타입

```typescript
function func1(): string {
  return "Hello";
}

function func2(): void {
  console.log("Hello");
}
```

## Never

불가능한 타입

```typescript
function func1(): never {
  while(true){}
}

function error : never {
  throw new Error()
}
```

반환값이 있는게 모순적일 때 사용함.

> any 타입의 값도 never타입에는 할당할 수 없음.
