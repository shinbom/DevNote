# NextJs 통합 테스트 - React Context

```typescript
import { createContext } from "react";
// ToastContext.tsx
// React Context Types

export type ToastStyle = "succeed" | "failed" | "busy";

export type ToastState = {
  isShown: boolean;
  message: string;
  style: ToastStyle;
};

// React Context
export const initialState: ToastState = {
  isShown: false,
  message: "",
  style: "succeed",
};

export const ToastStateContext = createContext(initialState);

export type ToastAction = {
  showToast: (state?: Partial<Omit<ToastState, "isShown">>) => void;
  hideToast: () => void;
};

export const initialAction: ToastAction = {
  showToast: () => {},
  hideToast: () => {},
};

export const ToastActionContext = createContext(initialAction);
```

```ts
// useToastProvider.tsx

import { useCallback, useState } from "react";
import { initialState, ToastState } from "./ToastContext";

export function useToastProvider(defaultState?: Partial<ToastState>) {
  const [{ isShown, message, style }, setState] = useState({
    ...initialState,
    ...defaultState,
  });
  const showToast = useCallback(
    (props?: Partial<Omit<ToastState, "isShown">>) => {
      setState((prev) => ({ ...prev, ...props, isShown: true }));
    },
    []
  );
  const hideToast = useCallback(() => {
    setState((prev) => ({ ...prev, isShown: false }));
  }, []);
  return { isShown, message, style, showToast, hideToast };
}
```

```tsx
// index.tsx
export const ToastProvider = ({
  children,
  defaultState,
}: {
  children: ReactNode;
  defaultState?: Partial<ToastState>;
}) => {
  const { isShown, message, style, showToast, hideToast } =
    useToastProvider(defaultState);
  return (
    <ToastStateContext.Provider value={{ isShown, message, style }}>
      <ToastActionContext.Provider value={{ showToast, hideToast }}>
        {children}
        {isShown && <Toast message={message} style={style} />}
      </ToastActionContext.Provider>
    </ToastStateContext.Provider>
  );
};
```

## 테스트 코드

- 1번째 방법

  - 테스트용 컴포넌트를 만들어 인터랙션 실행

```tsx
// TestComponent를 먼저 선언
const TestComponent = ({ message }: { message: string }) => {
  const { showToast } = useToastAction();

  return <button onClick={() => showToast({ message })} show></button>;
};

test("showToast 호출", () => {
  const message = 'bom'
  render(
    // Provider 안에 TestComponent를 넣어준다.
    <ToastProvider>
      <TestComponent message={message}>
    </ToastProvider>
  )

  expect(screen.queryByRole('alert')).not.toBeInTheDocument()
  await user.click(screen.getByRole('button'))
  expect(screen.getByRole('alert')).toHaveTextContent(messgae)
});
```

- 2번째 방법

  - 초기값 주입하여 렌더링된 내용 확인

```tsx
test('Succed', () => {
  const state: ToastState = {
    isShown : true,
    messagea : '성공',
    style : 'succed'
  }

  render(
    <ToastProvider defaultState={state}>
      {null}
    </ToastPropvider>
  )
  expect(screen.getByRole('alert')).toHaveTextContent(state.message)
})

```

2번째 방법보다, 1번째 방법이 `useToastAction`을 포함하므로 더 넓은 범위의 통합 테스트라고 할 수 있다.
