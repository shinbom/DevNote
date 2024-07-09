# 비동기 처리 테스트

```typescript
const wait = (duration : number) => {
  return ne Promise((resolve) => {
    setTimeout( () => {
      resolve(duration)
    }, duration)
  })
}
```

```typescript
// Promise 이용
test('지정 시간을 기다린 뒤 경과 시간과 함께 resolve된다.', () => {
  return wait(50).then((duration) => {
    expect(duration).toBe(50)
  })
})

// resolve 매처를 사용하는 단언문 return
test('지정 시간을 기다린 뒤 경과 시간과 함께 resolve된다', () => {
  return expect(wait(50)).resolves.toBe(50)
})

// async/await
test('지정 시간을 기다린 뒤 경과 시간과 함께 resolve된다', async () => {
  await expect(wait(50)).resolves.toBe(50)
})

// async/awiat 더 간략한 방법
test('지정 시간을 기다린 뒤 경과 시간과 함께 resolve된다', async () => {
  expect(awiat wait(50)).toBe(50)
})

```

## Reject 테스트

```typescript
const wait = (duration : number) => {
  return ne Promise((_, reject) => {
    setTimeout( () => {
      reject(duration)
    }, duration)
  })
}
```

```typescript
// Promise 이용
test('지정 시간을 기다린 뒤 경과 시간과 함께 reject된다.', () => {
  return timeout(50).catch((duration) => {
    expect(duration).toBe(50)
  })
})

// rejects 매처를 사용하는 단언문 return
test('지정 시간을 기다린 뒤 경과 시간과 함께 reject된다.', () => {
  return expect(timeout(50)).rejects.toBe(50)
})


// async/await
test('지정 시간을 기다린 뒤 경과 시간과 함께 resolve된다', async () => {
  await expect(wait(50)).rejects.toBe(50)
})

// try-catch 활용
test('지정 시간을 기다린 뒤 경과 시간과 함께 resolve된다', async () => {
  expect.assertions(1)
  try {
    await timeout(50)
  } catch (err) {
    expect(err).toBe(50)
  }
})
```

> 비동기 처리를 할 때에는 첫번째 줄에 `expect.assertions`를 추가하면 사소한 실수를 줄일 수 있음.