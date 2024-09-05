# 열거형 타입(Enumerable Type : Enum Type)

여러가지 값들에 각각 이름을 부여해 열거해두고 사용하는 타입

## 숫자형 Enum

```typescript
enum Role {
  ADMIN = 0,
  USER = 1,
  GUEST = 2,
}

const user1 = {
  name: "신봄",
  role: Role.ADMIN, // 관리자
};

const user2 = {
  name: "홍길동",
  role: Role.USER, // 일반 유저
};

const user3 = {
  name: "김철수",
  role: Role.GUEST, // 게스트
};
```

```typescript
enum Role {
  ADMIN,
  USER,
  GUEST,
}

// 숫자를 입력하지 않아도, index순서대로 숫자가 지정된다.
```

```typescript
enum Role {
  ADMIN,
  USER = 10,
  GUEST,
}

// ADMIN : 0
// USER : 10
// GUEST : 11
```

## 문자형 Enum

```typescript
enum Language {
  korean = "ko",
  enbliag = "en",
}

const user = {
  name: "신봄",
  language: Language.korean, // ko
};
```

`Enum`은 컴파일 결과 사라지지 않음.
