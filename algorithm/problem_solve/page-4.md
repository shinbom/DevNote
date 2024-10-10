# 빈도수 세기 패턴 : 과제

> 두 개의 문자열을 취하며 두 문자열이 서로의 아나그램(어느 한 단어를 재배열하면 상대편 단어가 될 수 있는 것)이면 참이 반환됨.

```javascript
validAnagram('', '') // true
validAnagram('aaz', 'zza') // false
validAnagram('anagram', 'nagram') // true
validAnagram('rat', 'car') // false
validAnagram('awesome', 'awesom') // false
validAnagram('qwerty', 'qeywrt') // true
validAnagram('texttwisttime', 'timetwisttext') // true
```

> 모두 소문자로 가정