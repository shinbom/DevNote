# 로그인 테스트

```typescript
  ...
  it('Salt 암호가 포함된 비밀번호가 있습니다.', async () => {
    const user = await service.signup('asdf@asdf.com', 'asdf')
    expect(user.password).not.toEqual('asdf');
    const [salt, hash] = user.password.split('.');
    expect(salt).toBeDefined()
    expect(hash).toBeDefined()
  })
  ...
```

실패되는 코드를 작성하고, 성공하는 테스트 코드가 되도록 테스트를 진행한다.

## 모의 구현

```typescript
describe('AuthService', () => {
  let service : AuthService;
  let fakeUsersService : Partial<UsersService>
  // 테스트 블록에서 사용할 수 있도록 변수에 service를 미리 할당한다.

beforeEach(async () => {
  // Fake 서비스 생성

  fakeUsersService = {
    find : () => Promise.resolve([]),
    create: (email : string, password : string) => Promise.resolve({id : 1,  email, password} as User)
  }
  ...
  it('회원가입시 이메일 오류가 발생한다.', async (done) => {
    fakeUsersService.find = () =>  Promise.resolve([
      {
      id : 1,
      email : 'a',
      password : '1'
      }  as User
    ])
    // 블록에서만 find가 동작할 수 있도록, 할당한다.

    try {
      await service.signup('asdf@asdf.com', 'asdf')
    } catch (err) {
      done()
    }
  })
```

`done`을 추가한 이유는, 오류가 반환될때 실행되는 함수를 만들기 위해서이다.

### 모의구현 변경

```typescript
  await expect(
    service.signup('asdf@asdf.com', 'asdf')
  ).rejects.toThrow(NotFoundException);
```

Jest가 업데이트 됨에 따라, `done`이 없어지고, 위와같이 코드가 변경되었다.

---

### 로그인 테스트 

```typescript
  it('올바른 비밀번호를 입력하여 로그인이 성공한다.',  async() => {
    fakeUsersService.find = () => 
      Promise.resolve([
        {email : 'asdf@asdf.com', password : '12345'} as User
      ])
    const user = await service.signin('asdf@asdf.com', '12345')
    expect(user).toBeDefined()
  })
```

위와 같이 하면, 오류가 발생된다.
왜냐하면, resolve로 처리된 값이  `salt + hash`가 되어있지 않기 떄문이다.

이에 대한 처리방법은 다음과 같다.

#### 간단한 방법

```typescript
const user = await service.signup('asdf@asdf.com', '12345')
console.log(user)

/*
  {
    id: 1,
    email: 'asdf@asdf.com',
    password: 'ecef47ea354a79e8.749c61941d23a1d904cafab8a68972b838763fd95362a45ae41bf4b85410b2de'
  }
  
*/

```
로 위의 값을 확인 한 후,

아래와 같이 테스트 코드를 다시 작성한다.

```typescript
  it('올바른 비밀번호를 입력하여 로그인이 성공한다.',  async() => {
    fakeUsersService.find = () => 
      Promise.resolve([
        {email : 'asdf@asdf.com', password : '15a2ab96db346c0c.4c2968606734cc319c00f59b324962b74623bafbee1a38e2f745c401f334a0c6'} as User
      ])
    const user = await service.signin('asdf@asdf.com',  '12345')
    expect(user).toBeDefined()
  })
```

#### 더 좋은 방법

> fakeUserService를 실제로 동작하도록 만든다.

```typescript
  const users : User[] = []

  fakeUsersService = {
    find : (email : string) => {
        const filteredUsers = users.filter(user => user.email === email)
        return Promise.resolve(filteredUsers)
    },
    create: (email : string, password : string) => {
      const user = {
        id : Math.floor(Math.random() * 99999), 
        email,
        password} as User
      users.push(user)
      return Promise.resolve(user)
    }
  }
  ...
  it('올바른 비밀번호를 입력하여 로그인이 성공한다.',  async() => {
    await service.signup('asdf@asdf.com', 'mypassword')

    const user = await service.signin('asdf@asdf.com', 'mypassword')
    expect(user).toBeDefined()
  })
```

실제로 동작하도록 함으로서, 테스트 코드가 더 간결해졌다.
