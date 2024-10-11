# 서로소 유니온 타입

교집합이 없는 타입들을 모아 만든 유니온 타입

```typescript
type Admin = {
  tag: "ADMIN";
  name: string;
  kickCount: number;
};

type Member = {
  tag: "MEMBER";
  name: string;
  point: number;
};

type Guest = {
  tag: "GUEST";
  name: string;
  visitCount: number;
};
```

> tag를 이용하여, 타입가드

- if문 이용

```typescript
function login(user: User) {
  if (user.tag === "ADMIN") {
    console.log(`${user.name}님 현재까지 ${user.kickCount}명 추방했습니다`);
  } else if (user.tag === "MEMBER") {
    console.log(`${user.name}님 현재까지 ${user.point}모았습니다`);
  } else {
    console.log(`${user.name}님 현재까지 ${user.visitCount}번 오셨습니다`);
  }
}
```

- switch문 이용

```typescript
function login(user: User) {
  switch (user.tag) {
    case "ADMIN": {
      console.log(`${user.name}님 현재까지 ${user.kickCount}명 추방했습니다`);
      break;
    }
    case "MEMBER": {
      console.log(`${user.name}님 현재까지 ${user.point}모았습니다`);
      break;
    }
    case "GUEST": {
      console.log(`${user.name}님 현재까지 ${user.visitCount}번 오셨습니다`);
      break;
    }
  }
}
```

```typescript
// AS-IS(타입이 좁혀지지 않음)
type AsyncTask = {
  state : 'LOADING' | 'FAILED' | 'SUCCESS'
  error ?: {
    message : string
  }
  esponse?: {
    data: string;
  };
}


// 서로소 유니온 타입으로 변환
// 타입을 나눈 후, 유니온 타입으로 변환
type LoadingTask = {
  state : 'LOADING'
}

type FailedTask = {
  state : 'FAILED',
  error: {
    message : string
  }
}

type SuccessTask = {
  state: 'SUCCESS',
  response: {
    data: string;
  };
};

type AsyncTask = LoadingTask | FailedTask | SuccessTask

const processResult(task : AsyncTask){
  swtich(task.status) {
    case 'LOADING' : {
      console.log('로딩 중')
      break;
    }
    case 'FAILED' : {
      console.log('에러 발생')
      console.log( task.error.message )
      break;
    }
    case 'SUCCESS' : {
      console.log('성공 발생')
      console.log( task.error.message )
      break;
    }

  }
}

const loading: AsyncTask = {
  state: "LOADING",
};

const failed: AsyncTask = {
  state: "FAILED",
  error: {
    message: "error message",
  },
};

const success: AsyncTask = {
  state: "SUCCESS",
  response: {
    data: "success message",
  },
};
```
