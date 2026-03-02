---
title: "[세수 정렬](http://www.acmicpc.net/problem/2750)"
description: 
created: 2026-02-28
modified: 2026-03-02
tags: []
---

# [세수 정렬](http://www.acmicpc.net/problem/2750)

## 문제

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

## 입력

첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

## 출력

첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

## 예제

### 예제 입력 1

```text
5
5
2
3
4
1
```

### 예제 출력 1

```text
1
2
3
4
5
```

## 내 풀이

```javascript
let fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().trim().split('\n').map(Number);
input.sort((a, b) => a - b);
const map = new Set(input);
let answer = '';
for(let i of map){
    answer += i + '\n';
}
console.log(answer);

// 오답
```

## 강사님 풀이

```javascript
let fs = require('fs');
const filePath = fs.readFileSync("/dev/stdin").toString().split(" ")
let n = Number(input[0]);
for (let i = 1; i <= n; i++) {
  arr.push(Number(input[i]));
}
arr.sort((a, b) => a - b);

let answer = ''
for (let i = 0; i < arr.length; i++) {
  answer += arr[i] + '\n';
}
console.log(answer);

```

## 강사님 풀이 2

```javascript
// 선택 정렬 사용
function selectionSort(arr) {
  for(let i = 0; i < arr.length; i++) {
    let minIndex = i;
    for (let j = i +1; j < arr.length; j++) {
      if(arr[imIndex] > arr[j]) minIndex = j
    }
    let temp = arr[i]
    arr[i] = arr[minIndex]
    arr[minIndex] = temp
  }
}

let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let n = Number(input[0]);
let arr = [];
for (let i = i; i <= n; i++) {
  arr.push(Number(input[i]));
}
selectionSort(arr);
let answer = '';
for (let i = 0; i < arr.length; i++) {
  answer += arr[i] + '\n';
}
console.log(answer);
```

### 틀린 이유

`첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다.`

- 첫째 줄 - 수의 개수
- 둘째 줄 - 수

이렇게 되므로 

```javascript
// input[0] = 수의 개수
// input[1] = 수
```
이런식으로 정해서 풀어야 했다. 즉,

```javascript
let fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n').trim().map(Number);
// 위처럼 하면, 런타임 에러가 자꾸 난다.

let numbers = input.slice(1);
numbers.sort((a, b) => a - b);
let answer = '';
for(let i of numbers){
    answer += i + '\n';
}
console.log(answer);
```
숫자가 554321 이렇게 들어오면 첫번째 인덱스를 자르거나

```javascript
let numbers = input.slice(1);
```

input[0]을 제외하고 숫자를 배열로 처리한 후, 정렬을 해야 한다.

그리고 초기에 `trim()`의 순서에 의해서 런타임 오류, 그리고 `오답`처리가 됐다.
  
```javascript
let input = fs.readFileSync(filePath).toString().trim().split('\n').map(Number);
```

**📝 `trim()`을 먼저 사용해야 하는 이유**

입력 문자열의 끝에 줄바꿈 문자가 있으면 `split('\n')` 후 배열에 빈 문자열(`''`)이 생깁니다. 이 빈 문자열은 숫자로 변환 시 `0`이 되어 정렬 결과에 영향을 줄 수 있습니다. `trim()`은 이런 끝부분의 공백이나 줄바꿈을 미리 제거하여, 의도치 않은 빈 문자열이 배열에 포함되는 것을 막아줍니다.

- **잘못된 순서**: `split()` → `trim()` = `['5', '2', ..., '8', '']` (오류 발생 가능)
- **올바른 순서**: `trim()` → `split()` = `['5', '2', ..., '8']` (안전)


