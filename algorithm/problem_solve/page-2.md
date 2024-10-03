# 문제의 이해

1. 문제를 이해하기
    - 자기만의 방식대로 문제를 이해했는가?
    - 문제가 어떤 입력값을 담고 있는가?
    - 어떤 출력값이 나와야 하는가?
    - 입력값이 출력값을 결정할 수 있을까 ? 문제를 해결하기 위한 충분한 정보가 제공되었는지 고민해봐야 한다.
    - 문제의 일부인 데이터의 중요한 부분에 어떻게 라벨을 지정할 수 있을까?

2. 구체적 예시 알아보기

    > 다양한 예시들을 알고 있음에 따라, 문제를 잘 이해하는데 도움이 된다.
    - 간단한 예시로 시작하기
    - 경계조건을 살펴보기
    - 빈 입력값이 있는 예제를 살펴보는 것은 유효하지 않은 입력값이 주어진 면접 상황에서 문제를 어떻게 해결해야 할지 해결 능력을 갖출 수 있도록 해줌.

3. 세부 분석
    > 문제를 세분화 하기<br/>
    > 면접관들은 수행하는 작업이 무엇인지 소통하기를 원함.

    - 주석을 사용하여 구체적으로 세부적으로 수행작업을 알 수 있도록 한다.
    - 주석을 달 경우, 시간이 부족해서 중간까지만 구현했다 하더라도 작업에 대한 틀은 잡을 수 있는 것

4. 해결 또는 단순화

    > 다른 모든 것에 집중하기 위해 시간이 많이 소요되는 부분은 무시하자

    ```javascript
    function charCount(str) {
      // 객체를 생성 후, 반환해야 한다.
      let result = {}
      // 문자열을 순회한다.
      for(let i = 0; i < str.length; i++) {
        let char = str[i]
        // 문자가 객체 안에 있다면 카운트를 추가한다.
        if(result[char] > 0) {
          result[char] ++;
        }
        // 문자가 숫자 안에 없다면 카운트는 1이다.
        else {
          result[char] = 1
        }
      }

      // 문자가 대문자일때에는 별개로 봐야하는지, 빈값일때에는 어떻게 처리해야하는지?
      // 결과를 반환한다.
      return result
    }
    ```

    > 해결을 하다가 면접관에게, 추가적으로 조치해야 할 사항이 있는지 물어볼 수도 있다.

5. 리팩토링

    - 결과를 확인할 수 있나요?
    - 결과를 다른 방식으로 도출할 수 있나요?
    - 해결한 방식외에 다른 방법을 적용할 수 있나요?
    - 해결책이 얼마나 직관적인가요?
    - 한눈에 보고 이해할 수 있나요?
    - 코드 편집기의 내용을 종이나 화이트보드에서 보더라도 이해할 수 있을까요?
    - 결과나 방법을 다른 문제에도 적용할 수 있을까요?

더 나은 성능을 이끌어 내기위해서는 시간 복잡도와 공간복잡도를 분석한다.

```javascript
// 1차 리팩토링
function charCount(str) {
  let obj = {}
  for (let i = 0; i < str.length; i++) {
    // 문자를 소문자로 치환
    let char = str[i].toLowerCase();
    // 정규표현식으로 변경
    if(/[a-z0-9]/.test(char)) {
      if(obj[char] > 0) {
        obj[char]++;
      } else {
        obj[char] = 1
      }
    }
  }
  return obj
}
```


```javascript
// 2차 리팩토링
function charCount(str) {
  let obj = {}
  for (let char of str) {
    char = char.toLowerCase()
    // 정규표현식으로 변경
    if(/[a-z0-9]/.test(char)) {
      obj[char] = ++ obj[char] || 1
    }
  }
  return obj
}
```

```javascript
// 3차 리팩토링
function charCount(str) {
  let obj = {}
  for (let char of str) {
    char = char.toLowerCase()
    // regExp에서 charCodeAt으로 변경
    if(isAlphaNumeric(char)) {
      obj[char] = ++ obj[char] || 1
    }
  }
  return obj
}


function isAlphaNumeric(char) {
  let code = char.charCodeAt(0);
  if( !(code > 47 && code < 58) && // numeric(0 - 9)
      !(code > 64 && code < 91) && // upper alpha (A-Z)
      !(code > 96 && code < 123)) { // lower alpha (a-z)
    return false
  }
  return true
}
```
> `charCodeAt`이 `regexp`보다 55%더 빠르다. 

> 함수를 구분하여 가독성을 높이자.

[charCode  vs RegExp](https://www.measurethat.net/Benchmarks/Show/15681/0/alphanumeric-string)