## 상품 목록

상품 목록을 얻어서 표시하는 화면을 만들자. 말 그대로 다음과 같이 두 가지로 나눌 수 있다:

1. 상품 목록 얻기
2. 상품 목록 보여주기

전자는 useFetchProducts 훅으로, 후자는 Products 컴포넌트로 구현하고, ProductListPage에선 이 둘을 조합한다.

테스트 하기 쉽게 하기 위해, 2가지를 나눠주었다.

```tsx
import Products from '../components/product-list/Products';

import useFetchProducts from '../hooks/useFetchProducts';

export default function ProductListPage() {
  const { products } = useFetchProducts();

  return (
    <div>
      <h2>Products</h2>
      <Products products={products} />
    </div>
  );
}
```

`useFetchProduct`를 할 때 2가지 선택지가 있다.

```typescript
useFetchProduct()
```

와 같이 함수를 호출만 할 것인지, 아니면 로딩, 에러등의 상태까지 받을 것인지 선택이 필요하다.

```typescript
const {products, isLoading, isError} = useFetchProduct()
```
---


```typescript
export default function Products({ products } : ProductsProps) {
  return (
    <div>
      {products.map((product) => (
        <p key={product.id}>{JSON.stringify(product)}</p>
      ))}
    </div>
  );
}

```

`JSON.stringify()`를 통해, 값이 어떻게 들어오는지 대략적으로 파악이 가능하다.

> JSON을 string으로 변환하여 화면에 나타내줌에 따라, 데이터가 올바르게 들어오고 있는지 확인하기 편리해 보인다.


```typescript
const apiBaseUrl = 'https://shop-demo-api-01.fly.dev';

export default function useFetchProducts() {
  ...
```

`apiBaseUrl` 미리 선언을 하여, 분리할 수 있도록 한다.
그리고 환경변수로 분리하여 관리하면 편하다.

```typescript
// useFetch

useFetch<Data>
```

useFetch를 사용하면서 `<Data>`와 같이 타입을 지정해줄 수 있다.

---

## Mdn Intl

```typescript
numberFormat(product.price)
```

`,` 찍는것이 국가마다 다르다.

```
  국제화 생성자 및 기타 언어 구분 함수에 공통적인 기능이 포함되어 있다. 
  전체적으로 ECMAScript 국제화 API로 구성되며, 언어에 민감한 문자열 비교, 숫자 서식, 날짜 및 시간 서식 등을 제공한다.
  ```

---

> 아샬님 : 코드가 깨끗하지 않다고 느끼는 건, 좋은 신호.

> 너무 긴 것 같으면, 더 나누고, 분리하면 된다.

> 중복인 것은 정리를 하자

---

API 호출을 모아주는 ApiService를 만든다. API의 base URL을 지정하기 위해 환경변수를 활용한다.

---

## useSearchParams

```typescript
window.location.search
```

`useSearchParams`를 이용하여 categoryId를 얻는다.

`useSearchParams`는 URL의 `Query String`을 가져오는 것이다.

### Query String

사용자가 입력 데이터를 전달하는 방법중의 하나로, url 주소에 미리 협의된 데이터를 파라미터를 통해 넘기는 것

URL주소뒤에 물음표(?)를 붙이고 key1=value1&key2=value2...방식으로 데이터를 요청

Axios는 queryString을 params를 이용하여 전달할 수 있다.

```typescript

async fetchProducts({ categoryId }: {
  categoryId?: string;
} = {}): Promise<ProductSummary[]> {
  const { data } = await this.instance.get('/products', {
    params: { categoryId },
  });
  const { products } = data;
  return products;
}

```

---

처음부터 고민해서 바로 만들어도 되고, 일단 만들고 고쳐나가도 된다.

테스트 코드가 있으면, 이런 변경 작업시 자신감을 가질 수 있다!