# 커스텀 데코레이터

```typescript
// serialize.interceptor.ts

import { UseInterceptors, NestInterceptor, ExecutionContext, CallHandler } from "@nestjs/common";
import { Observable } from "rxjs";
import { map } from 'rxjs/operators';
import { plainToClass } from "class-transformer";
import { UserDto } from "src/users/dtos/user.dto";

export function Serialize(dto : any) {
  return UseInterceptors(new SerializeInterceptor(dto))
}

export class SerializeInterceptor implements NestInterceptor {
  constructor (private dto : any) {}

  intercept(context : ExecutionContext, handler : CallHandler) : Observable<any> {

    return handler.handle().pipe(
      map((data : any) => {
        return plainToClass(UserDto, data, {
          excludeExtraneousValues : true
        })
      })
    )
  }
}

```


```typescript
// user.controller.ts
import { Serialize } from 'src/interceptors/serialize.interceptor';

...
@Serialize(UserDto)
  @Get('/:id')
  async findUser(@Param('id') id : string) {
    const user = await this.userService.findOne(parseInt(id))
    if(!user) {
      throw new NotFoundException('user not found')
    }
    return user
  }
...

```

`UserInterceptor`를 반환하는 함수를 생성 후, 해당 함수만 import하여 데코레이터로 선언해준다. 

---

## 전체 컨트롤러에 Interceptor 데코레이터 적용 

```typescript

@Controller('auth')
@Serialize(UserDto)
export class UsersController {
  ...
}

```
전체 인터셉터를 구현할 때에는 Controller에 데코레이터를 선언해주면 된다.