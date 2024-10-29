# 선택정렬(Selection Sort)

![selectionSort](./src/selectionSort.gif)

```javascript
// 한 셀씩 이동하면서 현재까지 가장 작은 값을 기록(인덱스를 변수에 저장)
// 변수에 들어 있는 값보다 작은 값이 들어있는 셀을 만나면 변수가 새 인덱스를 가르키도록 변수를 대체한다.

function selectionSort(arr) {
  // 배열 전체를 반복
  for (let i = 0; i < arr.length - 1; i++) {
    // 최소값의 인덱스를 현재 위치로 설정
    let minIndex = i;

    // 나머지 배열에서 가장 작은 요소 찾기
    for (let j = i + 1; j < arr.length; j++) {
      // 현재 요소가 최소값보다 작으면 minIndex 업데이트
      if (arr[j] < arr[minIndex]) {
        minIndex = j;
      }
    }

    // 최소값이 현재 위치와 다르면 값 교환
    if (minIndex !== i) {
      // 현재 요소와 최소값 요소를 교환
      [arr[i], arr[minIndex]] = [arr[minIndex], arr[i]];
    }
  }
  return arr;
}

// 사용 예시:
const numbers = [64, 25, 12, 22, 11];
console.log(selectionSort(numbers)); // 출력: [11, 12, 22, 25, 64]
```

- 모든 경우 (Best, Average, Worst): O(N²)  
- 항상 배열을 완전하게 반복하여 최솟값을 찾고 교환하기 때문에 최선, 평균, 최악의 경우가 모두 동일
