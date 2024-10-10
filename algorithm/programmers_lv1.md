# 문제 풀이

## 나머지가 1이 되는 수 찾기

> 자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요. 답이 항상 존재함은 증명될 수 있습니다.

|n|result|
|-|---|
|10|3|

```javascript
// 내 풀이
function solution(n) {
    let answer = []
    for(let i = 0; i< n; i++){
        if((n % i) === 1){
            answer.push(i)
        }
    }

    return answer[0]
}
```

```javascript
// 좋은 풀이
function solution(n, x = 1) {
  while (x++) {
      if (n % x === 1) {
          return x;
      }
  }
}
```

```javascript
// 개선 풀이
function solution(n) {
    for(let i = 0; i< n; i++){
        if((n % i) === 1){
            return i
        }
    }
}
```
배열을 사용하지 않고, 바로 return 하였다. 이렇게 하면 나머지가 1이 나오는 제일 작은 수일떄 바로 return하므로 더이상 반환되지 않는다.
