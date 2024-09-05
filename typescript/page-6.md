# 타입 별칭과 인덱스 시그니처

## 타입 별칭 (Type Alias)

타입정의를 변수처럼 하도록 도와주는 것

```typescript

type User = {
  id: number;
  name: string;
  birth : string
  location : string
}

let user : User{
} = {
  id: 1,
  name: "신봄",
  birth: "1989.02.12",
  location: "서울",
};

function func() {
  type User = {}
  // func 스코프 안의 User타입
}

```

동일한 스코프에 중복될 수 없음.

---

## 인덱스 시그니쳐(Index Signature)

```typescript
type CountryCodes = {
  [key: string]: string;
};

let countryCodes: CountryCodes = {
  Korea: "ko",
  UnitedState: "us",
  UnitedKingdom: "uk",
};
```

인덱스 시그니처를 사용 시, 객체를 정의할 때 `키와 타입의 규칙을 기준`으로 타입을 정의할 때 유용함.

```typescript
type CoutryNumberCodes = {
  [key: string]: number;
};

let countryNumbercodes: CoutryNumberCodes = {
  Korea: 410,
  UnitedState: 840,
  UnitedKingdom: 826,
};
```

인덱스 시그니처는 규칙을 위반하지만 않으면 오류가 발생되지 않는다.

꼭 필요한 `property`가 있을 경우에는 아래와 같이 타입을 선언하면 된다.

```typescript
type CoutryNumberCodes = {
  [key: string]: number;
  Korea: number;
};

type CoutryNumberAndStringCodes = {
  [key: string]: number; // 오류 발생[string 할당할 수 없음]
  Korea: string;
};
```

인덱스 시그니처와 프로퍼티의 타입을 선언할때에는 `인덱스 시그니처의 타입이 프로퍼티의 타입을 호환`해야 한다.
