# UI테스트

## 특정 DOM 요소 취득하기

```typescript
import { render, screen } from '@testing-library/react'
import { Form } from './Form'

test('이름을 표시한다.', () => {
  render(<Form name='bom'/>)
  expect(screen.getByText('bom')).toBeInTheDocument()
})
```

`screen.getByText()` : 일치하는 문자열을 가진 한 개의 텍스트 요소를 찾는 쿼리<br/>
`toBeInTheDocument()` : 해당 요소가 DOM에 존재하는지 검증하는 커스텀 매쳐

## 특정 DOM 요소를 역할로 취득하기

```typescript
test('버튼 표시', () => {
  render(<Form name='bom'/>)
  expect(screen.getByRole('button')).toBeInTheDoucment()
})

test('헤딩 찾기', () => {
  render(<Form name='bom'/>)
  expect(scrren.getByRole('heading')).toHaveTextContent('계정 정보')
})
```

`getByRole` : 역할을 찾는 쿼리
`toHaveTextContent` : 원하는 문자의 포함여부를 확인하는 매쳐

## 이벤트 핸들러 호출

```typescript
import { fireEvent, render, scrren } from '@testing-library/react'

test('버튼 클릭 시 이벤트 핸들러 실행', () => {
  const mockFn = jest.fn()
  render(<Form name='bom' onSubmit={mockFn}/>)
  fireEvent.click(screen.getByRole('button'))
  expect(mockFn).toHaveBeenCalled()
})
```
