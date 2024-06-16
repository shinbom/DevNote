# 인증 가드

가드 클래스에는 `canActivate`라는 메서드가 있어야 함.
이 메서드는 자동으로 호출되는데,  반환값에 따라서, 라우터 이동이 거부된다.

```typescript
// src/guards/auth.guard.ts

import {
  CanActivate,
  ExecutionContext
} from '@nestjs/common'

export class AuthGuard implements CanActivate {
  canActivate(context : ExecutionContext) {
    const request = context.switchToHttp().getRequest()

    return request.session.userId;
  }
}
```

```typescript
import { ..., UseGuard } from '@nestjs/common';
import { AuthGuard } from 'src/guards/auth.guard';


@Get('/whoami')
@UseGuards(AuthGuard) // 전역 가드 설정
whoAmI(@CurrentUser() user : User) {
  return user
}

```