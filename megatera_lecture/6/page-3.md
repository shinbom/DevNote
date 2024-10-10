# Redux

```text
키워드

- Redux
- Reflect
```

https://redux.js.org/

```typescript
state = {};

reducer = (state, action) => {
  return {
    ...state,
  };
};
```

Reducer는 기존에 있던 state과 action을 받음

---

## Action Create Function

```typescript
function increase() {
  return {
    type: "increase",
  };
}

// JSX
<button type="button" onClick={() => dispatch(increase())}>
  Increase
</button>;
```

## Selector

```typescript
type Selector<T> = (state: State) => T;

function useSelector<T>(selector: Selector<T>): T {
  const store = useStore();
  return selector(store.state);
}

...

const count = useSelector((state) => state.count);

```

---

## Reflect

자바스크립트에는 리플렉션과 비슷한 이름의 리플렉트(Reflect) API가 있다.

```javascript
Reflect.defineProperty(foo, "name", { writable: true });
```

Obejct와 Reflect가 자바스크립으에 이미 정의된 속성을 다루는 API를 제공하지만 이것만으로 메타 프로그래밍을 하기에는 부족하다.
이를 극복하기 위해 `리플렉트 메타데이터` [Metadata Proposal - ECMAScript](https://rbuckton.github.io/reflect-metadata/)`가 제안되었다.

### 리플렉트 메타데이터(Reflect MetaData)

메타 데이터를 저장할 인터널 슬롯을 추가하고, 여기에 접근할 수 있는 ReflectAPI를 추가한다.

[Metadata] : 모든 객체의 메타데이터를 관리하기 위한 맵
[DefineMetadata] : Reflect.defineMetadata로 호출할 인터널 메소드. 객체 혹은 메소드의 메타데이터를 정의
[GetMetadata] : Reflect.getMetadata로 호출할 인터널 메소드. 객체 혹은 메소드의 메타데이터를 정의

---

#### defineMetadata()

메타키, 메타값, 대상 객체를 인자롤 받는다. 객체의 속성을 받기도 한다.
대상 객체의 메타데이터를 조회한다.
없으면 맵을 새로 만들어 저장 후 반환한다.

---

#### getMetadata()

메타 데이터 저장소(Metadata)에서 대상 객체의 메타데이터 맵을 찾는다.
없으면 프로토타입 체인을 재귀적으로 찾는다.
메타데이터 맵에서 해당 키의 값을 찾는다.
