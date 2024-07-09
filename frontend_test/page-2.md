# 테스트 코드

> 테스트 코드 실행방법과 Jest에서 사용하는 test, describe, expect에 관한 내용은 생략하여 정리하였다.


## 조건분기

사양이 복잡할수록 조건 분기에서 버그가 많이 생긴다.<br/>
조건 분기가 있는 부분에서는 특별히 주의하면서 테스트를 작성해야 한다.

```typescript
// 최대값이 정해져 있는 더하기 함수
const add = (a : number, b : number) => {
  const sum  = a + b
  if(sum > 0) return 100
  return sum
}
```
```typescript
// Test Code

// AS-IS
test('50 + 50은 100', () => {
  expect(add(50,50)).toBe(100)
})

test('70 + 80은 100', () => {
  expect(add(70,80)).toBe(100)
})


// TO-BE
test('반환값은 첫 번째 매개변수와 두 번째 매개변수를 더한 값이다.', () => {
  expect(50, 50).toBe(100)
})

test('반환값의 상한은 100이다', () => {
  expect(add(70, 80)).toBe(100)
})
```

테스트 코드가 어떤 의도로 작성되었는지, 어떤 작업이 포함되었는지 테스트명으로 명확하게 표현되어야 한다.

---

## 예외 발생


```typescript
const add = (a : number, b : number)
```

> 요구사항 추가 : 매개변수 `a,b`는 양수만 받을수 있다.

매개변수 `a,b`는 타입 어노테이션을 통해 `number`라고 제한하고 있다.<br/>
이 때에는 어노테이션으로 충분하지 않으므로 다음과 같이 작성을 한다.

```typescript
const add = (a : number, b : number) => {
  if(a < 0 || a > 100) {
    throw new Error('0~100 사이의 값을 입력해주세요.')
  }

  if(b < 0 || b> 100) {
    throw new Error('0~100 사이의 값을 입력해주세요.')
  }
  const sum  = a + b
  if(sum > 0) return 100
  return sum
}
```

```typescript
// Test Code
  expect(() => add(-10, 110)).toThrow()
```

> 화살표 함수를 사용하면 함수에서 예외가 발생하는지 검증할 수 있다.<br/>
> Jest의 권장사항은 `Arrow Function Call`이다.

---

## `instanceof` 연산자를 활용한 세부 사항 검증

```typescript
export const checkRange = (value : number) => {
  if( value < 0  || value > 100) {
    throw new RangeError('0~100 사이의 값을 입력해주세요.')
  }
}
```

```typescript
const add = (a : number, b : number) => {
  checkRange(a)
  checkRange(b)
  // 에러를 반환하는 코드를 별도의 함수로 처리하여 더 좋은 코드가 된다.
  const sum  = a + b
  if(sum > 0) return 100
  return sum
}
```