# ScrollView(스크롤)

> 스크롤을 위한 View를 명시적으로 선언해야 한다.

스크롤을 하기 위해서는, `<View>`가 아닌, `<ScrollView>`을 사용해야 한다.

```tsx
import { Button, StyleSheet, Text, View, TextInput, ScrollView} from 'react-native';


return (
  ...
  <View style={styles.goalsContainer}>
    <ScrollView>
      {courseGoals.map((goal : string, goalIndex : number) =>
        <View style={styles.goalItem} key={`goal_${goalIndex}`} >
          <Text style={styles.goalText}>{goal}</Text>
        </View>
      )}
    </ScrollView>
  </View>
  ...
)
```

스크롤이 가능한 높이는, 부모요소의 `<View>`가 정의함에 따라 View에 style을 지정해야 한다.

> iOS에서 스크롤이 튀어오르는 alwaysBouceVertical과 같은 속성도 제어할 수 있다.

[ReactNative - ScrollView](https://reactnative.dev/docs/scrollview)