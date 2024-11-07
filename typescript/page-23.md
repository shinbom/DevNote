# 타입 조작하기

기본 타입이나 별칭 또는 인터페이스로 만든 기존에 존재하던 타입을 상황에 따라 다른 타입으로 변환하는 것

```typescript

```

## 인덱스드 엑세스 타입

객체, 배열, 튜플 타입에서 특정 프로퍼티 혹은 요소의 타입을 추출하는 타입

```typescript
interface Post {
  title: string;
  content: string;
  author: {
    id: number;
    name: string;
    age: number;
  };
}

function printAuthorInfo(author: Post["author"]) {
  console.log(`${author.name} - ${author.id}`);
}

const post: Post = {
  title: "게시물 제목",
  content: "게시글 본문",
  author: {
    id: 1,
    name: "신봄",
  },
};

const author: Post["author"]["id"]; // 속성이 있으므로 사용가능
```

`Post["author"]`를 통해 Post 인터페이스에서 필요한 타입만 추출할 수 있다.

```typescript
type PostList = {
  title: string;
  content: string;
  author: {
    id: number;
    name: string;
    age: number;
  };
}[];

const post: PostList[number] = {
  title: "게시글 제목",
  content: "게시글 본문",
  author: {
    id: 1,
    name: "신봄",
  },
};

const post1: PostList[0] = {
  title: "게시글 제목",
  content: "게시글 본문",
  author: {
    id: 1,
    name: "신봄",
  },
};
```

배열타입에서 하나의 요소 타입만 가져올 경우 위와 같은 방법으로 가져올 수 있다.

```typescript
type Tup = [number, string, boolean];

type Tup0 = Tup[0];
// number

type Tup1 = Tup[1];
// string

type Tup2 = Tup[2];
// boolean

type Tup3 = Tup[number];
// number | string | boolean
```

튜플의 각 요소들도 인덱스트 엑세스 타입으로 추출이 가능하다.

주의할 점은 튜플 타입에 인덱스드 엑세스 타입을 사용할 때 인덱스에 number타입을 넣으면 마치 튜플을 배열처럼 인식하여 배열 요소의 타입을 추출하게 됨.

### 주의

```typescript
const post: Post = {
  title: "게시물 제목",
  content: "게시글 본문",
  author: {
    id: 1,
    name: "신봄",
  },
};

const key = "author";

const author: Post[key]; // Error - key는 변수고 곧 값이므로, 들어갈 수 없음

const author: Post["what"]; // Error - 속성이 없으므로 타입 오류
```

`index`에 들어올 수 있는 건 오로지 type만 들어올 수 있음

## Keyof 연산자

특정 객체 타입으로부터 프로퍼티 키들을 모두 스트링 리터럴 유니온 타입으로 추출하는 연산자

```typescript
interface Person {
  name: string;
  gender: string;
}

function getPropertyKey(person: Persoon, key: string) {
  return person[key];
  // key : string으로 할 경우, 오류가 발생
  // Person의  속성이 string에 적히는 타입들에 좁혀지지 못해서 오류
}

function getPropertyKey(person: Persoon, key: "name" | "gender") {
  return person[key];
  // 오류가 발생하지는 않지만, 새로운 프로퍼티가 추가, 수정될 때마다 바꿔줘야함.
}

function getPropertyKey(person: Persoon, key: keyof Person) {
  return person[key];
  // 타입의 모든 프로퍼티를 String Literal Union타입으로 추출함.
  // 'name' | 'gender'로 추출
}

function getPropertyKey(person: Persoon, key) {
  return person[key];
}

const person: Person = {
  name: "신봄",
  gender: "male",
};

getPropertyKey(person, "name");
```

### TypeOf와 KeyOf함께 사용하기

```typescript
const person = {
  name: "신봄",
  gender: "male",
};

type Person = typeof person;
// {name : string, gender : string}
// 타입스크립트가 추론하는 타입이 나옴.

function getPropertyKey(person: Person, key: keyof typeof person) {
  return person[key];
}

const person: Person = {
  name: "신봄",
  gender: "male",
};
```

## Mapped(맵드) 타입

기존의 객체 타입으로부터 새로운 객체 타입을 만드는 타입

```typescript
// 유저정보를 관리
interface User {
  id: number;
  name: string;
}

// 한명의 유저 정보를 불러오는 기능
function fetchUser(): User {
  return {
    id: 1,
    name: "신봄",
  };
}

// AS_IS
// 유저 수정
function updateUser(user: User) {}

// name만 변경하고 싶지만, 매개변수의 타입이 User이므로, id, name이 모두 들어가야 한다.
// 변경하고자 하는 속성외에 불필요한 데이터가 들어가게 된다.
updateUser({
  id: 1,
  name: "홍길동",
});

// TO_BE
// Mapped Type 문법
type PartialUser = {
  [key in "id" | "name"]?: User[key];
};

// `?:`로 바꾸는 것만으로, 모든 객체 타입이 옵셔널로 바뀌게 된다.

type BooleanUser = {
  [key in "id" | "name"]: boolean;
};
// 객체의 타입이 모두 boolean으로 변경되었다.

// keyof연산자로 변경
type BooleanUser = {
  [key in keyof User]: boolean;
};

// 유저의 속성을 모두 readonly로 변경
type ReadonlyUser = {
  readonly [key in keyof User]: User[key];
};

function updateUser(user: PartialUser) {}
```

필요한 속성만 프로퍼티로 보내고 싶을 때, interface를 별도로 생성하거나 하지 않을 수 있다.

> 맵드 타입은 `인터페이스`에서는 사용할 수 없다.

## 템플릿 리터럴 타입

스트링 리터럴 타입을 기반으로 정해진 패턴의 문자열만 포함하는 타입

```typescript
type Color = "red" | "black" | "green";

type Animal = "dog" | "cat" | "chicken";

// AS_IS
type ColorAnimal = "red-dog" | "red-cat" | "red-chicken" | "black-dog";

// TO_BE
type ColorAnimal = `${Color}-${Animal}`;
```
