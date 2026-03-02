---
title: 빈도수 세기 - sameFrequency
description: 
created: 2025-05-26
modified: 2025-05-26
tags: []
---

# 빈도수 세기 - sameFrequency

빈도수 세기 - sameFrequency
sameFrequency라는 함수를 작성하세요. 두 개의 양의 정수가 주어졌을 때, 두 숫자의 자릿수가 같은 빈도를 갖는지 구합니다.

여러분의 솔루션은 반드시 다음과 같은 복잡성을 가져야 합니다.:

Time: O(N)

예시 인풋:

```javascript
sameFrequency(182,281) // true
sameFrequency(34,14) // false
sameFrequency(3589578, 5879385) // true
sameFrequency(22,222) // false
```

## 정답

```javascript
function sameFrequency(num1, num2){
    const str1 = num1.toString()
    const str2 = num2.toString()
  
    if(str1.length !== str2.length) return false
    //  문자열로 변환 후, 글자 수가 맞지 않으면 false

    const frequencyCounter = {};
    // 문자를 순회하면서 각 문자가 있는지 확인하기 위해 객체에 담음.

    for (let char of str1) {
        // {
        //  1 : 0, 
        //  8 : 0, 
        //  2 : 0
        // }

        frequencyCounter[char] = (frequencyCounter[char] || 0) + 1
        // 객체에 이미 문자열로 된 속성이 없으면 0
        // 객체에 이미 문자열로 된 속성이 있으면 1
    }

    for(let char of str2) {
        if (!frequencyCounter[char]) {
            return false
        }
        
        frequencyCounter[char] -= 1
        // 동일한 값이 있으면 -1하여 0으로 만듬
        // 모든 값이 0일때 true
    }
    return true
}
```

> for of문을 통해 interable한 객체를 순회한다.

