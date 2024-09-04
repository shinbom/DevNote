# 스코프(Scope)

1. 전역 스코프(Global scope) : 스크립트 전체에서 참조, 어느곳에서든 참조됨.
2. 지역 스코프(Local scope) : 정의된 함수 내에서만 참조, 밖에서는 참조되지 않음.

## 유효범위의 특징

1. 함수단위의 유효범위(function-level-scope)

   - 함수 코드 블럭 내에서 선언된 변수는 함수 코드 블럭 내에서만 유효하고, 함수외부에서는 유효하지 않다.

   <aside>
   ⚠️ ES6이후, let 키워드를 사용할 경우, block-level scope를 사용할 수 있음.

   </aside>

2. 변수명 중복 허용

   - 글로벌 영역에 변수를 선언하면, 어느곳에서든 참조할 수 있는 global scope를 갖는 전역 변수가 됨.

3. 암묵적 전역(implied globals)

   - 명시적으로 var를 붙여주지 않으면 암묵적 전역 변수가 됨.

4. **렉시컬 스코프(Lexical scoping - Static scoping)**
   - 함수를 처음 선언하는 순간, 함수 내부의 변수는 자기 스코프로부터 가장 가까운 곳(상위범위에서)에 있는 변수를 계속 참조하게 됨.

참고 : [https://www.zerocho.com/category/JavaScript/post/5740531574288ebc5f2ba97e](https://www.zerocho.com/category/JavaScript/post/5740531574288ebc5f2ba97e)

---

<aside>
📌 ECMA6 이후로는 var는 사용되지 않음.
</aside>
<br/>
var : 함수단위 스코프<br/>
let, contst : 블록단위 스코프
