# NextJs에서 Link 컴포넌트를 사용하는 이유

## Routing & Navigation 과정

- Routing

URL을 조작하고 구성하는 동작 > 페이지 컴포넌트와 연결해주는 것

- Navigation

페이지간의 이동과정 자체

## code split > prefetch

### code split

code split은 서버에서 일어남.

`route segment`가 code split이 일어나는 기준점이다.

### prefetch

```tsx
...

return (
  <main>
    <div>
      <Link href='/example'>Example</Link>
      <Link href='/example2'>Example2</Link>
    </div>
  </main>
)
```

> Prefetching is only enabled in production 

`build`를 한 이후, `next start`로 `production`환경일 때에는 개발자 도구 Network에 미리 prefetch된 페이지가 있는 것을 볼 수 있다.(RSC Payload)

## `<Link/>` 이용하는 이유

Link href에 할당한  router segment를 미리 prefetch하기 위해서

```tsx
  <Link href='/example'>Example</Link>
```

> `/example`이 router segment이다.

## 대안

```tsx
  const goToExample = () => {
    router.push('/example')
  }

  useEffect(() => {
    router.prefetch('/example')
  }, [router])

  ...
  return (
     <>
      <button type="button" onClick={goToExample}>Example</button>
     </>
  )
```

Link컴포넌트를 사용할 수 없을 때, `router.prefetch`를 이용하여, prefetch가 가능해지게 된다.

### 참고

[NextJs router prefetch](https://nextjs.org/docs/pages/api-reference/functions/use-router#routerprefetch)