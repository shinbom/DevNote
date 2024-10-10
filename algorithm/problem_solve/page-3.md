# 문제 해결 패턴

> 일반적인 문제 해결 패턴을 습득하자

## 빈도수 세기 패턴(Frequency Counters)

### 유용할 때

- 여러 데이터와 입력값이 서로 비슷한 값으로 구성되어 있는지
- 서로 간의 아나그램인지
- 값이 다른 값에 포함되는지 여부를 비교하거나
- 데이터를 입력 값이나 두 개 이상의 빈도 혹은 특정하게 발생하는 빈도를 비교할 때


```javascript
  // 예시
  // 첫번째 배열과 두번째 배열이 제공되고, 
  // 두번째 배열에는 첫번째 배열의 값의 제곱수들이 존재하는지 확인하기.

  same([1,2,3], [4,1,9]) // true
  same([1,2,3], [1,9]) // false
  same([1,2,1], [4,4,1]) // false

```


```javascript

// 순진한 접근법

function same(arr1, arr2) {
  if(arr.length !== arr2.length) {
    return false
  }
  for(let i = 0; i < arr1.length; i++) {
    let correctIndex = arr2.indexOf(arr[1] ** 2)
    if(correctIndex === -1) {
      return false
    }
    arr2.splice(correctIndex, 1)
  }
  return true
}

[1,2,3], [9,1,4,4] // false
[1,2,3,2],[9,1,4,4] // true

// BigO - O(n^2)

```

```javascript

  // 빈도 카운터 패턴
  // Refactoring
  function same(arr1, arr2) {
    if(arr1.length !== arr2.length) {
      return false
    }
    let frequencyCounter1 = {}
    let frequencyCounter2 = {}
    for (let val of arr1) {
      frequencyCounter1[val] = (frequencyCounter1[val] || 0) + 1
    }
    for (let val of arr2) {
      frequencyCounter2[val] = (frequencyCounter1[val] || 0) + 1
    }
    for(let key in frequencyCounter1) {
      if(!(key ** 2 in frequencyCounter2)){
        return false
      }
      if(frequencyCounter2[key ** 2] !== frequencyCounter1[key]){
        return false
      }
    }
    return true
  }

  // BigO - O(n)
```

> 빈도 카운터의 개념은 보통 `객체를 사용`<br/>
> 두 개의 배열을 객체로 세분화하여 각 배열의 요소들을 분류한 다음 각 배열을 비교