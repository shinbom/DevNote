# 커스텀 데코레이터 & 인터셉터

## 커스텀 데코레이터

```typescript
// decorators/current-user.decorator.ts

import {
  createParamDecorator,
  ExecutionContext
} from '@nestjs/common'

export const CurrentUser = createParamDecorator(
  (data : any, context : ExecutionContext) => {
    return 'hi there!'
  }
)
```

```typescript
//users.controller.ts
  import { CurrentUser } from './decorators/current-user.decorator'

  @Get('/whoami')
  whoAmI(@CurrentUser() user : string) {
    return user;
  }
```

함수를 만들듯이 `createParamDecorator`를 데코레이터를 만들어 처리하는 데코레이터를 만든다.

## 인터셉터


```typescript
// interceptors/current-user-interceptor.ts

import {
  NestInterceptor,
  ExecutionContext,
  CallHandler,
  Injectable
} from '@nestjs/common'
import { UsersService } from '../users.service'

@Injectable()
export class CurrentUserInterceptor implements NestInterceptor{
  constructor(private usersService : UsersService) {}

  async intercept(context : ExecutionContext, handler : CallHandler) {
    const request = context.switchToHttp().getRequest()
    const { userId } = request.session || {};

    if(userId) {
      const user = await this.usersService.findOne(userId)
      request.currentUser = user
    }

    return handler.handle()
  }
}
```


```typescript
// decorators/current-user.decorator.ts

import {
  createParamDecorator,
  ExecutionContext
} from '@nestjs/common'

export const CurrentUser = createParamDecorator(
  (data : any, context : ExecutionContext) => {
    const request = context.switchToHttp().getRequest();
    return request.currentUser
  }
)
```

데코레이터를 사용함으로서, 가독성이 좋아질 수 있다.

## 인터셉터를 의존성 주입과 연결하기

> 아래 소스는 컨트롤러에만 Interceptor를 설정

```typescript
// users.module.ts

...

@Module({
  imports : [TypeOrmModule.forFeature([User])],
  controllers: [UsersController],
  providers: [UsersService, AuthService, CurrentUserInterceptor]
})
export class UsersModule {}
```

작성한 `CurrentUserInterceptor`를 provider에 넣어준다.

```typescript
import { ..., UseInterceptors, ... } from '@nestjs/common';
...
import { CurrentUserInterceptor } from './interceptors/current-user.interceptor';

@Controller('auth')
@Serialize(UserDto)
@UseInterceptors(CurrentUserInterceptor)
export class UsersController {
  constructor(
    ...
  ){}
```

## 전역 인터셉터

```typescript
import { Module } from '@nestjs/common';
import { APP_INTERCEPTOR } from '@nestjs/core'; // 전역 Interceptor import
import { TypeOrmModule } from '@nestjs/typeorm';
import { UsersController } from './users.controller';
import { UsersService } from './users.service';
import { User } from './user.entity';
import { AuthService } from './auth.service';
import { CurrentUserInterceptor } from './interceptors/current-user.interceptor';

@Module({
  imports : [TypeOrmModule.forFeature([User])],
  controllers: [UsersController],
  providers: [
    UsersService, 
    AuthService,
    {
      provide : APP_INTERCEPTOR,
      useClass : CurrentUserInterceptor
    }
  ]
})
export class UsersModule {}

```