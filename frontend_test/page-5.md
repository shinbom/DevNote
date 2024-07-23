# 웹 API 목 객체

웹 API를 `스텁`으로 대체하여 테스트를 작성한다.<br/>
실제 응답은 아니지만 응답 전후의 관련 코드를 검증할 때 유용하게 사용할 수 있다.

```typescript
//  웹 API 클라이언트

export type Profile = {
  id : string
  name ?: string
  age ?: number
  email : string
}

export function getMyProfile() : Promise<Profile> {
  return fetch('https://myapi.testing.com/my/profile').then(async (res) => {
    const data = await res.json()
    if ( !res.ok ) {
      throw data
    }
    return data
  })
}
```

```typescript
import { getMyProfile } from '../fetchers'

export async function getGreet() {
  const data = await getMyProfile()
  if(!data.name) {
    return `안녕!`
  }
  return `안녕 ${data.name}`
}
```

## 웹 API 클라이언트 스텁

```typescript
import * as Fetchers from './fetcheres'
jest.mock('./fetcheres')


// jest.spyOn(테스트할 객체, 테스트할 함수 이름)
jest.spyOn(Fetchers, 'getMyProfile')
```

## 데이터 취득 성공을 재현한 테스트

> spyOn : 함수의 구현을 가짜로 대체하지 않고, 함수의 호출여부와 어떻게 호출되었는지만 알아내야 할 때 사용



```typescript
test('데이터 조회 성공, name이 없을 때', async () => {
  jest.spyOn(Fetchers, 'getMyProfile').mockResovedValueOnce({
    id : 'test12345',
    email : 'test@test.com'
  })
  // spyOn을 이용하여, 응답객체를 정의

  await expect(getGreet()).resolves.toBe('안녕!')
})


test('데이터 조회 성공, name이 있을 때', async () => {
  jest.spyOn(Features, 'getMyProfile').mockResolvedValueOnce({
    id : 'test12345',
    email : 'test@test.com',
    name : '봄'
  })

  await expect(getGreet()).resolves.toBe('안녕 봄!')
})
```

`mockResolvedValueOnce`를 이용하여, 성공했을 때의 응답 객체를 정리한다.

## 데이터 취득 실패를 재현한 테스트

```typescript
export const HttpError = {
  error : {
    message : 'Internal Server Error'
  }
}
```

```typescript
test('데이터 조회 실패 시', async () => {
  jest.spyOn(Fetchers, 'getMyProfile').mockRejectedValueOnce(HttpError)
  // spyOn을 이용하여, 응답객체를 정의

  await expect(getGreet()).rejectes.toMatchObject({
    error : {
      message: 'Internal Server Error'
    }
  })
})

```

`mockRejectedValueOnce`를 이용하여, 실패했을 때의 응답 객체를 정리한다.

### 예외 검증 테스트 코드

```typescript
test('데이터 취득 실패 시 예외가 throw된다.', async () => {
  expect.assertions(1);
  jest.spyOn(Fetchers, 'getMyProfile').mockRejectedValueOnce(httpError)

  try {
    await getGreet()
  } catch (error) {
    expect(error).toMatchObject(httpError)
  }
})
```