# Core Component(핵심 컴포넌트)

> Native 문법은 엄격하다.


## Text

문자열은 `<Text>`안에 있어야 한다.

```typescript
<Text> Hello World! </Text>
```


## View

View는 HTML에서 `div`와 유사한 역할이다.

일반적으로 콘텐츠를 담는 상자나 컨테이너 구축에 사용된다.

> HTML에는 section, article 이 있지만 React Native에는 View가 유일함.


## Button

```jsx
<Button title='Tap me!'/>
```

HTML과 같이 `<Button>Tab me!</Button>`가 아닌, title속성을 이용하여 텍스트를 출력한다.