---
title: "[K번째 수](http://www.acmicpc.net/problem/11004)"
description: 
created: 2026-02-28
modified: 2026-03-02
tags: []
---

# [K번째 수](http://www.acmicpc.net/problem/11004)

## 문제

본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다. 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.

C++을 사용하고 있고 cin/cout을 사용하고자 한다면, cin.tie(NULL)과 sync_with_stdio(false)를 둘 다 적용해 주고, endl 대신 개행문자(\n)를 쓰자. 단, 이렇게 하면 더 이상 scanf/printf/puts/getchar/putchar 등 C의 입출력 방식을 사용하면 안 된다.

Java를 사용하고 있다면, Scanner와 System.out.println 대신 BufferedReader와 BufferedWriter를 사용할 수 있다. BufferedWriter.flush는 맨 마지막에 한 번만 하면 된다.

Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다. 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.

또한 입력과 출력 스트림은 별개이므로, 테스트케이스를 전부 입력받아서 저장한 뒤 전부 출력할 필요는 없다. 테스트케이스를 하나 받은 뒤 하나 출력해도 된다.

자세한 설명 및 다른 언어의 경우는 이 글에 설명되어 있다.

이 블로그 글에서 BOJ의 기타 여러 가지 팁을 볼 수 있다.

## 입력

첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.

## 출력

각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.

## 예제

### 예제 입력 1

```text
5
1 1
12 34
5 500
40 60
1000 1000
```

### 예제 출력 1

```text
2
46
505
100
2000
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

const [ answerCount, ...number] = input;
for(let i = 0; i < answerCount; i++) {
    const [a, b] = number[i].split(' ').map(Number);
    console.log(a + b);
}

// 시간초과
```

## gemini 풀이

```javascript
const fs = require('fs');
const path = require('path');

const filePath = process.platform === 'linux'
    ? '/dev/stdin'
    : path.resolve(__dirname, 'input.txt');

const input = fs.readFileSync(filePath).toString().trim().split(/\r?\n/);

const answerCount = Number(input[0]);
let result = ''; // 출력할 결과를 담을 변수

for (let i = 1; i <= answerCount; i++) {
    const numbers = input[i].split(' ');
    const a = parseInt(numbers[0]);
    const b = parseInt(numbers[1]);
    result += (a + b) + '\n';
}

process.stdout.write(result);
```

1. console.log의 오버헤드
console.log는 단순히 값을 출력하는 기능만 있는 것이 아니라, 내부적으로 다음과 같은 추가 작업을 수행합니다.

포맷팅: 전달된 인자를 문자열로 변환하고, %d, %s 같은 포맷 지정자가 있는지 확인합니다.

줄바꿈 자동 추가: 매 호출마다 문자열 끝에 \n을 붙입니다.

동기적 특성: 환경에 따라 (특히 터미널 출력 시) 동기적으로 동작하여 다음 코드 실행을 차단할 수 있습니다.

2. process.stdout.write의 단순함
반면 process.stdout.write는 저수준(Low-level) 스트림 메서드입니다.

데이터 전달 전용: 추가적인 포맷팅이나 처리를 하지 않고, 받은 데이터를 그대로 표준 출력 버퍼로 보냅니다.

줄바꿈 없음: 사용자가 직접 문자열 끝에 \n을 붙여줘야 하지만, 그만큼 불필요한 연산이 빠집니다.

🚀 왜 더 빠르게 느껴질까? (핵심 원리)
알고리즘 문제에서 "시간 초과"가 발생하는 결정적인 이유는 출력 횟수 자체에 있습니다.

System Call 감소: console.log를 1만 번 호출하면 운영체제에 "화면에 그려줘"라는 요청(System Call)을 1만 번 보냅니다. 이는 매우 비싼 작업입니다.

버퍼링 활용: 반면, 전체 결과를 하나의 큰 문자열(result)로 합친 뒤 process.stdout.write(result)를 단 한 번 호출하면, 운영체제와의 통신이 1회로 줄어들어 실행 시간이 드라마틱하게 단축됩니다.