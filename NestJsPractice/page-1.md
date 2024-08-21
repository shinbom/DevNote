# NestJs 회원가입 관련 학습내용 정리

[인증 - NestJs 학습내용](../NestJs/page-16.md)

인증을 할 때에는, 암호화가 필요하다.<br/>

단순 암호화가 아니라 `salt`를 이용한다.

> Salt란 ? 해시함수를 돌리기 전에 원문에 임의의 문자열을 덧붙이는 것을 말함. <br/>
> 단어 뜻 그대로 원문에 임의의 문자열을 붙인다는 의미의 소금친다(salting) 는 것이다.

## `Salt`를 해야하는 이유

1. 해시 함수의 약점 보완

해시 함수는 동일한 입력값에 대해 항상 동일한 출력값을 생성함.<br/>
이에 따라, 동일한 비밀번호를 가진 사용자들이 있을 경우, 해시값도 동일함에 따라 해시 값을 기반으로 비밀번호를 `역추적`할 수 있는 위험이 있다.

2. 레인보우 테이블 공격 방지

[레인보우 테이블](../NestJs/page-16.md)

레인보우 테이블에는 흔히 사용되는 비밀번호와 그에 대한 해시 값이 포함되어 있어, 해시 값만으로도 비밀번호를 알아낼 수 있게 된다.

> salt를 사용하면 비밀번호가 동일하더라도 해시 값이 달라져서 공격자가 비밀번호를 추측하거나 역공학을 통해 알아내는 것을 어렵게 만든다, 이에따라 사용자의 비밀번호를 더욱 안전하게 보호하는 중요한 보안 조치이다.

---

### Bcrypt 이용

```bash
yarn add bcrypt
yarn add @types/bcrypt -D
```

```typescript
bcrypt.hash(myPlaintextPassword, saltRounds, function(err, hash) {
    // hash데이터가 반환됨.
});
```

bcrypt.hash 함수로 인해 생성된 hash는 생성할 때마다 매번 다른 값이 생성되고, `saltOrRounds = 10` 으로 설정하면 2^10번 해싱을 반복한다.

```typescript

import * as bcrypt from 'bcrypt'

...
bcrypt.hash(data.password, 10) // Hash 암호화

```

`import bcrypt from 'bcrypt'`로 할 경우, `TypeError: Cannot read properties of undefined (reading 'hash')` 발생한다.<br/>
이는 CommonJs와 ES Module의 차이점 때문이다. <br/>
CommonJS에는 default가 없다.

```bash
result ::: $2b$10$pBK.Bzu7DXNy7voxNdSiwObaf1Tlwet3NzRNNg3qWtLITRp/M9w.2
```

동일한 암호인지 확인하기 위한 방법으로는 `bcrypt.compareSync()`를 사용하면 된다.

```typescript
bcrypt.compareSync(plainString, hashString)
```

이를 통해, 로그인 시 동일한 암호를 가진 사용자인지 확인을 할 수 있다.

```typescript

// member.service
async signInMember(data: SigninMemberDto): Promise<boolean> {
  const member = await this.repo.findOne({
    where: {
      email: data.email,
    },
  });

  if (!member) {
    throw new HttpException('유저가 없습니다.', HttpStatus.NOT_FOUND);
  }

  const isCompare = await bcrypt.compare(data.password, member.password);

  if (!isCompare) {
    throw new HttpException(
      '이메일 또는 암호가 틀렸습니다.',
      HttpStatus.UNAUTHORIZED,
    );
  }

  return isCompare;
}

```

회원가입 후, `Cookie` or `Session`과 같은 처리를 추가적으로 해보자.