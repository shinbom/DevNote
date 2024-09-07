# Blocking과 Non-Blocking

## Blocking

Node.js 프로세스에서 JavaScript를 실행할 때 JavaScript가 아닌 작업이 완료될 때까지 기다려하는 경우이다.

이벤트 루프가 Blocking작업이 발생하는 동안 JavaScript를 계속 실행할 수 없기 때문에 발생한다.

Node.js 표준 라이브러리의 모든 I/O 메서드는 비동기를 제공한다. Non-Blocking이며, 콜백함수를 허용한다.

Blocking되는 메서드들도 있다.


```javascript
const fs = require('node:fs');

const data = fs.readFileSync('/file.md'); 

moreWork()
// 파일이 읽어질 때까지 블로킹
```

비동기로 실행되게 하기 위해서는 다음과 같이 해야 한다.

```javascript
const fs = require('node:fs');

fs.readFile('/file.md', (err, data) => {
  if (err) throw err;
  console.log(data);
});
moreWork(); 

```

#### 참고

[동시성과 이벤트 처리 문제에 대한 탐구](https://0xffffffff.tistory.com/99)