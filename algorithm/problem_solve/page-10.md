# 빈도수 세기 / 다중 포인터 - areThereDuplicates

가변적인 수의 인수(a variable number of arguments)를 받아들이고 전달된 인자 중 중복이 있는지 확인하는 areThereDuplicates라는 함수를 구현합니다.  빈도 카운터 패턴 또는 다중 포인터 패턴을 사용하여 이 문제를 해결할 수 있습니다.

```javascript
예시:
areThereDuplicates(1, 2, 3) // false
areThereDuplicates(1, 2, 2) // true 
areThereDuplicates('a', 'b', 'c', 'a') // true 
```
제약 조건:
Time - O(n)
Space - O(n)

보너스:
Time - O(n log n)
Space - O(1)

```javascript
function areThereDuplicates(...args) {
  const freq = {};
  for (let el of args) {
    if (freq[el]) return true;
    freq[el] = 1;
  }
  return false;
}

```

동적 인자를 받기 위해 `...arg`를 이용

`빈도수 세기`는 객체로 바꾸는게 중요.

## areThereDuplicates 솔루션 (다중 포인터)
```javascript
function areThereDuplicates(...args) {
  // Two pointers
  args.sort((a,b) => a > b);
  let start = 0;
  let next = 1;
  while(next < args.length){
    if(args[start] === args[next]){
        return true
    }
    start++
    next++
  }
  return false
}
```


## areThereDuplicates One Liner 솔루션

```javascript
function areThereDuplicates() {
  return new Set(arguments).size !== arguments.length;
}
```