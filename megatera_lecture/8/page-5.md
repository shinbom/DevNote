# Props

```
키워드

Props
Attrs
```

### Props 활용

> [Passed props](https://styled-components.com/docs/basics#passed-props)
>

활성화 여부를 표현하거나, 특정 스타일을 잡아주고 싶을 때 유용함.

```typescript
import { useBoolean } from 'usehooks-ts';

import styled, { css } from 'styled-components';

type ParagraphProps = {
 active?: boolean;
}

const Paragraph = styled.p<ParagraphProps>`
 color: ${(props) => (props.active ? '#F00' : '#888')};
 ${(props) => props.active && css`
  font-weight: bold;
 `}
`;

export default function Greeting() {
 const { value: active, toggle } = useBoolean(false);
 
 return (
  <div>
   <Paragraph>
    Inactive
   </Paragraph>
   <Paragraph active>
    Active
   </Paragraph>
   <Paragraph active={active}>
    Hello, world
    {' '}
    <button type="button" onClick={toggle}>
     Toggle
    </button>
   </Paragraph>
  </div>
 );
}
```
