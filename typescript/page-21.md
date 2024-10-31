# 클래스

```typescript
class Student {
  // field
  name;
  grade;
  gender;

  // contructor
  constructor(name, grade, gender) {
    this.name = name;
    this.grade = greade;
    this.gender = gender;
  }

  // method
  study() {
    console.log('공부')
  }

  introduce () {
    console.log(`안녕하세요. ${this.name}`)
  }
}

// instance 생성
let student = new Student("신봄", "A+", 'male);
student.study()
```

```typescript
class StudentDeveloper extends Student {
  // filed
  favoriteSkills;

  // constructor
  contructor(name, grade, gender, favroriteSkill) {
    // super
    super(name, gread, gender);
    this.favoriteSkill = favroriteSkill;
  }

  // method
  programming() {
    console.log(`${this.favoriteSkil}로 프로그래밍`);
  }
}

const studentDeveloper = new StudentDeveloper(
  "신봄",
  "B+",
  "male",
  "Typescript"
);
```

## 타입스크립트의 클래스

```typescript
const employee = {
  name: "신봄",
  gender: "male",
  position: "developer",
  work() {
    console.log("work");
  },
};

class Employee {
  // field
  name: string;
  gender: string;
  position: string;

  // constructor
  constructor(name: string, gender: string, position: string) {
    this.name = name;
    this.gender = gender;
    this.position = position;
  }

  // method
  work() {
    console.log("일함");
  }
}

const employee = new Employee("신봄", "male", "developer");

const employeeB: Employee = {
  name: "",
  gender: "male",
  position: "",
  work() {},
};
```

`employeeB`는 구조적으로 타입을 결정하는 구조적 타입 시스템을 따르기 때문에 가능하다.

```json
// tsconfig.json

{
  "compilerOptions": {
    "target": "ESNext",
    "module": "ESNext",
    "outDir": "dist",
    "strict": true,
    "moudleDetection": "force",
    "allowJs": true,
    // "noImplicitAny": true // any 타입오류를 허용할 것인지 아닌지에 대한 옵션
  },
  "ts-node": {
    "esm": true
  },
  "include" ["src"]
}
```

> any타입에 할당되는 위험한 상황을 방지하기 위해 "anoImplicitAny"옵션은 건드리지 않는 것이 좋다.

```typescript
class ExecutiveOfficer extends Employee {
  // field
  officeNumber: number;

  // constructor
  constructor(
    name: string,
    gender: string,
    position: string,
    officeNumber: number
  ) {
    super(name, gender, position);
    this.officeNumber = officeNumber;
  }

  // method
}
```

자식 클래스는 `super()`가 있어야 타입 오류가 발생하지 않는다.

## 접근제어자(Access Modifier)

```typescript
class Employee {
  // field
  private name: string;
  gender: string;
  protected position: string;

  // constructor
  constructor(name: string, gender: string, position: string) {
    this.name = name;
    this.gender = gender;
    this.position = position;
  }

  // method
  work() {
    console.log("일함");
  }

  getName() {
    return ${this.name}
  }
}

const employee = new Employee("신봄", "male", "developer");
employee.name = "홍길동"; // name속성은 private 이며 Employee안에서만 접근할 수 있습니다.
employee.gender = "femail";
```

접근제어자는 기본적으로 `public`

### private

```typescript
class ExecutiveOfficer extends Employee {
  // field
  officeNumber: number;

  // constructor
  constructor(
    name: string,
    gender: string,
    position: string,
    officeNumber: number
  ) {
    super(name, gender, position);
    this.officeNumber = officeNumber;
  }

  // method
  getName() {
    return this.name; // name속성은 private 이며 Employee안에서만 접근할 수 있습니다.
  }
}
```

`private`은 클래스 내에서만 접근할 수 있음.

클래스 내부에서만 접근할 수 있으므로, 별도의 메소드를 만들어서 리턴하도록 해야 접근할 수 있다.

자식클래스에서도 접근할 수 없음

### protected

```typescript
class ExecutiveOfficer extends Employee {
  // field
  officeNumber: number;

  // constructor
  constructor(
    name: string,
    gender: string,
    position: string,
    officeNumber: number
  ) {
    super(name, gender, position);
    this.officeNumber = officeNumber;
  }

  // method
  getName() {
    return this.name; // name속성은 private 이며 Employee안에서만 접근할 수 있습니다.
  }

  getPosition() {
    return this.position;
  }
}
```

`protected`도 클래스 내부에서만 접근할 수 있지만, 자식 클래스에서 접근을 허용하고 싶으면, `protected`를 사용하면 된다.

---

### 생성자

```typescript
//AS_IS
class Employee {
  //filed
  private name: string;
  protected gender: string;
  public position: string;

  constructor(
    private name: string, // name식별자가 중복되었습니다.
    protected gender: string, // gender식별자가 중복되었습니다.
    public position: string // position식별자가 중복되었습니다.
  ) {
    this.name = name;
    this.age = age;
    this.position = position;
  }
}
```

생성자에 접근제어자를 달면 자동으로 필드를 알아서 생성함.

그러므로, `constructor`에 접근 제어자를 달면 `filed`에는 정의하지 않아도 됨

그리고 자동으로 값도 할당이 됨.

```typescript
// TO_BE
class Employee {
  //filed
  constructor(
    private name: string,
    protected gender: string,
    public position: string
  ) {}
}
```

## 인터페이스와 클래스

```typescript
interface CharacterInterface {
  name: string;
  moveSpeed: number;
  move(): void;
}

class Character implements CharacterInterface {
  constructor(
    public name: string,
    public moveSpeed: number,
    private extra: string
  ) {}

  move(): void {
    console.log(`${this.moveSpeed} 속도로 이동`);
  }
}
```

클래스의 타입정의는 `implements`를 이용한다.

`interface`를 이용하여 정의된 속성들은 `public`만 허용됨.

`private`필드가 필요하다면, 별도로 정의를 해줘야 함.
