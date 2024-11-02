# 함수형 컴포넌트(Functional Component)

```tsx
import { useState } from 'react'

type SampleProps = {
  text : string
  required ?: boolean
}

export function SampleComponent({ text, required } : SampleProps ) {
  const [count, setCame] = useState<number>(0)

  function handleClick = () => {
    const newValue = count + 1
    setCount(newValue)
  }

  return (
    <div>
      <p>{text}</p>
      <p>{!required ? '필수 아님' : '필수'}</p>
      <button type='button' onClick={handleClick}>증가</button>
    </div>;
  )
}
```

- `render`내부에서 필요한 함수를 선언할 때 `this`바인딩이 필요없음
- `state`가 각각의 원시값, 객체로 관리되어 사용하기가 편리함.
