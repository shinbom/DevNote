---
title: "[K번째 수](http://www.acmicpc.net/problem/10810)"
description: 
created: 2026-03-01
modified: 2026-03-02
tags: []
---

# [K번째 수](http://www.acmicpc.net/problem/10810)

## 문제

도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다. 또, 1번부터 N번까지 번호가 적혀있는 공을 매우 많이 가지고 있다. 가장 처음 바구니에는 공이 들어있지 않으며, 바구니에는 공을 1개만 넣을 수 있다.

도현이는 앞으로 M번 공을 넣으려고 한다. 도현이는 한 번 공을 넣을 때, 공을 넣을 바구니 범위를 정하고, 정한 바구니에 모두 같은 번호가 적혀있는 공을 넣는다. 만약, 바구니에 공이 이미 있는 경우에는 들어있는 공을 빼고, 새로 공을 넣는다. 공을 넣을 바구니는 연속되어 있어야 한다.

공을 어떻게 넣을지가 주어졌을 때, M번 공을 넣은 이후에 각 바구니에 어떤 공이 들어 있는지 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.

둘째 줄부터 M개의 줄에 걸쳐서 공을 넣는 방법이 주어진다. 각 방법은 세 정수 i j k로 이루어져 있으며, i번 바구니부터 j번 바구니까지에 k번 번호가 적혀져 있는 공을 넣는다는 뜻이다. 예를 들어, 2 5 6은 2번 바구니부터 5번 바구니까지에 6번 공을 넣는다는 뜻이다. (1 ≤ i ≤ j ≤ N, 1 ≤ k ≤ N)

도현이는 입력으로 주어진 순서대로 공을 넣는다.

## 출력

1번 바구니부터 N번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력한다. 공이 들어있지 않은 바구니는 0을 출력한다.

## 예제

### 예제 입력 1

```text
5 2
4 1 2 3 5
```

### 예제 출력 1

```text
2
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
const [exportNumbers, maximumBucket] = nm.split(" ").map(Number);
let result = [];
for(let i = 1; i < maximumBucket; i++) {
  const [startBucketNumber, endBucketNumber, insertBallNumber] = numbers[i].split(" ").map(Number);
  for(let j = startBucketNumber; j <= endBucketNumber; j++){
    result[j] = insertBallNumber;
  }
}

console.log(result.slice(1));

// 실패
```

## 문제 분석 및 해결 포인트

백준 10810번(공 넣기) 문제를 해결할 때 배열의 인덱스 처리와 반복문 범위 설정에서 헷갈리는 경우가 많습니다. 현재 코드에는 크게 3가지 수정 포인트가 있습니다.

### 1. 입력값 파싱 (N과 M의 위치)

문제에서 첫 줄의 **N**은 바구니의 개수, **M**은 공을 넣는 횟수입니다. 현재 코드에서는 `maximumBucket` 변수에 **M**이 할당되어 있는데, 반복문의 조건이나 배열 크기 설정에서 이 **N**과 **M**의 역할이 뒤바뀌어 있습니다.

### 2. 초기 배열 설정

`result` 배열을 빈 배열(`[]`)로 시작하면, 공이 한 번도 들어가지 않은 바구니는 `undefined`가 됩니다. 문제에서는 공이 없는 경우 **0**을 출력해야 하므로, 처음부터 **N** 크기만큼 **0**으로 채워진 배열을 만드는 것이 안전합니다.

### 3. 반복문 범위 (1-based vs 0-based)

바구니 번호는 1번부터 시작하지만, JavaScript 배열은 0번부터 시작합니다. `result[j] = insertBallNumber`를 할당할 때 인덱스를 맞추거나, 배열 크기를 **N+1**로 만들어야 합니다.

## Gemini 풀이

```javascript
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// 1. 첫 번째 줄에서 N(바구니 개수)과 M(공 넣는 횟수) 추출
const [NM, ...queries] = input;
const [n, m] = NM.split(' ').map(Number);

// 2. 0으로 채워진 바구니 배열 생성 (1번 바구니를 index 1에 맞추기 위해 n+1 크기)
let baskets = new Array(n + 1).fill(0);

// 3. M번의 쿼리를 순회하며 구조 분해 할당 적용
for (let i = 0; i < m; i++) {
    // 각 줄(queries[i])을 공백으로 나누고 바로 [i, j, k]로 분해
    const [start, end, ballNum] = queries[i].split(' ').map(Number);
    
    // 범위만큼 공 넣기 (교체)
    for (let j = start; j <= end; j++) {
        baskets[j] = ballNum;
    }
}

// 4. 1번 바구니부터 n번까지 slice 후 공백으로 합쳐서 출력
console.log(baskets.slice(1).join(' '));
```

## 코드 오류 분석

### 반복문의 범위 문제 (i=1 부터 시작)

```javascript
const [nm, ...numbers] = input;
```

위 코드를 실행하면 `numbers` 배열의 0번 인덱스부터 실제 데이터가 들어갑니다.

그런데 `for(let i = 1; i < maximumBucket; i++)`로 시작하면 첫 번째 공 넣기 시도(0번 인덱스)를 건너뛰게 됩니다. 또한 `i < maximumBucket` 조건은 마지막 데이터를 포함하지 못할 수도 있습니다 (**M**번의 시도라면 `i=0`부터 `i < m`까지 돌아야 함).

### result 배열의 초기화 부재

```javascript
let result = [];
```

이렇게 선언하고 `result[j]`에 값을 넣으면, 공이 들어가지 않은 바구니 자리는 `undefined`가 됩니다. 백준 출력 결과에는 **0**이 나와야 하므로 `new Array(n + 1).fill(0)`처럼 초기값을 채워주는 과정이 필요했습니다.

### 입력값 파싱 문제 (N과 M의 혼동)

```javascript
const [exportNumbers, maximumBucket] = nm.split(" ").map(Number);
```

여기서 `maximumBucket`은 사실 '바구니 개수(**N**)'가 아니라 '공을 넣는 횟수(**M**)'입니다. 변수 이름 때문에 나중에 반복문을 돌릴 때 헷갈리셨을 가능성이 커요.