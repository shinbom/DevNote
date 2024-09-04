# 함수의 return

<aside>
📌 자바스크립트 함수는 항상 리턴값을 반환한다.

</aside>

- 일반 함수나 메서드에 리턴값을 지정하지 않을 경우
    - undefined가 리턴됨.
- 생성자 함수에서 리턴값을 지정하지 않을 경우
    - 생성된 객체가 리턴됨.
    
    <aside>
    📌 명시적으로 생성된 객체가 아닌, 다른 객체를 리턴하는 경우
    
    </aside>
    
    ```jsx
    function Person(name, age, gender) {
    	this.name = name;
    	this.age = age;
    	this,gender = gneder;
    
    	// 명시적으로 리턴
    	return {name : 'bar', age : 20, gender : 'woman'};
    }
    
    var foo = new Person('foo', 30, 'man');
    console.dir(foo); // name : 'bar', age : 20, 'gender' : 'woman';
    ```
    
    - 객체 리터릴 방식의 특정 객체로 지정해서 넘긴 경우, new 생성자 함수를 이용하여 새로운 객체를 생성하더라도, 리턴값에서 명시적으로 넘긴 객체나 배열이 리턴된다.
    
    <aside>
    📌 생성자 함수의 리턴값으로 넘긴 값이 객체가 아닌 불린, 숫자, 문자열의 경우 변경되지 않고 this로 바인딩된 객체가 리턴됨.
    
    </aside>
    
    ```jsx
    function Person(name, age, gender) {
    	this.name = name;
    	this.age = age;
    	this.gender = gender;
    
    	return 100;
    }
    var foo = new Person('foo', 30, 'man');
    console.log(foo); // Person{name : 'foo', age : 30, gender : 'man'};
    ```