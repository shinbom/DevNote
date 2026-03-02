---
title: [수 정렬하기 2](http://www.acmicpc.net/problem/2751)
description: 
created: 2026-02-28
modified: 2026-03-02
tags: []
---

# [수 정렬하기 2](http://www.acmicpc.net/problem/2751)

## 문제

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

## 입력

첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

## 출력

첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

## 예제

### 예제 입력 1

```text
5
5
4
3
2
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

---

## 내 풀이

```javascript
let fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

function solution(data) {
  let numbers = [];
  for (let i = 1; i <= input.length; i++) {
    numbers.push(Number(input[i]));
  }

  numbers.sort((a, b) => a - b);
  let answer = '';

  for(let i = 0; i < numbers.length; i++) {
    answer += numbers[i] + '\n';
  }

  console.log(answer);
}

solution(input);

// 오답
/*
0
8
NaN
*/
```

### Nan이 나오는 이유

```javascript
  for (let i = 1; i <= input.length; i++) {
    numbers.push(Number(input[i]));
  }
```

```javascript
let fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

function solution(data) {
  let numbers = [];
  for (let i = 1; i <= input.length; i++) {
    numbers.push(Number(input[i]));
  }

  numbers.sort((a, b) => a - b);
  let answer = '';

  for(let i = 0; i < numbers.length; i++) {
    answer += numbers[i] + '\n';
  }

  console.log(answer);
}

solution(input);
```

## 강사님 풀이

```javascript
// 데이터의 갯수가 1,000,000이므로, 시간복잡도 O(NlogN)인 정렬 알고리즘을 사용해야 합니다.
// O(N^2)인 선택 정렬은 시간초과가 발생할 수 있습니다.

let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let n = Number(input[0]);
let arr = [];
for (let i = 1; i <= n; i++) {
  arr.push(Number(input[i]));
}

arr.sort((a, b) => a - b);
let answer = '';
for (let i = 0; i < arr.length; i++) {
  answer += arr[i] + '\n';
}
console.log(answer);
```
