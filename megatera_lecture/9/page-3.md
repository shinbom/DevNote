# 상품 상세

## useParams

`react-router-dom`에서 제공하는 Hook

현재 URL에서 일치하는 동적 매개 변수의 키/값 쌍 개체를 반환

---

```typescript

  const { loading, error } = useFetchProduct({
    productId: String(params.id),
  });

  if (loading) {
    return (
      <p>Loading...</p>
    );
  }

  if (error) {
    return (
      <p>Error!</p>
    );
  }

  return (
    <ProductDetail />
  );

```

1. `ProductDetail`에 `Props`를 넘겨준 후 처리해도 상관없지만,
 `Props Drilling`이 일어날 수 있어서, `useFetchProduct`를 이용하여 상태의 Trigger만 한다.

2. 에러가 나는 케이스가 여러가지가 있다.

- Not Found 등

---

### Null Object Pattern

```typescript
product : ProductDetail | null = null;
```

null체크를 계속하는게 어려울 수 있으므로 다음과 같이 한다.

```typescript

product : ProductDetail = nullProductDetail;


export const nullProductDetail: ProductDetail = {
  id: '',
  category: { id: '', name: '' },
  images: [],
  name: '',
  price: 0,
  options: [],
  description: '',
};
```

[introduce Special Case - Refactoring](https://refactoring.com/catalog/introduceSpecialCase.html)

---

## E2E 테스트

테스트 해야할 항목들을 작성하면서, 테스트를 진행하면 된다.
