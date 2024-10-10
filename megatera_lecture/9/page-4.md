# 장바구니

```typescript
type Cart = {};

export default function Cart() {}
```

`Cart 타입`과 `Cart 컴포넌트`의 이름이 겹치는 문제가 있다.

이 문제에 대한 쉬운 해법은 다음과 같다.

1. Cart타입을 가져올 때 `as CartType`을 사용하여 타입의 이름을 바꾼다.
2. Cart컴포넌트를 CartView등 다른 이름으로 바꾼다.

> 아샬님은 1번을 많이 사용함.

---

### Early Return

```typescript
  export default function Options({options} : OptionProps) {
    if(!options.length) {
      return null;
    }

  return {
    ...
  }
}
```

Return early는 함수 혹은 메소드를 작성하는 방법으로, Return early를 씀으로써 예상하는 결과가 함수의 끝에서 리턴된다. 또한, 조건이 충족되지 않았을 때 코드의 나머지 부분이 실행문을 종료(예외처리를 리턴함으로써)시킨다.

출처: [WOONY's 인사이트:티스토리](https://woonys.tistory.com/entry/Design-PatternJavaEarly-return-pattern이란)

---

## Curl

curl(client url) 명령어는 프로토콜들을 이용해 URL로 데이터를 전송하여 서버에 데이터를 보내거나 가져올때 사용하기 위한 명령줄 도구 및 라이브러리이다.

### Curl Method(HTTP Method - GET, POST, PUT, DELETE)

아무 옵션을 적지 않을 경우, 기본적으로 GET으로 동작

```curl
curl www.example.com

curl -X GET www.example.com
```
