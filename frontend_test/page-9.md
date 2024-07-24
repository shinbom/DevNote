# 컴포넌트 스냅숏 테스트

`스냅숏 테스트(snapshot test)` : UI컴포넌트가 예기치 않게 변경됐는지 검증

스냅숏을 남기고 싶은 컴포넌트의 테스트 파일에 `toMatchSnapshot` 단언문을 실행한다.

```typescript
test('snapShot', () => {
  const { container } = render(<Form name='bom'/>)
  expect(container).
})
```

> 스냅샷 테스트가 실행되면 __snapshot__ 디렉터리가 생성되고 디렉토리 안에 `테스트 /파일명.snap` 파일이 저장된다.<br/>
> snap파일은 git의 추적 대상으로 두고 커밋한다.

## 회귀 테스트 발생시키기

```typescript
test('snapShot : 변경되었는지 확인', () => {
  const { container } = render(<Form name='bom1234'/>)
  expect(container).toMatchSnapShot()
})
```

스냅숏 테스트는 이미 커밋된 .snap 파일과 현시점의 스냅숏 파일을 비교하여 차이점이 발견되면 테스트가 실패한다.

## 스냅숏 갱신

`--update Snapshot` 혹은 `-u` 옵션을 추가하면 스냅숏이 갱신된다.

```bash
npx jest --updateSnapshot
```

갱신이 의도된 것이라면 `git`에 `commit`한다.