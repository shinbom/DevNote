# 분할과 정복 패턴(Divide and Conquer)

주로 배열이나 문자열 같은 큰 규모의 데이터셋을 처리함.

배열을 작은 조각으로 세분화하여 각 조각들을 어디로 이동시킬지 결정하는 작업을 통해 `큰 데이터 덩어리를 작은 조각으로 나눔`

```javascript
// 선형탐색
function search(arr, val) {
    for (let i = 0; i < arr.length; i++) {
        if(arr[i] === val) {
            return i
        }
    }
    return -1
}
// O(N)

// 이진탐색 - 분할 정복 알고리즘
function search(arr, val) {
    let min = 0;
    let max = array.length - 1;

    while(min <= max) {
        let middle = Math.floor((min + max) / 2);
        let currentElement = array[middle];

        if(array[middle] < val) {
            min = middle + 1;
        } else if (array[middle] > val) {
            max = middle - 1;
        } else {
            return middle;
        }
    }
    return -1
}
// Log(N)
```