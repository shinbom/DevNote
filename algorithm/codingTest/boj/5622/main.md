# [K번째 수](http://www.acmicpc.net/problem/11004)

## 문제

상근이의 할머니는 아래 그림과 같이 오래된 다이얼 전화기를 사용한다.

![dial](./dial.png)

전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다. 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.

숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.

상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.

할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어의 길이는 2보다 크거나 같고, 15보다 작거나 같다.

## 출력

첫째 줄에 다이얼을 걸기 위해서 필요한 최소 시간을 출력한다.

## 예제

### 예제 입력 1

```text
WA
```

### 예제 출력 1

```text
13
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
const dial = {
  A : 2,
  B : 2,
  C : 2,
  D : 3,
  E : 3,
  F : 3,
  G : 4,
  H : 4,
  I : 4,
  J : 5,
  K : 5,
  L: 5,
  M : 6, 
  N : 6,
  O : 6,
  P : 7,
  Q : 7,
  R : 7,
  S : 7,
  T : 8,
  U : 8,
  V : 8,
  W : 9,
  X : 9,
  Y : 9,
  Z : 9
}

let sum = 0;

// 번호 1을 할때 최초 2초가 소요됨.
// 1보다 큰 숫자를 걸리는 시간은 1초씩 더 걸림.
// 즉, 2번인 경우 3초가 걸림.
// 2 + 1 = 3 > 즉, (번호 + 1)

for(let i = 0; i < input.length; i++) {
  const word = input[i]
  sum += (dial[word] + 1);
}
console.log(sum);

```
