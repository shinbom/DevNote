# 배열과 튜플 타입

## 배열 타입

```typescript
let numArr : number[] = [1,2,3]

let strArr : string[] = ['hello', 'iam', 'bom']

let boolArr : Array<boolean> = [true, false, true]
```

1. `배열요소타입[]`로 배열 타입을 정의
2. `제네릭`을 이용하여 배열 타입을 정의

### 배열에 들어가는 요소가 다양할 경우

```typescript
let multiArr : (number | string)[] = [1, 'hello']
```

### 다차원 배열 타입 정의

```typescript
let doubleArr : number[][] = [
  [1,2,3],
  [4,5]
]
```

## 튜플 타입

길이와 타입이 고정된 배열

```typescript
let tup1 : [number, number] = [1, 2]

let tup2 : [number, string, boolean] = [1, 'hello', true]
```


### 튜플을 사용하는 이유

```typescript
const users = [
  ["이정환", 1],
  ["이아무개", 2],
  ["김아무개", 3],
  ["박아무개", 4],
  [5, "조아무개"], // <- 새로 추가
];
```

순서를 잘못 넣는 경우가 있을 수 있음에 따라, `튜플을 이용하여 실수를 방지`할 수 있다.

> 튜플도 결국 배열이다.

```typescript
let tup1: [number, number] = [1, 2];


tup1.push(1);
tup1.push(1);
tup1.push(1);
tup1.push(1);
```

튜플의 길이 제한을 `배열의 메서드인 push, pop등`을 사용할 경우, 고정된 길이를 무시하게 되므로, 주의해서 사용해야 한다.