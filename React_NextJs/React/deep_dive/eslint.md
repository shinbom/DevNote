# ![ESLint](https://eslint.org/)

자바스크립의 코드를 정적 분석해 잠재적인 문제를 발견하고 나아가 수정까지 도와주는 도구

## 분석방법

1. 자바스크립트 코드를 문잗열로 읽음
2. 자바스크립트 코드를 분석할 수 있는 파서(parser)로 코드를 구조화
3. 2번에서 구조화한 트리를 AST(Abstract Syntax Tree)를 기준으로 각종 규칙과 대조
4. 규칙과 대조했을 때 이를 위반한 코드를 알리거나 수정

### AST

코드를 트리 구조로 표현한 데이터 구조로, 프로그래밍 언어의 구문을 구조화된 방식으로 분석하고 조작할 수 있게 해줌

![AST Explorer](https://astexplorer.net/)

```javascript
function hello(str) {}
```

```json
{
  "type": "Program",
  "start": 0,
  "end": 22,
  "body": [
    {
      "type": "FunctionDeclaration",
      "start": 0,
      "end": 22,
      "id": {
        "type": "Identifier",
        "start": 9,
        "end": 14,
        "name": "hello"
      },
      "expression": false,
      "generator": false,
      "async": false,
      "params": [
        {
          "type": "Identifier",
          "start": 15,
          "end": 18,
          "name": "str"
        }
      ],
      "body": {
        "type": "BlockStatement",
        "start": 20,
        "end": 22,
        "body": []
      }
    }
  ],
  "sourceType": "module"
}
```


## 설치

```bash
npm install -D eslint # npm
yarn add -D eslint # yarn
```

## .eslintrc.js

```javascript
module.exports = {
  parser: '@typescript-eslint/parser',
  parserOptions: {
    project: 'tsconfig.json',
    tsconfigRootDir: __dirname,
    sourceType: 'module',
  },
  plugins: [],
  extends: [],
  root: true,
  env: {
    node: true,
    jest: true,
  },
  ignorePatterns: [],
  rules: {},
};
```

## 옵션

- parser 
    - 각 코드 파일을 검사할 parser를 설정 
    
- parserOptions 
    - parser의 추가 정보를 등록

- extends 
    - eslint role 설정이 되어있는 외부 file을 extends 하는 부분

- rules 
    - lint rule을 적용하는 부분
    - extends로 자동 설정된 rules를 끄거나, error를 warning으로 변경하는 등 설정을 바꿀 수 있음

- ignorePatters
    - 린트하고 싶지 않은 디렉토리를 설정

---

## 새로운 ESLint 규칙 만들기

작성한 코드를 기반으로 트리 국조의 데이터 스트럭쳐를 만든 후, 지적하고 싶은 코드를 만들어서 룰로 저장

> 파일명은 `eslint-plugin-`로 시작되어야 한다.

### new Date()를 막는 ESLint 규칙 만들기

```javascript
new Date()
```

```json
{
  "type": "Program",
  "start": 0,
  "end": 10,
  "body": [
    {
      "type": "ExpressionStatement",
      "start": 0,
      "end": 10,
      "expression": {
        "type": "NewExpression",
        "start": 0,
        "end": 10,
        "callee": {
          "type": "Identifier",
          "start": 4,
          "end": 8,
          "name": "Date"
        },
        "arguments": []
      }
    }
  ],
  "sourceType": "module"
}
```

```javascript
// AST를 기반으로 만든 ESLint 규칙
module.exports = {
    meta : {
        type : 'suggestion',
        docs : {
            description : 'disallow use of the new Date()',
            recommended : false
        },
        fixable : 'code',
        schma : [],
        messages : {
            message : 'new Date()는 클라이언트에서 실행 시 해당 기기의 시간에 의존적이므로, 정확하지 않습니다. 현재 시간이 필요하다면 serverDate()를 사용해 주세요.'
        }
    },
    create : function (context) {
        return {
            NewExpression : function (node) {
                if (node.callee.name === 'Date' && node.arguments.length ===0) {
                    context.report({
                        node : node,
                        messageId : 'message',
                        fix : function (fixer)a {
                            return fixer.replaceText(node, 'serverDate()')
                        }
                    })
                }
            }
        }
    }
}
```

> 규칙은 반드시 eslint-plugin 형태로 묶음 배포하는 것만 가능함<br/>
> yo와 generate-eslint를 활용해 eslint-plugin을 구성할 환경을 빠르게 구성

```bash
yo eslint:plugin
...

yo eslint:rule
```

환경설정이 완료되면 다음과 같은 구조로 디렉터리와 파일이 생성됨

📂eslint-plugin-
 ┣ 📂docs
 ┃ ┗ 📂rules
 ┃ ┃ ┗ 📜no-new-date.md
 ┣ 📂lib
 ┃ ┣ 📂rules
 ┃ ┃ ┗ 📜no-new-date.js
 ┃ ┗ 📜index.js
 ┣ 📂tests
 ┃ ┗ 📂rules
 ┃ ┃ ┗ 📜no-new-date.js
 ┣ 📜.eslintrc.js
 ┣ 📜.npmrc
 ┣ 📜README.md
 ┣ 📜package-lock.json
 ┗ 📜package.json

rules/no-new-date.js 파일에 작성한 규칙을 붙여넣은 후, docs에는 해당 규칙을 위한 설명을, tests에는 테스트 코드를 작성

```javascript
/**
 * @fileoverview 
 * @author 
 */

'use strict';

// -------------------------------------------------------------------------
// Requirements
// -------------------------------------------------------------------------

const rule = require('../../../lib/rules/no-new-date'),
  RuleTester = requert('eslint').RuleTester;

// -----------------------------------------------------------------------------------------------
// Tests
// -----------------------------------------------------------------------------------------------

const ruleTester = new RuleTester();
ruleTester.run('no-new-date', rule, {
  valid: [
    {
      code: 'new Date(2021, 1, 1)',
    },
    {
      code: 'new Date("2022-01-01")',
    },
  ],

  invalid: [
    {
      code: 'new Date()',
      errors: [{ message: rule.meta.message.message }],
      output: 'ServerDate()',
    },
  ],
});
```

마지막으로 `npm publish`로 배포한 후, 프로젝트에서 설치하여 사용한다.
