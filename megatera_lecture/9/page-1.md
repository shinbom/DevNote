# 개발을 위한 준비

## 용어 정의

> 서비스의 개념 정리를 통해, 만드는 것에 대한 혼선이 있을 수 있으므로 정의가 필요하다.

```
- Product: 상품
    - Summary: 상품에 대한 요약 정보
    - Detail: 상품에 대한 상세 정보
    - Image: 상품 이미지
    - Option: 상품에 대한 상세 옵션 종류 (색상, 크기 등)
        - OptionItem: 옵션에 대한 상세 옵션 값 (옵션이 색상이라면 이건 Blue, Red 같은 걸 의미함)
- Category: 상품에 대한 분류
- Cart: 장바구니
    - LineItem: 장바구니에 담긴 것 (상품, 옵션, 수량 등을 동시에 다룸)
        - 여기서도 Option과 OptionItem을 사용한다.
        - 용어는 동일하지만 Product와 다른 구성을 갖기 때문에, 여기서는 Product와 Order라는 접두어를 활용
- Order: 주문
    - 여기서도 동일한 LineItem 활용.
- User: 사용자
```

---

## 기능 정의

```
1. 상품 목록 확인
2. 상품 상세 정보 확인
3. 장바구니에 상품 담기
4. 주문하기 → 배송지 입력, 결제
5. 주문 목록 확인
6. 주문 상세 확인
7. 로그인
8. 회원 가입
```

---

## 화면 정의

```
1. 홈 페이지 - `/`
2. 상품 목록 페이지 - `/products`
3. 상품 상세 페이지 - `/products/{id}`
4. 장바구니 페이지 - `/cart`
5. 주문 페이지 - `/order`
6. 주문 완료 페이지 - `/order/complete`
7. 주문 목록 페이지 - `/orders`
8. 주문 상세 페이지 - `/orders/{id}`
9. 로그인 페이지 - `/login`
10. 회원 가입 페이지 - `/signup`
11. 회원 가입 완료 페이지 - `/signup/complete`
```

---

## REST API

REST API 문서를 보면서, 백엔드에 필요한 것들 조회한다.

필요한 부분이 필요할 떄에는, 백엔드 개발자에게 요청하여 API를 수정해야 한다.

---

## Axios

대부분 REST API호출할 떄, 자주 사용하는 라이브러리

---

## Jest-dom

React Testing Library에서 활용할 수 있는 DOM 확인용 Matcher 모음

## Test Helper

테스트 코드에서 Theme, React Router에서 문제가 발생하지 않도록 헬퍼 함수를 정리하였다.

```typescript
import { render as originalRender } from '@testing-library/react';

import React from 'react';

import { MemoryRouter } from 'react-router-dom';

import { ThemeProvider } from 'styled-components';

import defaultTheme from './styles/defaultTheme';

export function render(element: React.ReactElement) {
  return originalRender((
    <MemoryRouter initialEntries={['/']}>
      <ThemeProvider theme={defaultTheme}>
        {element}
      </ThemeProvider>
    </MemoryRouter>
  ));
}
```

## Types

MSW에서 쓸 Types들을 정리하여 미리 정의를 해둔다.

FE입장에서, 데이터를 구성할 수 있다고 하면, FE입장에서 구성을 하면 된다.
하지만, BE와 소통이 잘 되고 있다면 BE와 이야기를 하며 맞추는 것이 좋다.

---

> 이전 강의에서 진행했던 E2E Test, Styled Component, Routes, MSW는 별도로 정리하지 않았음.
