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

### expect.assertions

```typescript
/*
expect.assertions(number)는 assertions(주장, 행사)가 테스트동안 몇번 일어났는지를 확인해준다.

콜백에서 assertions가 실제로 호출되었는지 확인하기 위해서 비동기 코드를 테스트할 때 유용하다.

예를들어, doAsync라는 callback1과 callback2을 받는 함수가 있다고 가정해보자.
비동기로 2개의 함수를 순서없이 호출하고, 이를 테스트 할 수 있다.
*/

test('doAsync calls both callbacks', () => {
    // 해당 코드는, callback1과 callback2 둘 다 호출되었다는 걸 확증해준다.
    expect.assertions(2);
    function callback1(data) {
        expect(data).toBeTruthy();
    }
    function callback2(data) {
        expect(data).toBeTruthy();
    }

    doAsync(callback1, callback2);
});
```