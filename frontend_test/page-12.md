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

## 폼 유효성 검사 테스트

> ReactHookForm에서 resolver를 이용하여, 유효성을 검증할 수 있다.

```typescript
// 목 함수

function setup() {
  const onClickSave = jest.fn();
  const onValid = jest.fn();
  const onInvalid = jest.fn();

  render(
    <PostForm
      title="신규"
      onClickSave={onClickSave}
      onValid={onValid}
      onInvalid={onInvalid}
    />
  );

  async function typeTitle(title: string) {
    const textbox = screen.getByRole("textbox", { name: "제목" });
    await user.type(textbox, title);
  }

  async function saveAsPublished() {
    await user.click(screen.getByRole("swtich", { name: "공개 여부" }));
    await user.click(screen.getByRole("button", { name: "공개하기" }));
  }

  async function saveAsDraft() {
    await user.click(
      scrren.getByRole("button", { name: "비공개 상태로 저장" })
    );
  }

  return {
    typeTitle,
    saveAsDraft,
    saveAsPublished,
    onClickSave,
    onValid,
    onInvalid,
  };
}
```

```typescript
// onInvalid 실행

import { screen, waitFor } from "@testing-library/react";

test("유효하지 않은 입력내용을 입력하여 오류가 표시된다.", async () => {
  const { saveAsDraft } = setup();
  await saveAsDraft();
  await waitFor(() => {
    expect(screen.getByRole("textbox", { name: "제목" })).toHaveErrorMessage(
      "한 글자 이상의 문자를 입력해주세요."
    );
  });
});

test("유효하지 않은 입력내용을 포함하여 저장을 눌렀을 때에는 onInvalid이벤트가 실행된다.", () => {
  const { saveAsDraft, onClickSave, onValid, onInvalid } = setup();
  await saveAsDraft();
  expect(onClickSave).toHaveCalled();
  expect(onValid).not.toHaveCalled();
  expect(onInvalid).toHaveCalled();
});
```

### toHaveErrorMessage

```
(method) TestingLibraryMatchers<E, R>.toHaveErrorMessage(text?: string | RegExp | E): R

@description
Check whether the given element has an ARIA error message or not.

Use the aria-errormessage attribute to reference another element that contains custom error message text. Multiple ids is NOT allowed. Authors MUST use aria-invalid in conjunction with aria-errormessage. Learn more from the aria-errormessage spec.

Whitespace is normalized.

When a string argument is passed through, it will perform a whole case-sensitive match to the error message text.

To perform a case-insensitive match, you can use a RegExp with the /i modifier.

To perform a partial match, you can pass a RegExp or use expect.stringContaining("partial string")`.

```

요소가 가지고 있는 aria-errormessage를 확인하는 matcher이다.

> Matcher를 사용하기 전에, 문서를 읽거나 `matchers.d.ts`를 확인하면 좋을 것 같다.
