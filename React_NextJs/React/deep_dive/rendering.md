# 렌더링

> 리액트 애플리케이션 트리 안에 있는 모든 컴포넌트들이 현재 자신이 가지고 있는 props와 state의 값을 기반으로 어떻게 UI를 구성하고 이를 바탕으로 DOM 결과를 브라우저에 제공할 것인지 계산하는 일련의 과정

## 리책트 렌더링이 일어나는 이유

- 최초 렌더링 

  - 리액트는 브라우저에 정보를 제공하기 위해 최초 렌더링을 수행

- 리렌더링 : 최초 렌더링이 발생한 이후 발생하는 모든 렌더링

  - 클래스형 컴포넌트
    - setState가 실행되는 경우
    - forceUpdate가 실행되는 경우

  - 함수형 컴포넌트
    - useState()의 두 번째 배열 요소인 setter rk tlfgodehlsms ruddn
    - useReducer()의 두 번째 배열 요소인 setter가 실행되는 경우
    - useReducer()의 두 번째 배열 요소인 dispatch가 실행되는 경우
    - 컴포넌트의 key props가 변경되는 경우

      > **key가 필요한 이유**
      > - 리렌더링이 발생하는 동안 형제 요소 사이의 동일한 요소를 식별하는 값
      > - 리렌더링이 발생하면 current 트리와 workInprogress트리 사이에 어떠한 변경값이 있었는지 구별해야 하는데 이 구별하는 값
      > - key가 없는 경우, 파이버 내부의 index만을 기준으로 판단함
      
  - prop가 변경되는 경우
    - 부모로부터 전달받는 값인 props가 변경되면 자식 컴포넌트에서도 리렌더링이 발생
  - 부모컴퍼넌트가 리렌더링 될 경우


## 렌더링 프로세스

- 컴포넌트의 루트부터 아래쪽으로 내려가며 업데이트가 필요하다고 지정되어있는 모든 컴포넌트를 찾음
- 업데이트가 필요한 컴포넌트를 발견하면 아래와 같은 동작이 발생된다.
  - 함수형 컴포넌트
    - FuncionalComponent() 호출 후, 결과물 저장

  - 클래스형 컴포넌트
    - render()함수 실행

  ---

  - JSX문법이 자바스크립트 문법으로 실행되며, React.creatElement() 호출하는 구문으로 변경
  - 브라우저나 UI 구조를 설명할 수 있는 자바스크립트 객체를 반환

## 렌더와 커밋

- 렌더 단계(Render Phase)

  - 컴포넌트를 렌더링하고 변경사항을 계산하는 모든 작업
  - 렌더링 프로세스에서 컴포넌트를 실행`(render() 또는 return)`해 이전 가상 DOM과 비교하여 변경이 필요한 컴포넌트를 체크하는 단계
    - 비교하는 것
      - type
      - props
      - key
      
      > 위 세가지 중, 하나라도 변경된 것이 있으면 변경이 필요한 컴포넌트로 체크

- 커밋 단계(Commit Phase)

  - 렌더 단계의 변경사항을 DOM에 적용하여, 사용자게에 보여주는 과정
  - 커밋이 끝난 후 `브라우저 렌더링이 발생`
  - DOM 노드 및 인스턴스를 가르키도록 리액트 내부 참조를 업데이트

  - 클래스형 컴포넌트`(생명주기 개념이 있음)`
    - componentDidMount, componentDidUpdate 메서드 호출
  - 함수형 컴포넌트
    - useLayoutEffect훅 호출

  > **리액트의 렌더링이 일어난다고 해서 무조건 DOM 업데디트가 일어나지 않음**
  > <br/>
  > <br/>
  > 변경사항을 감지할 수 없다면 커밋단계가 생략되어 DOM업데이트가 일어나지 않음 

## 정리

리액트 렌더링은 동기식으로 동작함.<br/>
렌더링 시간이 길어지면, 애플리케이션 성능 저하로 이어지고, 결과적으로 그 시간만큼 브라우저의 다른 작업을 지연시킬 가능성이 있음.

하지만, 비동기적으로 동작하게 되면 사용자에게 혼란을 줄 수 있음

`리액트 18`에서는 의도된 우선순위대로 컴포넌트를 렌더링해 최적화 할 수 있는 비동기렌더링(동시성 렌더링)이 도입됨.

> **동시성 렌더링**
> 렌더단계가 비동기로 작동하여 특정 렌더링의 우선순위를 낮추거나, 필요하면 중단 혹은 재시작, 포기 할 수 있음.