# NextJs 통합 테스트 - Next Router

```bash
npm install --save-dev next-router-mock
```

```tsx
test("현재 위치는 메인 페이지이다.", () => {
  mockRouter.setCurrentURl("/");
  render(<Nav onCloseMenu={() => {}} />);
  const link = screen.getByRole("link", { name: "Home" });
  expect(link).toHaveAttribute("aria-current", "page");
});
```

`test.each`를 이용하여 페이이 이동에 따른 동일한 테스트를 작성할 수 있다.

```tsx
test.each([
  { url: "/", name: "Home" },
  { url: "/profile", name: "Profile" },
])("현재 위치는 메인 페이지이다.", () => {
  mockRouter.setCurrentURl("/");
  render(<Nav onCloseMenu={() => {}} />);
  const link = screen.getByRole("link", { name: "Home" });
  expect(link).toHaveAttribute("aria-current", "page");
});
```
