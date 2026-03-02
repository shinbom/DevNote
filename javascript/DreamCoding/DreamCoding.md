---
title: "DreamCoding"
description: 
created: 2024-09-09
modified: 2024-09-04
tags: []
---

# DreamCoding

Javascript transcompiler - BABEL을 이용해 변환

Single Page Application - SPA

API - Application Programing Interface

console API - 브라우저가 가지고 있는 API

자바스크립트의 공식사이트

- ecma-international.org
- developer.mozilla.org

### DOM에서 script의 위치에 따라 로딩 방법

- Dom실행 순서
    1. HTML Pharsing
    2. Script Fetching(스크립트 다운로드)
    3. Executing Script(스크립트 실행)

<aside>
👌 DOM을 그릴 때, 최초 HTML을 파싱한다. 이후 script를 만나면 script를 다운로드하게 된다.
script다운, 실행이 완료된 후, 다시 HTML을 파싱한다.
script의 위치와 속성(asnc, defer)에 따라, 다운로드 + 실행의 순서가 바뀌게 된다.

</aside>

```jsx
<!DOCTYPE html>
<html lang="ko">
<head>
	<meta charset="utf-8">
	<title>Document</title>
	<script src="test.js"></script>
</head>
```

```jsx
<!DOCTYPE html>
<html lang="ko">
<head>
	<meta charset="utf-8">
	<title>Document</title>
</head>
<body>
<script src="test.js"></script>
</body>
```

js가 무겁거나, js에 의존적인 경우 사용자들은 다운로드 + 실행되기를 기다려야 한다.

- async
    
    ```jsx
    <!DOCTYPE html>
    <html lang="ko">
    <head>
    	<meta charset="utf-8">
    	<title>Document</title>
    	<script src="test.js" async></script>
    	<script src="test2.js" async></script>
    </head>
    ```
    
    async는 스크립트를 만나는 순간, 다운로드만 하고, 다운로드가 완료되었을 때 실행하게 된다.
    
    하지만, HTML Pharsing이 다 되지 않은 상태에서 실행되기 때문에, 선택자가 올바르게 동작하지 않을 수 있고,  **js의 크기에 따라 다운로드되어지는 순서에 따라 실행되어 개발자가 작성한 스크립트 순서대로 실행되지 않을 수 있음.**
    
- **defer**
    
    ```jsx
    <!DOCTYPE html>
    <html lang="ko">
    <head>
    	<meta charset="utf-8">
    	<title>Document</title>
    	<script src="test.js" defer></script>
    	<script src="test2.js" defer></script>
    </head>
    ```
    
    defer는 HTML Pharsing의 경우에는, pharsing하는 동안 동시에, 다운로드를 미리 해두고 HTML Pharsing이 완료된 후, 바로 js를 실행하게 되어 가장 안정적이다.
    
- use strict - 자바스크립트가 엄격해짐. 자바스크립트 엔진이 효율적으로 처리할 수 있게 됨.
    
    
    ## 클래스
    
    ### getter와 setter
    
    ```jsx
    class User {
    	constructor ( firstName, lastName, age) {
    		this.fistName = firstName;
    		this.fistName = lastName;
    		this.age= age;	
    	}
    
    	get age() {
    		return this._age;
    	}
    	
    	set age(value) {
    	// if (value < 0) {
    			throw Errow('age can not negative');	
    		}
    		this.age = value < 0 ? 0 : value;	
    	}
    }
    
    const user = new User('Steve', 'Job', -1);
    ```
    
    <aside>
    👌 getter와 setter를 조금 더 공부해야 할 것으로 보임.
    
    </aside>
    
    ### publicField와 privateField
    
    ```jsx
    class Experiment {
    	publicField = 2;
    	#privateField = 0; // #를 붙이게 되면 privateField가 됨.
    }
    const experiment = new Experiment();
    console.log(experiment.publicField); // 2
    console.log(experiment.privateField); 
    // privateField는 undefined 접근이 불가능함에 따라 undefined가 출력됨.
    ```
    
    publicField는 외부에서 접근이 가능하지만, privateField는 접근이 불가능함
    
    (브라우저 지원이 거의 안됨) - 바벨 사용해야 함.
    
    ### static함수
    
    ```jsx
    class Shape {
    	constructor(width, height, color) {
    		this.width = width;
    		this.height = height;
    		this.color = color;
    	}
    	
    	draw () {
    		console.log(`drawing ${this.color} color of`);	
    	}
    
    	getArea() {
    		return width * this.height;
    	}
    }
    
    /*  상속과 다양성 */
    
    class Rectangle extends Shape {}
    class Triangle extends Shape {
    	/* Overwriting */
    	draw() {
    		super.draw();
    		console.log('super');	
    	}
    	getArea() {
    		return(this.width * this.height) / 2;
    	}
    }
    
    const rectangle = new Rectangle(20, 20, 'blue');
    rentangle.draw();
    const triangle = new Triangle)(20, 20, 'red');
    triangle.draw();
    
    console.log(rectangle instanceof Rectangle); // true
    console.log(triangle instanceof Rectangle); // false
    console.log(triangle  instanceof Triangle); // true
    console.log(triangle instanceof Shape); // true
    console.log(triangle instanceof Object); // true
    console.log(triangle.toString()); // [object Object] 
    
    ```
    
    instanceOf
    
    - 인스턴스 인지 확인하는 것 ( true || false Return)
    
    ## 오브젝트
    
    ```jsx
    const obj = {}; // 'Object literal' syntax
    sont obj2 = new Object(); // 'object constructor' syntax
    
    print(name, age);
    function print(name, age) {
    	console.log(person.name);
    	console.log(person.age);
    }
    
    const ellie = {
    	name : 'ellie', age : 4 };
    }
    print(ellie);
    
    //자바스크립트는 동적 타입 업어임에 따라, 하단에 추가적으로 프로퍼티를 추가할 수 있음. (유지보수가 어려움)
    ellie.hasJob = true;
    
    delete ellie.hasJob; // 삭제 가능
    
    console.log(ellie.name); // 코딩하는 순간 값을 받아오고 싶을떄, 쓰는 경우
    console.log(ellie['name']); // 실시간으로 원하는 값을 받아오고 싶을때 사용
    
    // 예);
    function printValue(obj, key) {
    	console.log(obj[key]);
    }
    print(ellie, 'name');
    print(ellie, 'age');
    
    const person1 = { name : 'bob', age : 2 }
    const person2 = { name : 'steve', age : 3 }
    const person3 = { name : 'dave', age : 4 }
    const person4 = new Person('ellie', 30);
    
    // 오브젝트를 필요할때 일일이 만들게 될 때, 반복해서 작성해야 할때 간단하게 작성하는 방법.
    // Constructor Function(생성자 함수)
    function Person(name, age) {
    	// this = {};
    	this.name;
    	this.age;
    }
    
    // in operator 함수안에 키가 있는지 없는지 확인하는 것.
    console.log('name' in ellie);
    
    // for in [vs] for of
    // for (key in obj)
    for (key in ellie) {
    	console.log(key);
    }
    
    // for (value of iterable)
    const array = [1, 2, 4, 5];
    for (value of array) {
    	console.log(value); // 1, 2, 4, 5;
    }
    
    // Cloning
    const user = {name : 'ellie', age : '20'};
    const user2  = user; // name : 'ellie';
    user2.namer = 'coder';
    console.log(user) // name : coder;
    
    // 오브젝트 복사 방법
    // old way 
    const user3 = {};
    for (key in user) {
    	user3[key] = user[key];
    }
    console.log(user3);
    
    // recent way 
    Object.assign();
    //메소드는 열거할 수 있는 하나 이상의 출처 객체로부터 대상 객체로 속성을 복사할 때 사용합니다. 대상 객체를 반환합니다.
    
    const user4 = Object.assign({}, user);
    console.log(user4);
    ```
    
    ## 배열(Array)
    
    ```jsx
    const arr1 = new Array();
    const arr2 = [1, 2];
    arr2[0] // 1;
    arr2[1] // 2;
    
    //Index Position
    arr2.length // 2;
    
    // Lopping over an array
    // 1. for
    for (let i = 0; i < arr2.length; i++) {
    	console.log(arr2[i]);
    }
    
    // 2. for of
    for (let item of arr2) {
    	console.log(item);
    }
    
    // 3. forEach
    arr2.forEach(function (value, idx, array) {
    	console.log(value); 
    	console.log(idx);  
    	console.log(array);  
    });
    
    // 4. Addtion, deletion, copy
    // push : add an item  
    	arr2.push('test'); // [1, 2, 'test'];
    // pop :remove an item 
    	arr2.pop(); // [1,2]
    ```
    
    <aside>
    👌 shift, unshift가 pop과 push보다 느림.
    - 길이가 길면 길수록 shift, unshift는 느림.
    - 중간에 데이터를 넣는 것은 index를 이용하기 때문에, 빠름.
    
    </aside>
    
    ```jsx
    const fruits2 = ['apple', 'banana'];
    fruits2.splice(1, 1);
    
    // combine
    var a = [1,2];
    var b = [3,4];
    var c = a.concat(b); // [1,2,3,4] 
    
    // 5. Searching
    console.log(fruits.indexOf(''); // array in item search -- index return or -1 return 
    console.log(fruits.includes(''); // array in item search - true or false return
    console.log(fruits.lastIndexOf('');
    ```
    
    ## JSON - Javascript Object Notation
    
    HTTP : Hypertext transfer protocol
    
    AJAX를 이용해서 데이터를 받아올 수 있음
    
    Asynchronous Javascript and XML
    
    XHR : XMLHttpRequest Object : 브라우저 API제공하는 오브젝트
    
    <aside>
    👌 fetch() API : ie에서는 지원하지 않음.
    
    </aside>
    
    서버와 데이터를 주고받을때에는 XML뿐만 아니라, 다른 것들도 주고 받을 수 있음.
    
    JSON : key와 value로 이루어져 있음.
    
    - Object를 JSON으로 어떻게 변경할지에 대해서 공부
    - JSON을 Object로 어떻게 변환할지에 대해서 공부
    
    ```jsx
    //JSON
    //JavaScript Object Notation
    
    //1. Object to JSON
    let json = JSON.stringingfy(true);
    console.log(json) // true
    
    const rabbit = {
    	name : 'tori',
    	color : 'white',
    	size : null,
    	birthDate : new Date(),
    	jump : () => {
    		console.log(`${name} can jump!`);
    	},
    };
    
    // ECMA6의 symbol은 JSON에 포함되지 않음. 
    
    json = JSON.stringfy(rabbit, (key, value) => {
    	console.log(`key : ${key}, value : ${value}`);
    	return key === 'name' ? 'ellie' : value;
    });
    // JSON.stringfy 세밀하게 제어할때 콜백 함수를 사용함
    console.log(json)
    ;
    
    //2. JSON to Object
    json = JSON.stringify(rabbit);
    const obj = JSON.parse(json);
    obj.jump(); // uncaught typeError - 메서드를 json으로 변경후, 다시 object로 변경함에 따라 method가 사라져서 오류가 발생함.
    
    rabbit.birthDate.getDate() // 29
    obj.birthDate.getDate() 
    // uncaught typeError - stringfy를 하게 됨에 따라, Date객체가 반환한 string값을 저장함에 따라 getDate라는 메서드가 존재하지 않음.
    // 그래서, 값을 새로 얻고 싶다면, 콜백 함수를 이용해서 값을 변경해야 함.
    
    const obj = JSON.parse(json, (key, value) => {
    	console.log(`key : ${key}, value : ${value}`);
    	return key === 'birthDate' ? new Date(value) : value;
    });
    
    ```
    

[프론트엔드 필수 브라우저 101](DreamCoding%2003093a5820114c1d8c53efd5b803fcf4/%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%86%AB%E1%84%90%E1%85%B3%E1%84%8B%E1%85%A6%E1%86%AB%E1%84%83%E1%85%B3%20%E1%84%91%E1%85%B5%E1%86%AF%E1%84%89%E1%85%AE%20%E1%84%87%E1%85%B3%E1%84%85%E1%85%A1%E1%84%8B%E1%85%AE%E1%84%8C%E1%85%A5%20101%2083ff275e68404bab9d89f7e87c061e02.md)