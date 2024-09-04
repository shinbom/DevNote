# this

## arguments 객체

- 함수를 호출할 때 인수들과 함꼐 암묵적으로 arguments 객체가 함수내부로 전달된다.

<aside>
📌 함수를 호출할 때 넘겨진 인자 : 함수를 호출할 떄 첫번째 인자는 0번 인덱스부터 시작
length 프로퍼티 : 호출할때 넘겨진 인자의 개수를 의미
calee 프로퍼티 : 현재 실행중인 함수의 참조값

</aside>

---

## 호출 패턴과 this 바인딩

<aside>
📌 함수를 호출할 때, 기존 매개변수로 전달되는 인자값에 더해,  arguments 객체 및 this인자가 암묵적으로 전달됨.

</aside>

<aside>
📌 함수가 호출되는 방식(호출 패턴)에 따라 this가 다른 객체를 참조(this 바인딩)함.

</aside>

---

### 객체의 메서드를 호출할 때의 this

- 해당 메서드를 호출한 객체로 바인딩 됨.

```jsx
var my Object = {
	name : 'foo',
	sayName : function () {
		console.log(this) // foo
	}
}
```

### 함수를 호출할 때의 this

- this는 전역객체에 바인딩됨.
- 브라우저에서 실행하는 경우 전역 객체는 window 객체가 됨.

---

### 생성자 함수를 호출할 때의 tihs

- 기존 함수에 new 연산자를 붙여서 호출하면 해당 함수는 생성자 함수로 동작한다.
- 객체 리터럴 방식과 생성자 함수를 통한 객체 생성 방식의 차이
    <aside>
    📌 프로토 타입 객체(__**proto__**)의 차이가 있음.
    
    </aside>


![this%202f3c41d4129b4e0aa8d9a9fba3ccc75d/Untitled.png](this%202f3c41d4129b4e0aa8d9a9fba3ccc75d/Untitled.png)

<aside>
📌 자바스크립트의 객체는 자신을 생성한 생성자 함수의 prototype 프로퍼티가 가르키는 객체를 자신의 프로토타입 객체로 설정함.

</aside>

- Constructor
  - 객체 리터럴 방식 : Object();
  - 생성자 함수 방식 : 생성자 함수 자체

---

### 생성자 함수를 new를 붙이지 않고 호출할 경우

```jsx
var qux = Person("qux", 20, "man");
console.log(qux); // undefined

console.log(window.name); // qux
```

- new없이 일반 함수 형태로 호출할 경우, this는 함수 호출이 됨에 따라 전역객체인 window로 바인딩됨.

<aside>
📌 자바스크립트에서는 일반 함수와 생성자 함수의 구분이 별도로 되지 않음에 따라,
생성자 함수로 사용할 함수의 첫 글자는 대문자료 표기하는 네이밍 규칙을 권장.

</aside>

---

### call과 apply메서드를 이용한 명시적 this 바인딩

<aside>
📌 apply와 call은 모든 함수의 부모객체인 Function.prototype의 메서드이므로, 메서드 호출이 가능하다.

</aside>

```jsx
function.apply(thisArg, argArray)
```

**apply() 메서드도 this를 특정 객체에 바인딩할 뿐, 본질적인 기능은 함수 호출이다.**

```jsx
function Person(name, age, gender) {
	this.name = name;
	this.age = age;
	this.gender = gender;
}

var foo = {}

Person.apply(foo, ['foo', 30, 'man'];
console.dir(foo) //
```

apply()나 call() 메서드는 this를 원하는 값으로 명시적으로 매핑해서 특정 함수나 메서드를 호출할 수 있다는 장점이 있음.
