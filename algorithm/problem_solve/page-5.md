# 다중 포인터 패턴

두 개 이상의 포인터(인덱스)를 생성한 후, 특정 조건에 따라 이 포인터들을 서로 다른 방향으로 이동시키면서 문제를 해결

배열이나 문자열 같은 선형 구조나 이중 연결 리스트, 단일 연결 리스트를 만드는 것

> 한 쌍의 값이나 조건을 충족시키는 무언가를 찾는다.<br/>
> 예시 문제: 정렬된 배열에서 두 숫자의 합이 특정 값과 같은 경우 찾기

```javascript
// 더하면 0이 되는 쌍을 찾기

sumZero([-3, -2, -1, 0, 1, 2, 3]); // [-3,3]
sumZero([-2, 0, 1, 3]); // undefined
sumZero([1, 2, 3]); // undefined

// 배열이 들어왔을 때 정렬이 되어있어야 효율적임.
```

```javascript
// 순진한 접근법

function sumZero(arr) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] + arr[j] === 0) {
        return [arr[i], arr[j]];
      }
    }
  }
}
// 시간복잡도 - O(n^2)
// 공간복잡도 - O(1)
```

```javascript
// 더 좋은 방법
function sumZero(arr) {
  let left = 0;
  let right = arr.length - 1;
  while (left < right) {
    let sum = arr[left] + arr[right];
    if (sum === 0) {
      return [arr[left], arr[right]];
    } else if (sum > 0) {
      right--;
    } else {
      left++;
    }
  }
}
// 시간복잡도 - O(N)
// 공간복잡도 - O(1)
sumZero([-4, -3, -2, -1, 0, 1, 2, 3, 10]);
```
