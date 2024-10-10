# 온라인 쇼핑몰 관리자 기능 개발

## SWR

> [SWR](https://swr.vercel.app/ko)

```bash
npm i swr
```

F/E에서 상태 관리를 아주 적극적으로 하는 흐름이 있다면, 반대로 F/E에선 캐시에 집중하고 백엔드와의 동기화에 집중하는 흐름이 있다.
B/E에 의존적인 아주 단순한 CRUD 애플리케이션을 구축할 거라 SWR를 써보도록 하겠다. 좀 더 복잡한 걸 다루고 싶다면 TanStack Query도 사용해보자.

## React Hook Form

> [React Hook Form](https://react-hook-form.com/)

```bash
npm i react-hook-form
```

단순한 CRUD 애플리케이션을 구축한다면 Uncontrolled Component를 사용하거나, 그에 준하는 편의성을 제공하는 도구를 활용할 수 있다. React Hook Form은 이 모두를 지원한다. 특히 Uncontrolled 방식에 집중해서 활용하면 리렌더링이 줄어들어 커다란 폼의 성능 문제에서 유리하다.

- [Uncontrolled Component](https://ko.legacy.reactjs.org/docs/uncontrolled-components.html)

# 관리자 페이지

관리자 사이트는 무조건 로그인을 해야 하므로, 일반페이지와 로그인 페이지를 완전 분리한다.

```tsx
  // routes.tsx
const routes = [
  { path: '/login', element: <LoginPage /> },
  {
    element: <Layout />,
    children: [
      { path: '/', element: <HomePage /> },
      { path: '/users', element: <UserListPage /> },
      { path: '/categories', element: <CategoryListPage /> },
      { path: '/categories/new', element: <CategoryNewPage /> },
      { path: '/categories/:id/edit', element: <CategoryEditPage /> },
      { path: '/products', element: <ProductListPage /> },
      { path: '/products/new', element: <ProductNewPage /> },
      { path: '/products/:id', element: <ProductDetailPage /> },
      { path: '/products/:id/edit', element: <ProductEditPage /> },
      { path: '/orders', element: <OrderListPage /> },
      { path: '/orders/:id', element: <OrderDetailPage /> },
      { path: '/orders/:id/edit', element: <OrderEditPage /> },
    ],
  },
];
```

로그인이 안되어 있을 때에는, 페이지가 리다이렉트 되도록 한다.

```tsx
import { Outlet } from 'react-router-dom';

import styled from 'styled-components';

import Header from './Header';

import useCheckAccessToken from '../hooks/useCheckAccessToken';

const Container = styled.div`
  margin-inline: auto;
  width: 90%;
`;

export default function Layout() {
  const ready = useCheckAccessToken();

  if (!ready) {
    return null;
  }

  return (
    <Container>
      <Header />
      <Outlet />
    </Container>
  );
}
```

```tsx
// useCheckAccessToken
import { useEffect, useState } from 'react';

import { useNavigate } from 'react-router-dom';

import useAccessToken from './useAccessToken';

import { apiService } from '../services/ApiService';

export default function useCheckAccessToken(): boolean {
  const [ready, setReady] = useState(false);

  const { accessToken, setAccessToken } = useAccessToken();

  const navigate = useNavigate();

  useEffect(() => {
    const fetchCurrentUser = async () => {
      try {
        await apiService.fetchCurrentUser();
        setReady(true);  
        // API에서 관리자인지 체크가 되면, ready로 상태가 변경된다.
      } catch (e) {
        setAccessToken('');
      }
    };

    fetchCurrentUser();
  }, [accessToken, setAccessToken]);

  // 기존과 다른 부분 —---------
  useEffect(() => {
    if (!accessToken) {
      navigate('/login');
    }
  }, [accessToken, navigate]);

  return ready;
}
```

> 내용이 많아지고, 복잡해지면 컴포넌트로 분리하는 것을 잊지 말자

## (SWR)([데이터 가져오기를 위한 React Hooks – SWR](https://swr.vercel.app/ko))

`mutate`는 강제로 데이터를 다시 불러오는 것

```tsx
fetcher() {
  return async (url: string) => {
    const { data } = await this.instance.get(url);
    return data;
  };
}
```

## React Hook Form

```tsx
import { useNavigate, useParams } from 'react-router-dom';

import { Controller, useForm } from 'react-hook-form';

import styled from 'styled-components';

import Button from '../components/ui/Button';

import useFetchCategory from '../hooks/useFetchCategory';

const Container = styled.div`
  h2 {
    margin-bottom: 2rem;
    font-size: 2rem;
  }

  [type=submit] {
    display: block;
    margin-block: 1rem;
  }
`;

export default function CategoryEditPage() {
  const params = useParams();

  const categoryId = String(params.id);

  const navigate = useNavigate();

  const {
    category, loading, error, updateCategory,
  } = useFetchCategory({ categoryId });

  type FormValues = {
    name: string;
    hidden: boolean;
  };

  const { handleSubmit, control } = useForm<FormValues>();

  const onSubmit = async (data: FormValues) => {
    await updateCategory({
      name: data.name,
      hidden: data.hidden,
    });
    navigate('/categories');
  };

  if (loading) {
    return (
      <p>Loading...</p>
    );
  }

  if (error || !category) {
    return (
      <p>Error!</p>
    );
  }

  return (
    <Container>
      <h2>Edit Category</h2>
      <form onSubmit={handleSubmit(onSubmit)}>
        <Controller
          control={control}
          name="name"
          defaultValue={category.name}
          render={({ field: { onChange, value } }) => (
            <div>
              <label htmlFor="input-name">이름</label>
              <input
                id="input-name"
                value={value}
                onChange={onChange}
              />
            </div>
          )}
        />
        <Controller
          control={control}
          name="hidden"
          defaultValue={category.hidden}
          render={({ field: { onChange, value } }) => (
            <div>
              <label htmlFor="input-hidden">감춤</label>
              <input
                id="input-hidden"
                type="checkbox"
                checked={value}
                onChange={onChange}
              />
            </div>
          )}
        />
        <Button type="submit">
          수정
        </Button>
      </form>
    </Container>
  );
}
```

## 주문 상태 변경

고객 지원 업무의 경우, 단순히 CRUD를 넘어 해당 도메인(비즈니스)에 대한 이해가 필요하다.
