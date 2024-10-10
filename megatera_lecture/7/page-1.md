# Routing

```
키워드

Location
pathname
```

> [Window.location](https://developer.mozilla.org/ko/docs/Web/API/Window/location)

> [Location](https://developer.mozilla.org/ko/docs/Web/API/Location)

리액트에서는 하나의 웹 페이지를 하나의 컴포넌트로 만들고, URL에 따라서 적절한 컴포넌트를 보이게 함

## Window.location

객체가 연결된 장소(URL)을 표현함.

```javascript
encodeURI('예제'); // '%EC%98%88%EC%A0%9C'
decodeURI('%EC%98%88%EC%A0%9C') // 예
```

## URL.Pathname

URL경로와 그 앞의 `/`로 이루어진 `USVString`을 반환한다.

경로가 없는 경우 빈 문자열을 반환한다.
