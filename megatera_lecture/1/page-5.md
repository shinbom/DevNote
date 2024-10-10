# Parcel + ESLint

```text
키워드

- Bundler(번들러)
  - Parcel

- Lint(린트)
  - ESLint

```

## Parcel

[Parcel 공식문서](https://parceljs.org/)

내부적으로 SWC를 사용해 기존 도구보다 빠르다.

- 참고:
  - <https://github.com/ahastudio/til/tree/main/parcel>
  - <https://github.com/ahastudio/til/tree/main/vite>

```json
// package.json

"source" : "./index.html"
```

실행할 때 실행 기준이 되는 파일 설정

### Static 파일

parcel-reporter-static-files-copy 패키지 설치 후 `.parcelrc` 파일 작성.
static 폴더의 파일을 정적 파일 로드 가능 (이미지 등 Assets)

```bash
// .parcelrc
{
  "extends": ["@parcel/config-default"],
  "reporters":  ["...", "parcel-reporter-static-files-copy"]
}
```

### 빌드 +_ 정적 서버 실행

```bush
npx parcel build
npx servor dist
```

---

## ESslint

소스코드를 분석하여 프로그램 오류, 버그, 스타일 오류, 의심스러운 구조체에 표시를 달아놓기 위한 도구

일관성 있는 코드

- 스타일 통일
- 잠재적 문제 발견
- 베스트 프랙티스 추천 > 최신 트렌드 학습

```json
// vscode - setting.json

{
  "editor.codeActionsOnSave": {
      "source.fixAll.eslint": true
  }
}
```

