# 응답 속성 제외

Response를 반환할 때, 필요한 값만 반환한다.

## NestJs에서 추천하는 방식 순서

1. Request
2. Controller
3. Service
4. Entity Instance 생성 후, Controller로 반환 (인스턴스를 일반 객체로 변환)
5. Controller에서 Class Serializer Interceptor를 이용하여, 응답을 가로채고 반환함.

```typescript
// user.entity.ts
import { Entity, Column, PrimaryGeneratedColumn, AfterInsert, AfterUpdate, AfterRemove } from 'typeorm'
import { Exclude } from 'class-transformer';

@Entity()
export class User {
  @PrimaryGeneratedColumn()
  id : number;

  @Column()
  email : string;

  @Column()
  @Exclude()
  password : string;
  // 비밀번호는 반환을 하지 않아야 하므로 Exclude 데코레이터를 붙임.

  ...
}
```

```typescript
//user.controller.ts
import { Body, Controller, Delete, Get, Param, Post, Query, Patch, NotFoundException, UseInterceptors, ClassSerializerInterceptor } from '@nestjs/common';
// UseInterceptor, ClassSerializerInterceptor를 import

...
  @UseInterceptors(ClassSerializerInterceptor)
  @Get('/:id')
  async findUser(@Param('id') id : string) {
    const user = await this.userService.findOne(parseInt(id))
    if(!user) {
      throw new NotFoundException('user not found')
    }
    return user
  }

```

NestJs가 추천하는 방식은 권한에 따른 데이터 조회 처리를 하기가 적절하지 않다.
그래서 커스텀 DTO를 만들어서, 처리한다.

