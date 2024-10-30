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
