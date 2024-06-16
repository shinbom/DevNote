# 로그아웃

```typescript
// users.controllers

@Post('signout')
signOut(@Session() session : any) {
  session.userId = null
}
```

```typescript
  //users.services

  findOne(id : number) {
    if(!id) return null
    
    return this.repo.findOne({
      where : {
        id
      }
    })
  }
```

findOne에서 id가 null로 들어올 경우 users의 첫번째 사용자를 반환하므로 이를 막는다.