# Session

```typescript
import { NestFactory } from '@nestjs/core';
import { ValidationPipe } from '@nestjs/common';
import { AppModule } from './app.module';

// CookieSession import
// tsconfig문제로 require를 이용하여 불러옴
const cookieSession = require('cookie-session')

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  // CookieSession 적용
  app.use(cookieSession({
    keys : ['asdfasfd']
  }))

  app.useGlobalPipes(
    new ValidationPipe({
      whitelist : true
    })
  )
  await app.listen(3000);
}
bootstrap();
```


```typescript
//users.controller

@Get('/colors/:color')
setColor(@Param('color') color : string, @Session() session : any){
  session.color = color
}

@Get('/colors')
getColor(@Session() session : any) {
  return session.color
}
```

> 위 코드들은 단순 예시이다.

---

## 세션을 이용하여 정보 조회하기

```typescript
// users.controller
  @Get('/whoami')
  whoAmI(@Session() session : any) {
    return this.userService.findOne(session.userId)
  }
```

session에 userId가 없으면 `undefined`가 들어가게 되어 유저정보가 반환되지 않고, 있으면 유저정보가 반환되게 된다.

