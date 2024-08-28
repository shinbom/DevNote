# 객체 타입

## 객체 리터럴 타입

```typescript
let user : {id : number, name : string} = {
  id : 1,
  name : '신봄'
}
```

## 선택적 프로퍼티(Optional Property)

```typescript
let user : {id : number, name?: string} = {
  id : 1
}
```

`?.`을 이용하여, 선택적 프로퍼티로 설정할 수 있다.

## 읽기전용 프로퍼티(Readonly Property)

```typescript
let user : {
  id?: number
  readonly name : string
} = {
  id : 1,
  name : '신봄'
}

user.name = '테스트' // 오류  발생
```

`readonly`를 이용하여, 프로퍼티를 읽기전용으로 만들 수 있다.
