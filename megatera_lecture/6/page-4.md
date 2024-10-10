# usestore-ts

```text
키워드

- usesotre-ts
- useSyncExternalStore
```

## Action을 메서드로 처리하기

`src/stores/ObjectStore.ts` 파일

```tsx
type Listener = () => void;

export default class ObjectStore {
  private listeners = new Set<Listener>();

  addListener(listener: Listener) {
    this.listeners.add(listener);
  }

  removeListener(listener: Listener) {
    this.listeners.delete(listener);
  }

  protected publish() {
    this.listeners.forEach((listener) => listener());
  }
}
```

`src/stores/CounterStore.ts` 파일

```tsx
import { singleton } from "tsyringe";

import ObjectStore from "./ObjectStore";

@singleton()
export default class CounterStore extends ObjectStore {
  count = 0;

  increase(step = 1) {
    this.count += step;
    this.publish();
  }

  decrease() {
    this.count -= 1;
    this.publish();
  }
}
```

`src/hooks/useObjectStore.ts` 파일

```tsx
import { useEffect } from "react";

import useForceUpdate from "./useForceUpdate";

import ObjectStore from "../stores/ObjectStore";

export default function useObjectStore<T extends ObjectStore>(store: T) {
  const forceUpdate = useForceUpdate();

  useEffect(() => {
    store.addListener(forceUpdate);
    return () => store.removeListener(forceUpdate);
  }, [store]);

  return store;
}
```

`src/hooks/useCounterStore.ts` 파일

```tsx
import { container } from "tsyringe";

import useObjectStore from "./useObjectStore";

import CounterStore from "../stores/CounterStore";

export default function useCounterStore() {
  const store = container.resolve(CounterStore);

  return useObjectStore(store);
}
```

## usestore-ts 사용

> [usestore-ts](https://usestore-ts.com/)

Store 작성.

```tsx
import { singleton } from "tsyringe";

import { Store, Action } from "usestore-ts";

@singleton()
@Store()
export default class CounterStore {
  count = 0;

  @Action()
  increase(step = 1) {
    this.count += step;
  }

  @Action()
  decrease() {
    this.count -= 1;
  }
}
```

커스텀 Hook 작성.

```tsx
import { container } from "tsyringe";

import { useStore } from "usestore-ts";

import CounterStore from "../stores/CounterStore";

export default function useCounterStore() {
  const store = container.resolve(CounterStore);
  return useStore(store);
}
```

비동기 함수에 `@Action`을 붙이면 다르게 작동할 수 있다는 점에 주의! 별도의 액션을 만들면 신경 쓸 부분이 줄어든다.

```tsx
@singleton()
@Store()
class PostStore {
  posts: Post[] = [];

  async fetchPosts() {
    this.startLoading();

    const posts = await fetchPosts();

    this.completeLoading(posts);
  }

  @Action()
  startLoading() {
    this.posts = [];
  }

  @Action()
  completeLoading(posts: Post[]) {
    this.posts = posts;
  }
}
```

## useSyncExternalStore

리엑트에서 내부적으로 제공하는 useState, useReducer와 같은 상태관리 api가 아니라, 자체적으로 상태관리 툴을 만들어 리엑트 훅과 연동시킨 상태관리 라이브러리들을 external store라고 합니다. 대표적으로 mobx, redux, recoil, jotai, xtsate, zustand, rect query등이 있습니다.

이들의 상태 관리 흐름은 리엑트에서 관찰하지 않는다.

> 나온 이유 : useSyncExternalStore이 해결하는 문제는 concurrent feature에서 발생하는 Tearing때문

concurrent feature는 렌더링 도중 들어오는 유저 인터렉션에 대해 기존 렌더링을 중지하고 인터렉션에 대한 UI를 먼저 렌더링 하기 때문에 아래처럼 빨간색으로 렌더링 트리를 업데이트하는 도중 파란색의 이터렉션으로 인해 트리의 일부분이 파란색으로 렌더링될 수 있습니다.

## 참고

- [useSyncExternalStore](https://react.dev/reference/react/useSyncExternalStore)
- [FECONF 2022 - 상태관리 이 전쟁을 끝내러 왔다](https://youtu.be/KEDUqA9JeIo)
