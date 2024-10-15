# Tanstack Query useInfiniteQuery를

간단한 TodoList 호출로 파악한 TanstackQuery의 InifiniteScroll

```typescript
// API
import ky from "ky";

export const getTodoList = async () => {
  return ky('https://dummyjson.com/products').json();
}

// Custom Hook
import { useQuery } from '@tanstack/react-query'
import {getTodoList} from "../api/getTodoList";
export const useTodoList = () => {
  const {data} = useQuery({
    queryKey: ['todos'],
    queryFn: getTodoList,
  })

  return {
    data
  }
}
```

React TanstackQuery의 useInfiniteQuery를 이용하여 API를 호출할 때에는 searchParams를 tanstackQuery에서 관리해준다.

공식문서에 따르면,
> useInfiniteQuery에서 pageParam은 자동으로 갱신됩니다. 이 값은 getNextPageParam 함수가 반환하는 값에 따라 결정되며, 각 페이지를 요청할 때마다 자동으로 넘겨집니다. 즉, fetchNextPage를 호출하면, React Query가 알아서 적절한 pageParam을 사용해 데이터를 가져옵니다.<br/><br/>
> 예를 들어, 커서 기반 API에서 데이터를 가져오는 경우, getNextPageParam은 마지막 페이지에서 다음 커서를 반환하며, 이 값이 다음 페이지를 가져오는 데 사용되는 pageParam이 됩니다. <br/><br/>
> 따라서, pageParam을 따로 관리할 필요는 없으며, getNextPageParam에서 다음 페이지의 커서를 정확히 계산하면 페이지네이션이 원활하게 작동합니다.<br/><br/>
> [useInfiniteQuery](https://tanstack.com/query/latest/docs/framework/react/reference/useInfiniteQuery)


```typescript
// API
import ky from "ky";

export const getInfiniteTodoList = async ({ pageParam = 0 }: { pageParam: number }) : Promise<ProductsResponse> => {
  return ky(`https://dummyjson.com/products?limit=100&skip=${pageParam}`).json();
}

// Custom Hook
import {useInfiniteQuery} from '@tanstack/react-query'
import {getTodoList} from "../api/getTodoList";
import {getInfiniteTodoList} from "../api/getInfiniteTodoList";
export const useInfiniteTodoList = () => {
  const {data, fetchNextPage, error} = useInfiniteQuery({
    queryKey: ['todos'],
    queryFn: getInfiniteTodoList,
    initialPageParam : 0,
    getNextPageParam : (lastPage, allPages, lastPageParam, allPageParams) => {
      if(lastPage.skip > lastPage.total) return
      return lastPageParam + 100
    }
  })

  return {
    data,
    fetchNextPage
  }
}
```

## data.pages

useInfiniteQuery를 통해 받아온 데이터들은 data.pages에 각 값들이 담기게 되어 배열형태로 저장되게 된다.

여기에서 `products`만 빼서 사용하고 싶으면 아래와 같이 하면 된다.

```typescript
const allProducts = data.pages.flatMap((page) => page.products);
```