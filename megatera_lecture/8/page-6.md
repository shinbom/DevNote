# Attrs

속성 추가

Attaching additional props
기본 속성을 추가할 수 있음. 불필요하게 반복되는 속성을 처리할 때 유용한데, 버튼 등을 만들 때 적극 활용함.

```typescript
import styled from 'styled-components';


type ButtonProps = {
  type ?: 'button' | 'submit' | 'reset'
  active : boolean
}

const Button = styled.button.attrs<ButtonProps>((props) => ({
  type: props.type ?? 'button',
}))<ButtonProps>`
  background:#FFF;
  color:#000;
  border:1px solid #888;
  /* background:#fff; */

  ${(props) => props.active && css`
    background:#f00;
    color:#fff;
  `}
`;

// 상속
const PrimaryButton = styled(Button)`
  background:#fff;
  ${(props) => props.active && css`
    background:#000;
    color:#fff;
  `}
`

export default Button;
```