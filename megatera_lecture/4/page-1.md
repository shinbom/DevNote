# Express

> Node.js FrameWork

```
키워드

- Express 란
- URL 구조
- REST API
- HTTP Method(CRUD)
```

[Express](https://expressjs.com/ko/)

프론트엔드 개발자이지만 백엔드 영역을 건들일이 많다.

> [Express 설치](https://expressjs.com/ko/starter/installing.html)

> [ts-node](https://github.com/TypeStrong/ts-node)

```bash
mkdir express-demo-app
cd mkdir express-demo-app

# .gitIgnore
touch .gitignore
echo "/node_modules/" > .gitignore

# Package Init
npm init -y

# TypeScript Inttall
npm i -D typescript
npx tsc --init


# ESLint Install
npm i -D eslint
npx eslint --init
#------------------------------#
how would you lie to use Eslint?
> To Check syntax, find problems, and enforce code style

What type of moduls your project use?
> JavaScript modules (import/export)

Which framework does your project use?
> None of these

Does your project use TypeScript?
> Yes

Where does your code run?
> Node

Which style guid do you want to follow?
> XO: https://github.com/xoojs/eslint-config-xo-typescript

What format do you want your config file to be in?
> JavaScript

Would you like to install them now?
> Yes

Which package manager do you want to use?
> npm

#------------------------------#

# Ts-node Install
npm i -D ts-node

# Express Install
npm i express
npm i @types/express
```

### ts-node

- Node.js에서 Typesciprt 를 실행 시키는 도구
- ts 파일을 미리 컴파일하지 않고 바로 실행 시키는 엔진
- JIT(Just In Time) 으로 Typescript를 Javascript로 변환하여 실행 가능

```typescript
import express from 'express';

const port = 3000;

const app = express();

app.get('/', (req, res) => {
    res.send('Hello, world!');
});

app.listen(port, () => {
    // 해당 포트에 접속 
    console.log(`Server running at http://localhost:${port}`);
});
```

```bash
npx ts-node app.ts


# 코드를 수정할 떄마다 서버를 재실행하지 안히도록 nodemon 실행
npm i -D nodemon
npx nodemon app.ts
```

```bash
# package.json

"scripts" : {
    "start" : "ts-node app.ts" #ts-node 실행
    "lint" : "eslint --fix" # eslint 자동 수정
}
```

## [Rest API](../3/page-2.md)

> Roy Fielding - “[Architectural Styles and the Design of Network-based Software Architectures](https://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm)” (2000)

> [Richardson Maturity Model](https://martinfowler.com/articles/richardsonMaturityModel.html)



> 대게 "필딩 제약조건" 4가지를 만족하지 않고, Resource와 Http Verb만 도입하는 수준으로 사용



CRUD에 대해 HTTP Method를 대입.
