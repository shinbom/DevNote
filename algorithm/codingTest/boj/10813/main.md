---
title: [K번째 수](http://www.acmicpc.net/problem/10813)
description: 
created: 2026-03-01
modified: 2026-03-02
tags: []
---

# [K번째 수](http://www.acmicpc.net/problem/10813)

## 문제

도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다. 바구니에는 공이 1개씩 들어있고, 처음에는 바구니에 적혀있는 번호와 같은 번호가 적힌 공이 들어있다.

도현이는 앞으로 M번 공을 바꾸려고 한다. 도현이는 공을 바꿀 바구니 2개를 선택하고, 두 바구니에 들어있는 공을 서로 교환한다.

공을 어떻게 바꿀지가 주어졌을 때, M번 공을 바꾼 이후에 각 바구니에 어떤 공이 들어있는지 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.

둘째 줄부터 M개의 줄에 걸쳐서 공을 교환할 방법이 주어진다. 각 방법은 두 정수 i j로 이루어져 있으며, i번 바구니와 j번 바구니에 들어있는 공을 교환한다는 뜻이다. (1 ≤ i ≤ j ≤ N)

도현이는 입력으로 주어진 순서대로 공을 교환한다.

## 출력

1번 바구니부터 N번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력한다.

## 예제

### 예제 입력 1

```text
5 4
1 2
3 4
1 4
2 2
```

### 예제 출력 1

```text
3 1 4 2 5
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

let input = fs.readFileSync(filePath).toString().trim().split(splitCode);
const [nm , ...numbers] = input;
const [n, m] = nm.split(" ").map(Number);
let result = []
for(let i = 1; i <= n; i++) {
  result[i] = i;
}

let originalData = {
  from :0,
  to : 0
}

for(let i = 0; i < m; i++) {
  const [fromIndex, toIndex] = numbers[i].split(" ").map(Number);
  originalData.from = result[fromIndex]
  originalData.to = result[toIndex]
  result[fromIndex] = originalData.to;
  result[toIndex] = originalData.from;
}

console.log(result.slice(1).join(' '));
```

## Gemini 풀이

```javascript
const fs = require('fs');
const path = require('path');

// 환경에 따른 입력 경로 설정
const filePath = process.platform === 'linux'
    ? '/dev/stdin'
    : path.resolve(__dirname, 'input.txt');

// 입력값 처리 (줄바꿈 문자에 유연하게 대응)
const input = fs.readFileSync(filePath).toString().trim().split(/\s+/);

// 첫 번째 값은 N, 두 번째 값은 M, 나머지는 숫자 배열로 분리
const n = parseInt(input[0]);
const m = parseInt(input[1]);
const queries = input.slice(2);

// 1. 1부터 N까지의 배열 생성 (0번 인덱스는 사용하지 않음으로써 문제의 번호와 일치시킴)
let result = Array.from({ length: n + 1 }, (_, i) => i);

// 2. M번만큼 반복하며 값 교체 (Swap)
for (let i = 0; i < m; i++) {
    const fromIndex = parseInt(queries[i * 2]);
    const toIndex = parseInt(queries[i * 2 + 1]);

    // 구조 분해 할당을 사용하여 임시 변수 없이 바로 교환
    [result[fromIndex], result[toIndex]] = [result[toIndex], result[fromIndex]];
}

// 3. 1번 인덱스부터 끝까지 공백으로 구분하여 출력
console.log(result.slice(1).join(' '));
```
