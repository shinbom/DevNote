# 제네릭

```typescript
function func<T>(value: T): T {
  return value;
}

let num = func(10);
```

> 제네릭(Generic) : 일반적인, 포괄적인

`제네릭 함수`로 만들어, 인수에 따라서 반환 값의 타입을 가변적으로 정할 수 있음.

`<T>`은 타입 변수

함수를 호출할 때마다 결정됨.

## 타입변수를 명시적으로 직접 정의

```typescript
function func<T>(value: T): T {
  return value;
}

let arr = func<[number, number, number]>([1, 2, 3]);
```

## 타입 변수 응용하기

```typescript
function swap<T, U>(a: T, b: U) {
  return [b, a];
}

const [a, b] = swap("1", 2);
```

타입변수는 여러개를 사용할 수 있다.

```typescript
function returnFirstValue<T>(data: T) {
  // T로만 했을때에는 return에 타입에러가 발생한다.
  // 왜냐하면 타입변수가 어떤것이 들어올지 모르기때문에 "unknown"으로 추론되기 때문이다.
  return data[0];
}

function returnFirstValue<T>(data: T[]) {
  // 이를 해결하기 위한 방법으로는 들어오는 데이터를 배열형태로 바꿔주면 된다.
  // 이렇게 하면 return되는 배열의 인덱스를 "unknown[]"로 추론할 수 있기 때문이다.
  return data[0];
}

function returnFirstValue<T>(data: T, ...unknown[]) {
  // 튜플타입으로 해도 타입 추론이 잘 된다.
  // 첫번쨰값만 리턴할것이기 때문에 2번째 인자부터는 알 필요가 없음.
  return data[0];
}

let num = returnFirstValue([0, 1, 2]); // return number

let str = returnFirstValue(["hello", "mynameis"]); // return string

let str = returnFirstValue([1, "hello", "mynameis"]); // return number | string
```

```typescript
function getLength<T extends { length: number }>(data: T[]) {
  return data.length;
}

let var1 = genLength([1, 2, 3]); // 3
let var2 = getLength("12345"); // 5
let var3 = getlength({ length: 10 }); // 10

let var4 = getLength(10); // number형식의 인수는 {length : number} 형식에 할당될 수 없음.
```

## map, forEach 메서드 타입 정의

```typescript
// map

const arr = [1, 2, 3];
const newArr = arr.map((it) => it * 2); // [2, 4, 6]

// map<U>(callbackFn : (value : T, index : number, array : T[]) => U, thisArg?: any) : U[];

function map<T, U>(arr: T[], callback: (item: T) => U): U[] {
  let result = [];
  for (let i = 0; i < arr.length; i++) {
    result.push(callback(arr[i]));
  }
  return result;
}

map(arr, (it) => it.toString());
```

```typescript
// forEach

function forEach<T>(arr: T[], callback: (item: T) => void) {
  for (let i = 0; i < arr.length; i++) {
    callback(arr[i]);
  }
}

forEach(arr2, (it) => {
  console.log(it.toFixed);
});
```

## 제네릭 인터페이스와 제네릭 타입 별칭

### 제네릭 인터페이스

> 타입 변수 = 타입 파라미터 = 제네릭 타입 변수 = 제네릭 타입 파라미터

```typescript
interface KeyPair<K, V> {
  key: K;
  value: V;
}

let keyPair: KeyPair<string, number> = {
  key: "key",
  value: 0,
};

let keyPair2: KeyPair<boolean, string[]> = {
  key: true,
  value: ["1"],
};
```

### 인덱스 시그니처(Index Signature)

```typescript
interface NumberMap {
  [key: string]: number;
}

let numberMap1: NumberMap = {
  key: -1231,
  key2: 123123,
};

interface Map<V> {
  [key: string]: V;
}

let stringMap: Map<string> = {
  key: "value",
};

let booleanMap: Map<boolean> = {
  key: true,
};
```

### 제네릭 타입 별칭

```typescript
type Map2<B> = {
  [key: string]: V;
};

let stringMap2: Map2<string> = {
  key: "hello",
};
```

### 제네릭 인터페이스의 활용 예시

> 유저 관리 프로그램<br/>
> 유저 구분 : 학생 유저 / 개발자 유저

```typescript
interface Student {
  type: "student";
  school: string;
}

interface Developer {
  type: "developer";
  skill: string;
}

interface User<T> {
  name: string;
  profile: T;
}

function goToSchool(user: User<Student>) {
  const school = user.profile.school;
  console.log(`${school}로 등교 완료`);
}

const developerUser: User<Developer> = {
  name: "이정환",
  profile: {
    type: "developer",
    skill: "TypeScript",
  },
};

const studentUser: User<Student> = {
  name: "홍길동",
  profile: {
    type: "student",
    school: "가톨릭대학교",
  },
};
```

## 제네릭 클래스

```typescript
class List<T> {
  constructor(private list: T[]) {}

  push(data: T) {
    this.list.push(data);
  }

  pop() {
    return this.list.pop();
  }

  print() {
    console.log(this.list);
  }
}

const numberList = new List<number>([1, 2, 3]);
const stringList = new List<string>(["1", "2"]);
```

## 프로미스와 제네릭

```typescript
const promise = new Promise<number>((resolve, reject) => {
  setTimeout(() => {
    // 결과값 : 20
    resolve(20);
  }, 3000);
});

promise.then((response) => {
  // response는 number 타입
  console.log(response);
});

promise.catch((error) => {
  if (typeof error === "string") {
    console.log(error);
  }
});
```

```typescript
function fetchPost() {
  return new Promise<Post>((resolve, reject) => {
    setTimeout(() => {
      resolve({
        id: 1,
        title: "게시글 제목",
        content: "게시글 본문",
      });
    }, 3000);
  });
}

function fetchPost(): Promise<Post> {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve({
        id: 1,
        title: "게시글 제목",
        content: "게시글 본문",
      });
    }, 3000);
  });
}
```
