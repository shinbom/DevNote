# 타입스크립트 컴파일러 옵션

```bash
tsc --init
```

tsconfig가 자동으로 생성됨.

```json
{
  "compilerOptions": {
    "target": "ESNext", // 생성되는 자바스크립트의 버전을 설정
    "module": "ESNext", // 모듈시스템을 설정
    "outDir": "dist", // 컴파일 후 생성된 파일들이 위치하고 싶은 위치 설정
    "strict": true, // 타입스크립트 타입검사를 엄격하게 할 것인지 설정
    "moduleDetection": "force",
    "skipLibCheck": true // 타입 정의 파일 검사 생략 설정(types.d.ts)
  },
  "include": ["src"] // 컴파일 할 경로 설정
}
```

타입스크립트는 기본적으로 전역모듈로 인식하고 있다. 이를 해결하기 위해서는,

1. 격리된 모듈로 바라보게 하기 위해서는 `export`라는 모듈 키워드를 넣으면 된다.
2. tsconfig.json에 옵션(`moduleDetection`)을 추가하는 방법이 있다.

[한 입 크기로 잘라먹는 타입스크립트 : 컴파일러 옵션](https://ts.winterlood.com/e7ec2f43-9d8c-4d30-bb2c-29e1b57f6a39)
