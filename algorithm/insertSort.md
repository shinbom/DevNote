# 삽입정렬(Insert Sort)

![insertSort](./src/insertSort.gif)

```javascript
function insertionSort(arr) {
  // 배열의 두 번째 요소부터 시작
  for (let i = 1; i < arr.length; i++) {
    let current = arr[i]; // 현재 삽입할 요소
    let j = i - 1;

    // 정렬된 부분을 오른쪽으로 이동하여 현재 요소가 들어갈 위치를 찾음
    while (j >= 0 && arr[j] > current) {
      arr[j + 1] = arr[j];
      j--;
    }
    // 현재 요소를 적절한 위치에 삽입
    arr[j + 1] = current;
  }
  return arr;
}

// 사용 예시:
const sampleList = [5, 3, 8, 4, 2];
console.log(insertionSort(sampleList)); // 출력: [2, 3, 4, 5, 8]
```

- 최선의 경우 (Best Case): O(N) — 배열이 이미 정렬된 경우, 각 요소는 한 번의 비교만 하면 되므로 효율적
<br/><br/>
- 평균 및 최악의 경우 (Average and Worst Case): O(N²) — 역순으로 정렬된 경우, 매번 모든 요소를 비교하고 이동해야 하므로 성능이 떨어짐.
