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