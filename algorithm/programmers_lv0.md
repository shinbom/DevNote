# 문제 풀이

## 콜라츠 수열

> 모든 자연수 x에 대해서 현재 값이 x이면 x가 짝수일 때는 2로 나누고, x가 홀수일 때는 3 * x + 1로 바꾸는 계산을 계속해서 반복하면 언젠가는 반드시 x가 1이 되는지 묻는 문제를 콜라츠 문제라고 부릅니다.
<br/>그리고 위 과정에서 거쳐간 모든 수를 기록한 수열을 콜라츠 수열이라고 부릅니다.
<br/>계산 결과 1,000 보다 작거나 같은 수에 대해서는 전부 언젠가 1에 도달한다는 것이 알려져 있습니다.
<br/>임의의 1,000 보다 작거나 같은 양의 정수 n이 주어질 때 초기값이 n인 콜라츠 수열을 return 하는 solution 함수를 완성해 주세요.

```javascript
// 내 풀이
function solution(n) {
    let number = n
    let answer = [number];
    while(number > 1){
        number % 2 > 0 ?  number = 3 * number + 1 : number = number / 2
        answer.push(number)
    }
    return answer;
}
```

```javascript
// 좋은 풀이
// 재귀함수를 이용
function solution(n, arr = []) {
    arr.push(n)
    if (n === 1) return arr
    if (n % 2 === 0) return solution(n / 2, arr)
    return solution(3 * n + 1, arr)
}
```

## 최댓값 만들기 (2)

> 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.


|numbers|result|
|---|---|
|[1,2,-3,4,5]|15|
|[0,-31,24,10,1,9]|240|
|[10,20,30,5,5,20,5]|600|


```javascript
// 1차 시도(실패)
function solution(numbers) {
  const sortNumbers = numbers.sort((a, b) => b - a)
  return sortNumbers[0] * sortNumbers[1];
}
```

```javascript
// 제출 답안

function solution(numbers) {
    const sortNumbers = numbers.sort((a, b) => b - a)
    const maxNumber = sortNumbers[0] * sortNumbers[1];
    const maxNumber2 = sortNumbers[sortNumbers.length - 1] * sortNumbers[sortNumbers.length - 2]
    return Math.max(maxNumber, maxNumber2)
}
```

1차 시도는 문제만 보고 간단하게 생각하여 `정렬 후` 최대값들만 출력되도록 하였다.<br/>
그런데 문제를 보면 `음수끼리 곱하였을때에도 최댓값`이 나올 수 있다.
이에따라 정렬한 상태에서 음수끼리도 곱한 값들을 받을 수 있도록 변수를 나누어 주었다.

> 문제를 꼼꼼히 보고, 입출력 예도 더 꼼꼼히 보자.

## 간단한 식 계산하기

문자열 binomial이 매개변수로 주어집니다. binomial은 "a op b" 형태의 이항식이고 a와 b는 음이 아닌 정수, op는 '+', '-', '*' 중 하나입니다. 주어진 식을 계산한 정수를 return 하는 solution 함수를 작성해 주세요.

|binomial|result|
|---|---|
|"43 + 12"|55|
|"0 - 7777"|-7777|
|"40000 * 40000"|1600000000|

```javascript
// 나의 풀이
function solution(binomial) {
    let answer = 0
    const arr = binomial.split(' ')
    if(arr[1] === '+') {
        return Number(arr[0]) + Number(arr[2])
    }
    
    if(arr[1] === '-') {
        return Number(arr[0]) - Number(arr[2])
    }
    
    if(arr[1] === '*') {
        return Number(arr[0]) * Number(arr[2])
    }
}
```

```javascript

// 좋은 풀이
const ops = {
  '+': (a, b) => a + b,
  '-': (a, b) => a - b,
  '*': (a, b) => a * b,
};

function solution(binomial) {
  const [a, op, b] = binomial.split(' ');
  return ops[op](+a, +b);
}
```

## 369게임

> 머쓱이는 친구들과 369게임을 하고 있습니다. 369게임은 1부터 숫자를 하나씩 대며 3, 6, 9가 들어가는 숫자는 숫자 대신 3, 6, 9의 개수만큼 박수를 치는 게임입니다. 머쓱이가 말해야하는 숫자 order가 매개변수로 주어질 때, 머쓱이가 쳐야할 박수 횟수를 return 하도록 solution 함수를 완성해보세요.

|order|result|
|---|---|
|3|1|
|29423|2|

```javascript
// 1차 시도(실패)
function solution(order) {
    return String(order).match(/[3|6|9]/g).length
}
```

런타임 에러가 발생하였다. 어떤부분을 놓친것인지 고민이 필요하다.

### GPT 확인 결과

> 런타임 에러가 발생하는 이유는 match 메서드가 null을 반환할 수 있기 때문입니다. 만약 order에 3, 6, 9가 하나도 포함되지 않은 경우, match는 null을 반환하고, null에 대해 length를 호출하면 런타임 에러가 발생하게 됩니다.


```javascript
// 제출 답안
function solution(order) {
    return (String(order).match(/[3|6|9]/g) || []).length;
}
```

> match는 null이 나올 수 있음에 따라, 빈배열도 반환되도록 처리