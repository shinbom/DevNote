# 빈도수 세기 패턴 : 과제

> 두 개의 문자열을 취하며 두 문자열이 서로의 아나그램(어느 한 단어를 재배열하면 상대편 단어가 될 수 있는 것)이면 참이 반환됨.

```javascript
validAnagram("", ""); // true
validAnagram("aaz", "zza"); // false
validAnagram("anagram", "nagram"); // true
validAnagram("rat", "car"); // false
validAnagram("awesome", "awesom"); // false
validAnagram("qwerty", "qeywrt"); // true
validAnagram("texttwisttime", "timetwisttext"); // true
```

> 모두 소문자로 가정
> O(n)

```javascript
// 내 풀이
function validAnagram(word, reword) {
  // add whatever parameters you deem necessary - good luck!
  if (word.length !== reword.length) return false;

  const sortWord = [...word].sort();
  const sortReword = [...reword].sort();

  return sortWord.every((word, idx) => word === sortReword[idx]);
}

validAnagram("", "");
validAnagram("aaz", "zza");
validAnagram("anagram", "nagaram");
validAnagram("rat", "car");
validAnagram("awesome", "awesom");
validAnagram("amanaplanacanalpanama", "acanalmanplanpamana");
validAnagram("qwerty", "qeywrt");
validAnagram("texttwisttime", "timetwisttext");
```

```javascript
// 강의 풀이
function validAnagram(first, second) {
  if (first.length !== second.length) {
    return false;
  }

  const lookup = {};

  for (let i = 0; i < first.length; i++) {
    let letter = first[i];
    // if letter exists, increment, otherwise set to 1
    lookup[letter] ? (lookup[letter] += 1) : (lookup[letter] = 1);
  }
  console.log(lookup);

  for (let i = 0; i < second.length; i++) {
    let letter = second[i];
    // can't find letter or letter is zero then it's not an anagram
    if (!lookup[letter]) {
      return false;
    } else {
      lookup[letter] -= 1;
    }
  }

  return true;
}

// {a: 0, n: 0, g: 0, r: 0, m: 0,s:1}
validAnagram("anagrams", "nagaramm");
```
