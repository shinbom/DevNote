# 핵심 컴포넌트 & 컴포넌트 스타일링

React Native는 HTML, CSS를 사용할 수 없음.

화면을 나타내는 중요한 React Native JSX로 `<View>`가 있다.

```jsx
<View style={styles.container}>
  <Text>Open up App.js to start working on your app!</Text>
</View>
```

[React Native Component API](https://reactnative.dev/docs/components-and-apis)

CoreComponent와 UI & Custom Component를 합쳐서 사용자 인터페이스를 구축함.

## Styles

CSS대신 Style을 사용함.

`Inline Styles`를 사용하거나, `StyleSheet Objects`를 사용함.

CSS프로퍼티와 비슷하지만 CSS 기능 일부를 지원함.