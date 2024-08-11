# 스토리북 테스트

스토리북에서 MSW를 사용하려면, `msw`와 `msw-storybook-addon`를 설치

```bash
npm install msw msw-storybook-addon --save-dev
```

```javascript
// .storybook/preview.js

import { initialize, mswDecorator } from "msw-storybook-addon";

export const decorators = [mswDecorator];

initialize();
```

## 스토리북의 3단계 깊은 병합

스토리북은 `Global, Component, Style`라는 세 단계의 설정이 깊은 병합 방식으로 적용된다.

- Global : 모든 스토리에 적용되는 설정 (.storybook/preview.js)
- Component : 스토리 파일에 적용할 설정 (export default)
- Story : 개별 스토리에 적용할 설정 (export const)

## 요청 핸들러 변경

요청핸들러가 적용되는 우선 순서는 Story, Component, Global 순이다.
동일한 URL을 가진 핸들러를 Story에 적용하면 이 설정이 적용된다.

```typescript
// Global
// preview.js
export const parameters = {
  ...
  msw : {
    handlers : [
      rest.get('/api/my/profile', async(_, res, ctx) => {
        return res(
          ctx.status(200),
          ctx.json({
            id : 1,
            name : 'Shinbom',
          })
        )
      })
    ]
  }
}
```

```typescript
export const NotLogginedIn: Story = {
  parameters: {
    msw: {
      handlers: [
        resg.get("/api/my/profile", async (_, res, ctx) => {
          return res(ctx.status(401));
        }),
      ],
    },
  },
};
```
