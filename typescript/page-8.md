# any, unknown

## any

변수의 타입을 확실히 모를 때 사용, 모든 타입이 될 수 있음.

```typescript
let anyVar: any = 10;
anyVar = "hello";
anyVar.toUpperCase();

let num: number = 10;
num = anyVar; // 타입 오류가 발생되지 않음.
```

모든 값을 할당받을 수 있으며, 모든 타입의 변수에 `any타입의 변수`를 할당 할 수 있음.

> any타입은 타입검사를 안하는 것과 똑같음.

검사가 다 통과하고, 런타임에서 오류가 발생하는 경우가 생김

---

## unknown

```typescript
let unknownVar: unknown;
unknownVar = "";
unknownVar = 1;
unknownVar.toUpperCase(); // 타입 오류 발생

let num: number = 10;
num = unknownVar; // 타입 오류 발생
```

unknown은 어떤 타입에도 할당할 수 없으며, 모든 연산에도 참가할 수 없음.

할당하고 싶다면 다음과 같이 사용하면 된다.

```typescript
if (typeof unknownVar === "number") {
  num = unknownVar;
}
```

> any타입보다는 unknown타입을 사용하는게 좋다!
