---
title: "[K번째 수](http://www.acmicpc.net/problem/11654)"
description: 
created: 2026-03-01
modified: 2026-03-02
tags: []
---

# [K번째 수](http://www.acmicpc.net/problem/11654)

## 문제

알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.

## 입력

알파벳 소문자, 대문자, 숫자 0-9 중 하나가 첫째 줄에 주어진다.

## 출력

주어진 글자의 아스키 코드값을 출력한다.

## 예제

### 예제 입력 1

```text
A
```

### 예제 출력 1

```text
65
```

---

## 내 풀이

```javascript
let fs = require('fs');
let path = require('path');

const filePath = process.platform === 'linux'
    ? '/dev/stdin'
    : path.resolve(__dirname, 'input.txt');

const splitCode = process.platform ==='linux' ? '\n' : '\r\n';

let input = fs.readFileSync(filePath).toString().trim()
console.log(input.charCodeAt())
```

`charCodeAt`이라는 문법을 몰라서 헤맷다.
복습하자
