# 타입스크립트의 클래스

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
