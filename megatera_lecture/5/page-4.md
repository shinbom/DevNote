# Playwright

```textile
키워드

- E2E(End to End) Test
- Headless Chrome
- Puppeteer
- Playwright
- CodeceptJS
```

## Playwright

> [Playwright](https://playwright.dev/)

> [Playwright Configuration](https://playwright.dev/docs/test-configuration)

> [Ashal의 Playwright](https://github.com/ahastudio/til/blob/main/test/playwright.md)

<aside>
💡 웹 브라우저 기반 E2E 테스트 자동화 도구.
Headless Chrome을 기반으로 한 Puppeteer를 계승하면서, 더 많은 웹 브라우저를 지원한다.
</aside>

- Test Runner

Playwright 패키지 설치

```bash
npm i -D @playwright/test eslint-plugin-playwright
```

`playwright.config.ts` 파일

```jsx
import { PlaywrightTestConfig } from '@playwright/test';

const config: PlaywrightTestConfig = {
 testDir: './tests',
 retries: 0,
 use: {
     channel: "chrome",
  baseURL: 'http://localhost:8080',
  headless: !!process.env.CI,
  screenshot: 'only-on-failure',
 },
};

export default config;
```

channel이 엣지인 경우 `channel: "msedge"`을 추가한다.

tests/.eslintrc.js 파일

```bash
module.exports = {
 env: {
  jest: false,
 },
 extends: ['plugin:playwright/playwright-test'],
 rules: {
  'import/no-extraneous-dependencies': 'off',
 },
};
```

tests/home.spec.ts

```typescript
import { test, expect } from '@playwright/test';

test('Filter products', async ({ page }) => {
 await page.goto('/');

 await expect(page.getByText('Apple')).toBeVisible();

 const searchInput = page.getByLabel('Search');

 await searchInput.fill('a');

 await expect(page.getByText('Apple')).toBeVisible();

 await searchInput.fill('aa');

 await expect(page.getByText('Apple')).toBeHidden();
});

test('Click the “Increase” button', async ({ page }) => {
 await page.goto('/');

 const count = 13;

 await Promise.all((
  [...Array(count)].map(async () => {
   await page.getByText('Increase').click();
  })
 ));

 await expect(page.getByText(`${count}`)).toBeVisible();
});
```

테스트 실행

```bash
npx playwright test
```

서버를 구동한 후, `npx playwright test`를 실행해야 한다.

```bash
CI=true npx playwright test
```

`CI=true`를 작성할 경우, 브라우저 창 없이 CI에서 테스트가 진행된다.

---

.gitignore 파일에 에러 상황의 스크린샷 등이 담기는 test-results 디렉터리 추가.

```json
//gitignore
/test-results/

// gitignore에 추가되면, vsCode에서는 폴더 글자색이 회색으로 변경된다.

```

---

테스트가 실패시, test-results에 스크린샷이 저장된다.

인간 친화적인 E2E 테스팅 도구로 CodeceptJS가 있다.

- [CodeceptJS](https://codecept.io/)
- [CodeceptJS 3 시작하기](https://github.com/ahastudio/til/blob/main/test/20201207-codeceptjs.md)
- [CodeceptJS 사용](https://github.com/ahastudio/CodingLife/tree/main/20211012/react#codeceptjs-사용)

가능하면 로직들을 많이 분리하기.

가능하면, UI관심사의 분리를 통해 UI 는 간단하게, 비즈니스 로직은 따로 분리하자.

범용으로 쓸 수 있는 부분은 많이 바뀌면 영향이 클 수 있으므로, 영향이 적도록 처음부터 테스트를 하면서 코딩하는 것이 좋으며, 확실하게 만들자.
