# JSX

> JSX는 자바스크립트 표준 문법이 아닌, 페이스북이 임의로 만든 새로운 문법이기 떄문에 반드시 `트랜스파일러`를 거쳐야 자바스크립트 런타임이 이해할 수 있는 자바스크립트 코드로 변환됨.

## JSX의 구성요소

1. JSXElement
2. JSXAttribute
3. JSXChilderen
4. JSXStrings


### JSXElement

HTML 요소(element)와 비슷한 역할

1. JSXOpeningElement : 요소의 시작을 알림

```jsx
<JSXElement JSXAttributes(optional)>
```

2. JSXClosingELement : 요소의 종료를 알림

```jsx
</JSXElement>
```

3. JSXSelfClosingElement : 요소가 시작되고, 스스로 종료되는 형태

```jsx
<JSXElement JSXAttributes(optional)/>
```

4. JSXFragment : 아무런 요소가 없는 형태

```jsx
<>
JSXChildren(optional)
</>
```

> 요소명은 대문자로 시작하여, HTML 태그명과 사용자가 만든 태그명을 구분짓기 위함이다.

### JSXElementName

1. JSXIdentifier
    - JSX 내부에서 사용할 수 있는 식별자
    - 자바스크릭트 식별자 규칙과 동일함.

    ```jsx
      // 가능
      function Valid1() {
        return <$></$>
      }

      function Valid2() {
        return <_></_>
      }

      // 불가능
      function InValid() {
        return <1></1>
      }
    ```

2. JSXNamespacedName
    - JSXIdentifier:JSXIdentifier의 조합
    - :로 묶을 수 있는 것은 한개뿐

    ```jsx
      // 가능
      function Valid() {
        return <foo:bar></foo:bar>
      }

      // 불가능
      function InValid() {
        return <foo:bar:barz></foo:bar:barz>
      }
    ```

3. JSXMemberExpression
    - JSXIdentifier.JSXIdentifier의 조합
    - .를 여러개 이어서 하는 것도 가능
    - 단, JSXNamesSpacedName과 이어서 사용하는 것은 불가능

    ```jsx
      // 가능
      function Valid() {
        return <foo.bar></foo.bar>
      }

      function Valid2() {
        return <foo.bar.barz></foo.bar.barz>
      }

      // 불가능
      function InValid () {
        return <foo:bar.barz></foo:bar.barz>
      }
    ```

### JSXAttributes

JSXElement에 부여할 수 있는 속성(Optional)

1. JSXSpreadAttributes
    - 자바스크립트의 전개 연산자와 동일한 역할

2. JSXAttributes
    - 속성을 나타내는 키와 값으로 표현
    - 키는 JSXAttributeName
    - 값은 JSXAttributeValue

    #### JSXAttributeValue에 할당할 수 있는 값들

    - 큰따옴표 or 작은따옴표로 구성된 문자열
    - AssignmentExpression(값을 변수나 객체의 속성에 할당하는 표현식)
    - JSXElement

    ```jsx
      function Child({attribute}) {
        return <div>{attribute}</div>
      }

      export default function App() {
        return (
          <div>
            <Child attribute=<div>Hello</div> />
          </div>
        )
      }
    ```

    > props에 `<Child attribute={<div></div>} />`에서 `{   }`로 감싸는 것은 태그가 포함된  JSX구문을 좀 더 읽기 쉽게 만들기 위한 `prettier`의 규칙이다.

    - JSXFragment


### JSXChildren

JSXElement의 자식 값

1. JSXChild
    - JSXChildren을 이루는 기본 단위

    #### JSXChild에 할당할 수 있는 값들

    - JSXText 

      - `{, <, >, }`을 제외한 문자열 (JSX 다른 문법과 혼동을 줄 수 있음)

        ```jsx
          // 위 문자열을 사용하기 위해서는 아래와 같이 해야 한다.
          function Valid () {
            return <>{'{} <>'}</>
          }
        ```

    - JSXElement
    - { JSXChildExpression (optional) }

      ```jsx
        // 'foo'라는 문자열이 출력됨`.
        export default function App() {
          return (
            <>
              {( () => 'foo')()}
            </>
          )
        }
      ```

### JSXStrings

HTML에서 사용가능한 문자열은 모두 JSXStrings에서도 가능함.

```jsx
<button>\</button>
```
