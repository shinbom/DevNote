# 타입계층도

![](./src/타입계층도.png)

## Unknown Type

```typescript
// Unknow Type

function unknowExamp() {
  // 업 캐스팅
  let a: unknown = 1;
  let b: unknown = "hello";
  let c: unknown = true;
  let d: unknown = null;
  let e: unknown = undefined;

  // 다운 캐스팅(불가)
  let unknowVar: unknown;
  let number: number = unknowVar;
  let str: string = unknowVar;
  let bool: boolean = unknowVar;
}
```

## Never Type

```typescript
// Never Type : 모든 타입의 서브 타입(공집합)
function neverExamp() {
  function nerverFunc(): never {
    while (true) {}
  }

  let num: number = nerverFunc();
  let str: string = nerverFunc();
  let bool: boolean = nerverFunc();

  // 모든 타입의 서브타입임에 모든 타입이 들어갈 수 있다.(업 캐스팅)

  // 다운 캐스팅(불가))
  let never1: never = 10;
  let never2: never = "string";
  let never3: never = true;
}
```

## Void Type

```typescript
function voidExam() {
  function voidFunc(): void {
    console.log("hi");
  }

  // 다운 캐스팅(불가)
  let voidVar: void = undefined;
}
```

## Any Type

> 타입 계층도를 완벽히 무시

```typescript
function anyExam() {
  let unknownVar: unknown;
  let anyVar: any;
  let undefinedVar: undefined;
  let neverVar: never;

  anyVar = unknownVar;
  undefinedVar = anyVar;
  neverVar = anyVar; // 오류 발생
  // any타입은 never타입으로까지 다운 캐스팅할수는 없다.
}
```
