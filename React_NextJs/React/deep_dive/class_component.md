# 클래스형 컴포넌트

```tsx
import React from 'react'


interface SampleProps { 
  required?: boolean
  text : string
}

interface SampleState {
  count : number
  isLimited ?: boolean
}

class SampleComponent extends React.Component<SampleProps, SampleState> {
private constructor(props : SampleProps) {
  super(props)
  this.state = {
    count : 0
    isLimited : false
  }

  private handleClick = () => {
    const newValue = this.state.count + 1
    this.setState({ count : newValue, isLimited : newValue >= 10})
  }


  public render() {
    const {
      props : { required, text }
      state: { count, isLimited }
    } = this

    return (
      <div>
        Sample COmponent
        <div>{required ? '필수' : '필수 아님'}</div>
        <div>문자 : {text}</div>
        <div>count : {count}</div>
        <button onClick={this.handleClick} disabled={isLimited}>
          증가
        </button>
      </div>
    )
  }
}
```

- constructor()
  - 컴포넌트가 초기화되는 시점에 호출
  - constructor 내부에서 state를 초기화 할 수 있음
  - `super()`를 이용하여, 상속받은 상위 컴포넌트에 접근할 수 있도록 도와줌

- state
  - 클래스형 컴포넌트 내부에서 관리하는 값
  - 값은 항상 객체여야만 함
  - **변화가 있을 때마다 리렌더링이 발생함**

- props
  - 컴포넌트에 속성을 전달하는 용도

- 메서드
  - constructor에서 this바인딩
    - 일반 함수로 호출 시 this에 전역 객체가 바인딩(strict모드에서는 undefined)되므로 bind를 활용해 강제로 this를 바인딩 해야 함.

    ```jsx
    class SampleComponent extends Component<Props, State>{
      private constructor (props : Props) {
        super(props)
        this.state = {
          count : 1
        }

        // this를 현재 클래스로 바인딩
        this.handleClick = this.handleClick.bind(this)
      }
    }
    ```

  - 화살표 함수를 사용
    - 실행시점이 아닌 작성시점에 this가 상위 스코프로 결정되는 화살표 함수를 사용하면 바인딩 하지 않아도 됨.

  - 렌더링 함수 내부에서 함수를 새롭게 만들어 전달

    ```jsx
    <button onClick={() => this.handleClick()}>증가</button>
    ```

    - 매번 렌더링이 일어날 떄마다 새로운 함수를 생성해서 할당하게 되므로 `최적화를 수행하기 어려움`

## 리액트 생명주기(Life Cycle)

![](./src/react_lifecycle.jpeg)
[React Life Cycle Diagram](https://projects.wojtekmaj.pl/react-lifecycle-methods-diagram/)

### 생명주기 메서드 실행시점

- 마운트(mount) : 컴포넌트가 생성되는 시점
- 업데이트(update) : 이미 생성된 컴포넌트가 변경되는 시점
- 언마운트(unmount) : 컴포넌트가 더이상 존재하지 않는 시점

---

- **render()**
  - 컴포넌트가 UI를 렌더링하기 위해 사용
  - 항상 순수해야 하며 부수효과가 없어야 함
  - 같은 입력값(props 또는 state)이 들어가면, 항상 같은 결과물을 반환해야 함
  - `render함수 내부에서 state를 직접 업데이트하는 this.setState를 호출하면 안됨. state를 변경하는 일은 메서드나 다른 생명주기 메서드 내부에서 발생해야 함`

- **componentDidMount()**
  - 마운트되고 준비가 된 후 호출되는 생명주기 메서드
  - `render() 와는 다르게 함수 내부에서 this.setState()로 state 값을 변경하는 것이 가능함`
  - this.setState() 호출 시, state가 변경되고, 즉시 렌더링을 시도하는데, 브라우저가 실제로 UI를 업데이트하기 전에 실행되어 `사용자가 변경되는 것을 눈치챌 수 없게 만듬`
  - 일반적으로 state를 다루는 것은 생성자(constructor)에서 하는 것이 좋다.
  - 생성자 함수에서 할 수 없는것
    - API 호출 후 업데이트
    - DOM에 의존적인 작업(이벤트 리스너 추가 등)

- **componentDidUpdate()**
  - 컴포넌트 업데이트가 일어난 이후 즉시 실행됨
  - 일반적으로 state나 props의 변화에 따라 DOM을 업데이트하는 등에 쓰임
  - `this.setState()`를 사용할 수 있음.
    - 적절한 조건문으로 감싸지 않는다면 `this.setState()`가 계속 호출되는 일이 발생할 수 있음

- **componentWillUnmount()**
  - 컴포넌트가 언마운트 되거나, 사용되지 않기 직전에 호출
  - `메모리 누수나 불필요한 동작을 막기 위한 클린업 함수를 호출하기 위한 최적의 위치`
  - `this.setState()`를 호출할 수 없음

- **shouldComponentUpdate()**
  - state나 prop의 변경으로 리렌더링 되는 것을 막고 싶을 때 사용
  - 컴포넌트의 영향을 받지 않는 변화에 정의할 수 있음

- **static getDerivedStateFormProps()**

  - `render()를 호출하기 직전에 호출`
  - 다음에 올 props를 바탕으로 현재 state를 변경하고 싶을 때 사용할 수 있음
  - static으로 선언되어 this에 접근할 수 없음
  - 반환하는 객체는 내용이 모두 state로 들어가게 되며, null로 반환 시 아무일도 일어나지 않음

  ```jsx
  static getDerivedStateFromProp(nextProps : Props, prevState : State) {
    <!--  -->
    if(props.name !== state.name) {
      return {
        name : props.name
      }
    }
  }
  ```

  > getDerivedStateFromProps는 불필요한 사용을 피하는 것이 좋음. 대부분의 경우 상태 동기화는 불필요하거나 다른 방식으로 더 효율적으로 처리될 수 있음. <br/><br/>주로 특별한 경우에만 사용되며, 무분별하게 사용하면 코드 복잡성이 증가할 수 있음.

  ---

  - **getSnapShotBeforeUpdate()**

    - DOM이 업데이트되기 직전에 호출
    - 반환되는 값은 componentDidUpdate로 전달됨
    - DOM에 렌더링되기 전에 윈도우 크기를 조절하거나 스크롤 위치를 조정하는 등의 작업을 처리하는데 용이함

    ```tsx
    getSnapshotBeforeUpdate(prevProps : Props, prevState : State) {
      // 메시지가 추가되기 전의 스크롤 위치를 기록
      if (prevProps.list.length < this.props.list.length) {
        const list = this.listRef.current
        return list.scrollheight - list.scrollTop
      }
      return null
    }

    componentDidUpdate(prevProps, prevState, snapshot) {
      /*
        componentDidUpdate 메서드의 세 번째 인자 snapshot은 getSnapshotBeforeUpdate에서 반환한 값
      */
      if(!snapshop) {
        const list = this.listRef.current
        list.scrollTop = list.scrollHeight - snapshot
      }
    }
    ```

## ErrorBoundray

- **getDerivedStateFormError()**

  - 에러 상황에서 실행되는 메서드
  - `반드시 state값을 반환해야 함`
  - `render단계`에서 실행
  - 렌더링 과정에서 호출되는 메서드이므로, 부수 효과를 발생시키면 안됨

  ```tsx
    ...
    static getDerivedStateFormError(error : Error) {
      return {
        hasError : true,
        errorMessage : error.toString()
      }
    }

    render() {
      if(this.state.hasError) {
        return (
          <div>
            <h1>에러가 발생했습니다.</h1>
            <p>{this.state.errorMessage}</p>
          </div>
        )
      }

      return this.props.children
    }
  ```

  - **componentDidCatch()**

    - `자식 컴포넌트에서 에러가 발생`했을 때 실행
    - `getDerivedStateFormError에서 에러를 잡고 state를 결정한 후 실행`
    - `commit 단계`에서 실행

    ```tsx
      ...
      componentDidCatch(error : Error, info : ErrorInfo) {
        console.log(error)
        console.log(info)
      }
    ```

  ### 주의할 점

  componentDidCatch는 개발 모드와 프로덕션 모드가 다르게 동작함

  - 개발 모드
    - 에러가 발생하면 window까지 전파

  - 프로덕션 모드
    - 잡히지 않은 에러만 window까지 전파

## React.Component vs React.PureComponent

> React.Component와 React.PureComponent의 차이는 컴포넌트의 리렌더링 최적화 방식에 있음

- React.Component
  - 기본적으로 React.Component는 shouldComponentUpdate 메서드가 구현되지 않은 상태임.
  - 상태(state)나 속성(props)이 변경되면 항상 리렌더링이 발생함.
  - 최적화를 위해 shouldComponentUpdate 메서드를 오버라이드하여 리렌더링을 제어할 수 있음.

- React.PureComponent
  - React.PureComponent는 shouldComponentUpdate 메서드가 내장된 형태로 제공됨.
  - 이 메서드는 **얕은 비교(shallow comparison)**를 통해 props와 state가 변경되지 않았다면 리렌더링을 하지 않음.
  - 객체나 배열과 같은 참조형 데이터가 깊은 구조일 경우 정확히 비교하지 못할 수 있으므로, 객체의 불변성을 유지해야 PureComponent가 효과적임.

  ```jsx
  class MyPureComponent extends React.PureComponent {
    render() {
      console.log('Render MyPureComponent');
      return <div>{this.props.text}</div>;
    }
  }
  ```

  > React.PureComponent를 사용하면 불필요한 리렌더링을 줄일 수 있지만, 경우에 따라 얕은 비교로 인한 오작동이 발생할 수 있으므로 주의가 필요함.

## 클래스 컴포넌트의 한계

- 데이터 흐름을 추적하기 어려움
- 애플리케이션 내부 로직의 재사용이 어려움
- 기능이 많아질수록, 컴포넌트의 크기가 커짐
- 클래스는 함수에 비해 상대적으로 어려움
- 코드 크기의 최적화가 어려움
- 핫 리로딩을 하는데 상대적으로 불리함

> 핫 리로딩(hot reloading) :코드에 변경 사항이 발생했을 때 앱을 다시 시작하지 않고서도 해당 변경된 코드만 업데이트해 변경 사항을 빠르게 적용하는 기법