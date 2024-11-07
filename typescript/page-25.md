# 유틸리티 타입

실무에서 자주 사용되는 타입을 미리 만들어 둔 것

## 맵드 타입 기반

### Partial<T>

특정 객체 타입의 모든 프러퍼티를 선택적 프로퍼티로 바꿔주는 타입

```typescript
interface Post {
  title: string;
  tags: string[];
  content: string;
  thumbnailURL? string;
}


// 임시 저장된 게시글
const draft: Partial<Post> = {
  title : '초안 제목',
  content : '초안'
}

// Partial 타입 직접 구현
type Partial<T> = {
  [key in keyof T] ?: T[key]
};
```

### Required<T>

특정 객체 타입의 모든 프로퍼티를 필수 프로퍼티로 바꿔주는 타입

```typescript
const withThumbnailPost: Required<Post> = {
  title: "한입 타스 후기",
  tags: ["ts"],
  content: "",
  thumbnailUrl: "https://...",
};

// Required 타입 직접 구현
type Partial<T> = {
  [key in keyof T]-?: T[key];
};
```

> `-?`는 필드를 선택적(optional) 속성이 아닌 필수 속성으로 만든다. 즉, 원래 T 타입에 선택적 속성이 있다면, 이 타입에서는 선택성이 제거되어 필수 속성으로 변경된다.

### Readonly<T>

특정 객체 타입에서 모든 프로퍼티를 읽기 전용 프로퍼티로 만들어 주는 타입

```typescript
const readonlyPost: ReadonlyPost<Post> = {
  title: "보호된 게시글",
  tags: [],
  content: "",
};

// Readonly 직접 구현
type Readonly<T> = {
  readonly [key in keyof T]-?: T[key];
};
```

### Pick<T, K>

객체 타입으로부터 특정 프로퍼티만 골라내는 타입

```typescript
interface Post {
  title: string;
  tags: string[];
  content: string;
  thumbnailURL?: string;
}

const legacyPost: Pick<Post, "title" | "content"> = {
  title: "옛날 글",
  content: "옛날 컨텐츠",
};

// Pick 타입 직접 구현

type Pick<T, K extends keyof T> = {
  [key in K]: T[key];
};

// extends keyof T를 통해, T로 들어오는 객체의 속성만 들어올 수 있도록 제한
```

### Omit<T, K>

객체 타입으로 부터 특정 프로퍼티를 제거하는 타입

```typescript
interface Post {
  title: string;
  tags: string[];
  content: string;
  thumbnailURL?: string;
}

const noTitlePost: Omit<Post, "title"> = {
  content: "",
  tegs: [],
  thumbnailURL: "",
};

// Omit 타입 직접 구현
type Omit<T, K extends keyof T> = Pick<T, Exclude<key of T, K>>;
```

### Record<K, V>

객체 타입을 새롭게 정의할 때 인덱스 시그니처처럼 유연하지만, 조금 더 제한적인 객체타입을 정의

```typescript
type ThumbnailLegacy = {
  large: {
    url: string;
  };
  medium: {
    url: string;
  };
  small: {
    url: string;
  };
};

type Thumbnail = Record<"large" | "medium" | "small", { url: string }>;

// Record 타입 직접 구현
type Record<K extends keyof any, V> = {
  [key in K]: V;
};
```

## 조건부 타입 기반

### Exclude<T, U>

T에서 U를 제거하는 타입

```typescript
type A = Exclude<string | boolean, boolean>;

// Exclude 직접 구현
type Exclude<T, U> = T Extends U ? never : T;
```

### Extract<T, U>

T에서 U를 추출하는 타입

```typescript
type B = Extract<string | boolean, boolean>;

// Extract 직접 구현
type Extract<T, U> = T extends U ? T : never;
```

### ReturnType<T>

함수의 반환값 다입을 추출하는 타입

```typescript
function funcA() {
  return "hello";
}

type ReturnA = ReturnType<typeof funcA>;

// ReturnType 직접 구현
type ReturnType<T extends (...arg: any) => any> = T extends (
  ...arg: any
) => infer R
  ? R
  : never;
```
