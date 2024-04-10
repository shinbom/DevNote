# Error

```typescript
// users.controller.ts
  @Get('/:id')
  async findUser(@Param('id') id : string) {
    const user = await this.userService.findOne(parseInt(id))
    if(!user) {
      throw new NotFoundException('user not found')
    }
    return user
  }
```


```typescript
// users.service.ts
  import { ...,  NotFoundException } from '@nestjs/common';


  async update(id : number, attrs : Partial<User>) {
    const user = await this.findOne(id)
    if(!user) {
      throw new NotFoundException()
    }
    Object.assign(user, attrs);
    return this.repo.save(user)
  }

```


`NotFoundException`을 통해 오류를 발생시킨다.

[Nest Exception](https://docs.nestjs.com/exception-filters)