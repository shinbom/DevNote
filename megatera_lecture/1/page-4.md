# Testing Library

```text
키워드

- Jest
- Describe-Context-It 패턴
- React Testing Library
```

## Jest

🚀 [**Jest 공식문서**](https://jestjs.io/)

거의 모든 것을 갖춘 테스팅 도구.

Mocha와 Chai처럼 RSpec의 describe-it을 지원하고, expect로 단언(assertion)할 수 있다. Mocking도 다양한 레벨에서 쉽게 사용할 수 있다.

>fileName.test.ts 형태로 생성

```typescript
//  main.test.ts
test('Test의 설명' , () => {
  expect(1 + 2).toBe(3)
})
```


```json
// package.json
"watch:test" : "jest --watchAll"
```

의도를 드러내고 중복을 제거하기
watchAll을 통해, test코드가 변경될 때마다 테스트를 감지할 수 있다.

## Describe-Context-It 패턴

```typescript
describe('add 함수', () => {
  it('returns sum of two numbers' , () => {
    expect(add(1,2).toBe(3));
  })
})
```

표현력이 좋아지고, 고민할 기회가 생김

## React Testing Library

React UI테스트에 특화된 라이브러리

F/E 테스트시, React 컴포넌트 테스트만 테스트 하는 상황은 최대한 피하는게 좋음.

```typescript
screen.getByText('Hello'); // 텍스트가 일치하는지
screen.getByText(/Hello/); // 텍스트가 있는지

// eslint-disable-next-line @typescript-eslint/no-unsafe-call
expect(screen.queryByText(/Hi/)).toBeInTheDocument();
expect(screen.queryByText(/Hi/)).not.toBeInTheDocument();
```

toBeInTheDocument가 matcher에 안잡힐 경우가 있으므로, jest.setup.js와 '@testing-library/jest-dom'을 jest.config.js에서 setupFilesAfterEnv에 올바르게 호출해주어야 하는 것 같다.
'// eslint-disable-next-line @typescript-eslint/no-unsafe-call' 을 통해 lint를 해결하였다.


- [프론트엔드(Front-end)도 테스트해야 하나요?](https://youtu.be/-kUmsKRmOnA)
- [Mocking 때문에 테스트 코드를 작성하기 어렵나요](https://youtu.be/RoQtNLl-Wko)
