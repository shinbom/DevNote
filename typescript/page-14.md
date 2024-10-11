# 타입 추론

## 점진적 타입 시스템

- 변수의 타입을 직접 정의하지 않아도 변수에 담기는 초기값을 기준으로 자동으로 타입을 알아서 추론

- 타입이 정의된 변수들에 대해서는 타입을 미리 결정하고, 아직 타입이 정의되지 않은 변수들에 대해서는 자동으로 타입을 추론

## 타입추론이 가능한 상황

- 변수를 선언할 때

```typescript
let a = 10; // number로 추론
let b = "hello"; // string으로 추론
```

변수의 초깃값을 기준으로 타입을 추론함.

- 구조 분해 할당

```typescript
let c = {
  id : 1,
  name '신봄',
  profile : {
    nickname : 'bom',
  }
}

let { id, name, profile } = c
```

- 함수의 반환 값

```typescript
function func() {
  return "hello";
}
// function func() : string
```

함수의 경우에는 return값을 기준으로 추론함.

- 기본값이 설정된 매개변수

```typescript
function func(message = "hello") {
  return "hello";
}

// function func(message : string) : string
```

## 주의해야 할 상황

- 암시적으로 any타입 추론

초깃값을 생략 시, 암시적으로 any타입으로 추론

```typescript
let d;
// d: any

d = 10;
d.toFixed();
// d: number

d = "hello";
d.toUpperCase();
// d: string

d.toFixed(); // 오류
```

타입이 할당된 코드의 흐름에 따라 타입이 계속 변화한다.<br/>
이를 `any 타입의 진화`라고 한다.

이는 명시적으로 `any타입`으로 지정하는 하는 것과는 동작이 다르다.
명시적으로 any타입으로 지정했을 때에는 any타입이 유지된다.

```typescript
let e: any;
e = 10;
```

> 암묵적으로 any로 하는것은 추천되지 않음.

- const 상수의 추론

```typescript
const num = 10;
// num : 10

const str = "hello";
// num : 'hello;
```

상수는 초기화 시, 설정한 값을 변경할 수 없기 때문에 가장 좁은 타입으로 추론됨.

- 최적 공통 타입(Best Common Type)

```typescript
let arr = [1, "string"];
// (string | number) []
```

타입을 추론해서 최적의 공통 타입으로 추론
