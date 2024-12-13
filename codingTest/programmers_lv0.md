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

---

## 인덱스 바꾸기

문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때, my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.

|my_string	|num1	|num2	|result|
|-----------|-------|-------|------|
| "hello"   |	1	|  2	|"hlelo"|
|"I love you"|3    |	6  |"I l veoyou"|

### 고민

1. my_string의 num1 인덱스의 문자를 미리 변수에 할당한다.
2. my_string의 num2 인덱스의 문자를 미리 변수에 할당한다.
3. my_string의 num1와 num2의 인덱스에 for문을 돌면서 체크하면 될 것으로 생각했었다.
4. for문을 이용해야 하나 고민하고 있었다. 하지만 for문의 경우 return을 해도 올바르게 되지 않았다.

> 문자를 그대로 사용하여 for문을 도려고 하는게 문제였던 것 같다.

### 답안

```javascript
function solution(my_string, num1, num2) {
    my_string = my_string.split('');
    [my_string[num1], my_string[num2]] = [my_string[num2], my_string[num1]];
    return my_string.join('');
}
```

---

## 수 조작하기 2

정수 배열 numLog가 주어집니다. 처음에 numLog[0]에서 부터 시작해 "w", "a", "s", "d"로 이루어진 문자열을 입력으로 받아 순서대로 다음과 같은 조작을 했다고 합시다.

"w" : 수에 1을 더한다.
"s" : 수에 1을 뺀다.
"d" : 수에 10을 더한다.
"a" : 수에 10을 뺀다.
그리고 매번 조작을 할 때마다 결괏값을 기록한 정수 배열이 numLog입니다. 즉, numLog[i]는 numLog[0]로부터 총 i번의 조작을 가한 결과가 저장되어 있습니다.

주어진 정수 배열 numLog에 대해 조작을 위해 입력받은 문자열을 return 하는 solution 함수를 완성해 주세요.

|numLog	| result |
|---|---|
|[0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]	| "wsdawsdassw"|


```javascript
// 나의 풀이
function solution(numLog) {
    let answer = [];

    for(let i = 0; i < numLog.length; i++){
        const currentNumber = numLog[i]
        const nextNumber = numLog[i + 1]
        const result = nextNumber - currentNumber
        if(isNaN(result)) break

        if(result === 1) {
            answer.push('w')
        }
        if(result === -1) {
            answer.push('s')
        }
        if(result === 10) {
            answer.push('d')
        }
        if(result === -10) {
            answer.push('a')
        }
    }
    return answer.join('')
}
```

```javascript
// 더 좋은 풀이 
function solution(numLog) {
    const convert = {
        '1': 'w', '-1': 's', '10': 'd', '-10': 'a'
    };

    return numLog.slice(1).map((v, i) => {
        return convert[v - numLog[i]]
    }).join('')
}
```

---

## 특별한 이차원 배열 

n × n 크기의 이차원 배열 arr이 매개변수로 주어질 때, arr이 다음을 만족하면 1을 아니라면 0을 return 하는 solution 함수를 작성해 주세요.

0 ≤ i, j < n인 정수 i, j에 대하여 arr[i][j] = arr[j][i]

| arr	| result |
|---|---|
|[[5, 192, 33], [192, 72, 95], [33, 95, 999]]|	1|
|[[19, 498, 258, 587], [63, 93, 7, 754], [258, 7, 1000, 723], [587, 754, 723, 81]]|	0|

```javascript
// 내 풀이
function solution(arr) {
    let answer = []
    // N^2
    for(let i = 0; i < arr.length; i++){
        for(let j = 0; j < arr.length; j++){
            answer.push(arr[i][j] === arr[j][i])
        }
    }
    return Number(answer.every((x) => x))
}
```

```javascript
// 더 좋은 풀이
function solution(arr) {
    return arr.every((r, i) => r.every((_, j) => arr[i][j] === arr[j][i])) ? 1 : 0;
}
```

 > 나는 불필요한 every, Number를 사용했다.

---
머쓱이네 피자가게는 피자를 여섯 조각으로 잘라 줍니다. 피자를 나눠먹을 사람의 수 n이 매개변수로 주어질 때, n명이 주문한 피자를 남기지 않고 모두 같은 수의 피자 조각을 먹어야 한다면 최소 몇 판을 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.

|n	|result|
|--|--|
|6	|1|
|10| 5|
|4	|2|


```javascript
// 나의 풀이
function solution(members) {
    let answer = 1;
    // O(N)
    for(let slice_pizza = 6; 0 < slice_pizza % members; slice_pizza += 6){
        answer = slice_pizza / 6 + 1
    }
    return answer
}
```

> 이전에도 코딩을 할 때 바로 코딩하기보다는 종이에 써가면서 했었는데, 코딩테스트는 빠르게 풀어야 겠다라는 생각이 자꾸 드는 것 같다. 이제부터라도
> 문제를 보고 바로 풀려고 하기보다는 예전부터 해왔던 대로 문제를 보고 분석하면서 종이에 차근차근 정리를 하니 해결방안이 보였다.

---

## 배열 만들기 3

정수 배열 arr와 2개의 구간이 담긴 배열 intervals가 주어집니다.

intervals는 항상 [[a1, b1], [a2, b2]]의 꼴로 주어지며 각 구간은 닫힌 구간입니다. 닫힌 구간은 양 끝값과 그 사이의 값을 모두 포함하는 구간을 의미합니다.

이때 배열 arr의 첫 번째 구간에 해당하는 배열과 두 번째 구간에 해당하는 배열을 앞뒤로 붙여 새로운 배열을 만들어 return 하는 solution 함수를 완성해 주세요.

| arr	| intervals	| result |
| ---- | --- | --- |
|[1, 2, 3, 4, 5]	| [[1, 3], [0, 4]]|	[2, 3, 4, 1, 2, 3, 4, 5]|


```javascript
    function solution(arr, intervals) {
        const result1 = arr.slice(intervals[0][0], intervals[0][1] + 1)
        const result2 = arr.slice(intervals[1][0], intervals[1][1] + 1)
        return result1.concat(result2)
    }
```

```javascript
// 더 좋은 풀이
function solution(arr, intervals) {
    const [[a,b],[c,d]] = intervals;

    return [...arr.slice(a, b+1), ...arr.slice(c, d+1)];
}

```