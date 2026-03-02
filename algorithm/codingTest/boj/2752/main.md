---
title: [세수 정렬](http://www.acmicpc.net/problem/2752)
description: 
created: 2026-02-28
modified: 2026-03-02
tags: []
---

# [세수 정렬](http://www.acmicpc.net/problem/2752)

## 문제

동규는 세수를 하다가 정렬이 하고 싶어졌다.
정수 세 개를 생각한 뒤에, 이를 오름차순으로 정렬하고 싶어졌다.
정수 세 개가 주어졌을 때, 가장 작은 수, 그 다음 수, 가장 큰 수를 출력하는 프로그램을 작성하시오.

## 입력

정수 세 개가 주어진다. 이 수는 1보다 크거나 같고, 1,000,000보다 작거나 같다. 이 수는 모두 다르다.

## 출력

제일 작은 수, 그 다음 수, 제일 큰 수를 차례대로 출력한다.

## 예제

### 예제 입력 1

```text
3 1 2
```

### 예제 출력 1

```text
1 2 3
```

---

## 내 풀이

```javascript
let fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().trim().split(' ').map(Number);
console.log(input.sort((a, b) => a - b).join(' '))
```

## 강사님 풀이

```javascript
let fs = require('fs');
const input = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let arr = input[0].split(' ').map(Number);
arr.sort(function (a, b) {
  return a - b;
});

let answer = ''
for (let i = 0; i < arr.length; i++) {
  answer += arr[i] + ' ';
}
console.log(answer);
```

## 강사님 풀이 2

```javascript
// 선택 정렬 사용
function selectionSort(arr) {
  for (let i = 0; i < arr.length - 1; i++) {
    let minIndex = i;
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[j] < arr[minIndex]) {
        minIndex = j;
      }
      let temp = arr[i]
      arr[i] = arr[minIndex]
      arr[minIndex] = temp
    }
  }
}

let fs = require('fs');
const input = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let arr = input[0].split(' ').map(Number);
selectionSort(arr);

let answer = ''
for (let i = 0; i < arr.length; i++) {
  answer += arr[i] + ' ';
}
console.log(answer);
```