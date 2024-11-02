# 함수형 컴포넌트 vs 클래스형 컴포넌트

## 생명주기 메서드의 부재

- props
  - 함수형 컴포넌트 
    - props를 받아 단순히 리액트 요소만 반환
    - `생명주기 메서드 사용 불가`
    - `useEffect` 훅을 이용하여 `componentDidMount, componentDidUpdate, componentWillUnmount`를 `비슷`하게 구현 가능

      > useEffect는 생명주기를 위한 훅이 아님.<br/>
      > 컴포넌트의 state를 활용해 부수 효과를 만드는 매커니즘

  - 클래스형 컴포넌트 
    - render 메서드에 있는 React.Component를 상속 받아 구현하는 자바스크립트 클래스 
    - `생명주기 메서드 사용 가능`

## 함수형 컴포넌트의 렌더링된 값

> `함수형 컴포넌트`는 렌더링 된 값을 `고정`하지만, 클래스형 컴포넌트는 그러지 못함

```tsx
import React from 'react'

interface Props {
  user : string
}

export function FunctionalComponent (props : Props) {
  const showMessage = () => {
    alert(`Hello ${props.user}`)
  }

  const handleClick = () => {
    setTimeout(showMessage, 3000)
  }

  return <button onClick={handleClick}>클릭</button>
}
```

- 함수형 컴포넌트
  - this와 다르게 state, props는 인수로 받기 때문에 값을 변경할 수 없고, 값을 그대로 사용함

```tsx
import React from 'react'

interface Props {
  user : string
}

export class ClassComponent extends React.Component<Props, {}>{
  const showMessage = () => {
    alert(`Hello ${this.props.user}`)
  }

  private handleClick = () => {
    setTimeout(this.showMessage, 3000)
    // 클릭 시, 3초뒤에 변경된 props를 기준으로 메세지가 뜸.(의도한 방향이 아님)

  }

  return <button onClick={this.handleClick}>클릭</button>
}
```


```tsx
import React from 'react'

interface Props {
  user : string
}

export class ClassComponent extends React.Component<Props, {}>{
  const showMessage = (name : string) => {
    alert(`Hello ${name}`)
  }

  private handleClick = () => {
    const {
      props : {user}
    } = this

    setTimeout(this.showMessage(name), 3000)
    // this.props를 좀 더 일찍 부르고, 함수의 인수로 넘김
  }

  public render() {
    <button onClick={this.handleClick}>클릭</button>
  } 
}
```

```tsx
import React from 'react'

interface Props {
  user : string
}

export class ClassComponent extends React.Component<Props, {}>{
  // render 함수안에 필요한 모든 값을 넘기는 방법
  // 함수가 가진 목적에 맞지 않은 것으로 보임

  render() {
    const {
      props : {user}
    } = this

    const showMessage = (name : string) => {
      alert(`Hello ${name}`)
    }

    handleClick = () => {
      setTimeout(showMessage, 3000)
    }

    return <button onClick={this.handleClick}>클릭</button>
  } 
```

- 클래스형 컴포넌트
  - this를 기준으로 렌더링이 일어남

---

### 클래스형 컴포넌트를 공부해야 하는 이유

리액트가 오래된 만큼, 클래스형 컴포넌트들로 작성된 코드들이 많기 때문에 이러한 흐름들을 알 기 위해서는 클래스형 컴포넌트에 대한 지식이 필요함

자식 컴포넌트에서 발생한 에러에 대한 처리는 현재 클래스형 컴포넌트로만 가능하므로 에러 처리를 위해서라도 클래스형 컴포넌트에 대한 지식은 필요함
