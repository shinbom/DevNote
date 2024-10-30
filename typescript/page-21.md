# 함수 오버로딩

함수를 매개변수의 개수나 타입에 따라 여러가지 버전으로 정의하는 방법

```typescript
// 오버로드 시그니처
function func(a: number): void; // version 1
function func(a: number, b: number, c: number): void; // version 2
```

```typescript
// 구현 시그니처
function func() {}

func(); // typeError
func(1); // 오버로드 시그니처 1번 버전과 맞음
func(1, 2); // typeError
func(1, 2, 3); // 오버로드 시그니처 2번 버전과 맞음
```

오버로드 시그니처를 가지고 있으면, 함수를 호출할 때 인수들의 타입이 실제 구현부에 정의된 매개변수의 갯수를 따르지 않고, 오버로드 시그니처를 따라감.

---

```typescript
// 오버로드 시그니처
function func(a: number): void; // version 1
function func(a: number, b: number, c: number): void; // version 2
```

```typescript
// 구현 시그니처
function func(a : number, b : number; c : number) {}
```

이렇게 사용했을 때, 오버로드 시그니처 `version 1`이 오류가 발생한다.
왜냐하면 구현 시그니처에서 매개변수 3개를 필수 매개변수로 정의함에 따라, 첫번째 오버로드 시그니처의 의미가 없어지도록 만들어지게 된다.

```typescript
// 구현 시그니처
function func(a : number, b ?: number; c ?: number) {
  if(typeof b === 'number' && typeof c === 'number') {
    return console.log(a + b + c)
  }
  console.log(a * 20)
}
```

그래서, 매개변수들을 옵셔널로 만들어 `모든 오버로드 시그니처`가 의미가 있도록 만들어 줘야 한다.
