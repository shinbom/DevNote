# 기준점 간 이동 배열 패턴(Sliding Window Pattern)

배열이나 문자열과 같은 일련의 데이터를 입력하거나 특정 방식으로 연속적인 해당 데이터의 하위 집합을 찾는 경우

```javascript
// 가장 긴 시퀀스의 고유 문자를 찾는 함수
'hellothere'
// hel
// lother
// e


//  배열과 숫자 하나를 전달하고 서로 마주한 두 숫자의 가장 큰 합계를 찾기

maxSubarraySum([1,2,5,2,8,1,5], 2) // 10
maxSubarraySum([1,2,5,2,8,1,5], 4) // 17
maxSubarraySum([4,2,1,6], 1) // 6
maxSubarraySum([4,2,1,6,2], 4) // 13
maxSubarraySum([], 4) // null

// 초기 해결방안

function maxSubarraySum(arr, num) {
  if ( num > arr.length){
    return null;
  }
  var max = -Infinity;
  for (let i = 0; i < arr.length - num + 1; i ++){
    temp = 0;
    for (let j = 0; j < num; j++){
      temp += arr[i + j];
    }
    if (temp > max) {
      max = temp;
    }
  }
  return max;
}
// O(N^)

maxSubarraySum([2,6,9,2,1,8,5,6,3],3)

// 리팩토링
function maxSubarraySum(arr, num){
  let maxSum = 0;
  let tempSum = 0;
  if (arr.length < num) return null;
  for (let i = 0; i < num; i++) {
    maxSum += arr[i];
  }
  tempSum = maxSum;
  for (let i = num; i < arr.length; i++) {
    tempSum = tempSum - arr[i - num] + arr[i];
    maxSum = Math.max(maxSum, tempSum);
  }
  return maxSum;
}

// O(N)

maxSubarraySum([2,6,9,2,1,8,5,6,3],3)
```
