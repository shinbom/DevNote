# 입력 테스트

```typescript
import {render, screen} from '@testing-library/react'
import mockRouter from 'next-frouter-mock'

const setup = (url : string) => {
  mockRouter.setCurrentUrl(url)
  render(<Header/>)
  cosnt combobox = screen.getByRole('combobox', { name : '공개 여부'})
  return { combobox }
}
```

```typescript
// Test

test('기본값으로 "전체"가 선택되어있다', async () => {
  const { combobox } = setup();
  expect(combobox).toHaveDisplayValue("전체");
});
```
