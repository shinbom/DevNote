# [K번째 수](http://www.acmicpc.net/problem/11004)

## 문제

수 N개 A1, A2, ..., AN이 주어진다. A를 오름차순 정렬했을 때, 앞에서부터 K번째 있는 수를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 N(1 ≤ N ≤ 5,000,000)과 K (1 ≤ K ≤ N)이 주어진다.
둘째에는 A1, A2, ..., AN이 주어진다. (-109 ≤ Ai ≤ 109)

## 출력

A를 정렬했을 때, 앞에서부터 K번째 있는 수를 출력한다.

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
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().trim().split('\n');

function solution(data) {
  const [count, k] = data[0].split(' ')
  const numbers = data[1].split(' ').map(Number).sort((a, b) => a-b)
  console.log(numbers[k - 1])
}

solution(input);
```

## 강사님 풀이

```javascript
// 시간복잡도 O(NlogN)인 정렬 알고리즘을 사용해야 합니다.
// O(N^2)인 선택 정렬은 시간초과가 발생할 수 있습니다.

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
let [n, k] = input[0].split(' ').map(Number);
let arr = input[1].split(' ').map(Number);
arr.sort((a, b) => a - b);
console.log(arr[k - 1]);
```