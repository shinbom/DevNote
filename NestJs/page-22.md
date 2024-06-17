# 테스트 코드 리팩토링

기존 테스트 코드는 DI부터 서비스 호출까지 동일한 논리를 반복해야 한다.

```typescript
import {Test} from '@nestjs/testing'
import { AuthService } from './auth.service'
import { UsersService } from './users.service'
import { User } from './user.entity'

let service : AuthService;

describe('AuthService', () => {
  beforeEach(async () => {
  // Fake 서비스 생성

    const fakeUsersService : Partial<UsersService> = {
      find : () => Promise.resolve([]),
      create: (email : string, password : string) => Promise.resolve({id : 1,  email, password} as User)
    }
    // Test DI Container 생성
    const module = await Test.createTestingModule({
      providers : [
        AuthService,
        {
          provide : UsersService,
          useValue : fakeUsersService
        }
        // DI시스템을 속이거나, 경로를 바꾸는 방법
        // UsersService를 요청한 경우, fakeUsersService를 제공
      ]
    }).compile()

    // 모듈에서 AuthService 인스턴스 생성
    service = module.get(AuthService)

  })

  it('AuthService를 만들 수 있습니다.', async () => {
    expect(service).toBeDefined()
  })
})

```

`beforeEach`를 통해, 테스트 전 동일한 논리가 설정되도록 할 수 있다.