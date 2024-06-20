# 스타일링

스타일을 적용하는 두가지 방법은 다음과 같다.

1. 인라인 스타일(Inline Styles)

2. 스타일시트 객체(StyleSheet Object)

> 모든 요소에 지원되는 것은 아님.
> View, Text등에 지원됨.

[React Native Style](https://reactnative.dev/docs/style)

## 인라인 스타일(Inline Styles)

```jsx
  <Text style={{ margin : 16, borderWidth: 2, borderColor : 'red', padding: 16 }}>Hello World!</Text>
```

## 스타일시트 객체(StyleSheet Object)

```jsx
<Text style={styles.dummyText}>Hello World!</Text>

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  dummyText : {
    margin : 16,
    padding: 16,
    borderWidth : 2,
    borderColor : 'red'
  }
});
```