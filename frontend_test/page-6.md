# 목 함수를 사용하는 스파이

스파이는 테스트 대상에 발생한 입출력을 기록하는 객체

## 실행됐는지 검증

> toBeCalled<br/>
> 함수가 호출되었는지 검증

```typescript
test('목 함수 실행 : 실행 검증', () => {
  const mockFn = jest.fn()
  mockFn()
  expect(mockFn).toBeCalled()
})
```

## 실행 횟수 검증

> toHaveBeenCalledTimes
> 함수가 몇 번 호출되었는지 검증

```typescript
test('목 함수 실행 : 횟수 체크', () => {
  const mockFn = jest.fn()
  mockFn()
  expect(mockFn).toHaveBeenCalledTimes(1);
  mockFn()
  expect(mockFn).toHaveBeenCalledTimes(2);
})
```

## 실행 시 인자 검증

> toHaveBeenCalledWith

## 인자 기록

```typescript
test('목 함수 : 인자 기록', () => {
  const mockFn = jest.fn()
  const greet = (message : string) => {
    mockFn(message)
  }
  greet('hello')
  expect(mockFn).toHaveBeenCalledWith('hello')
})
```

mockFn은 전달받은 인자를 저장하고 있다.

### 스파이로 활용

```typescript
  const greet = (name : string, callBack ?: (message:string)) => {
    callBack?.(`Hello! ${name}`)
  }


  test('목 함수 : 테스트 대상의 인자로 사용', () => {
    const mockFn = jest.fn()
    greet('Bom', mockFn)

    expect(mockFn).toHaveBeenCalledWith('Hello! Bom')
  })
```

> 인자가 배열, 객체일 때에도 검증도 가능하다.
