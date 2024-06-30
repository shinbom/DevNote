# FlatList

스크롤을 실현하는 컴포넌트

보이는 항목만 렌더링하고, 화면 밖의 항목은 사용자가 스크롤 해야 로딩 및 렌더링이 됨.

```tsx
<View style={styles.goalsContainer}>
  <FlatList
    data={courseGoals}
    renderItem={(itemData) => {
      return (
        <View style={styles.goalItem}>
          <Text style={styles.goalText}>{itemData.item.text}</Text>
        </View>
      )
    }}
    keyExtractor={(item, index) => {
      return item.id
    }}
    alwaysBounceVertical={false}
  />
</View>
```

flatList는 자체적으로 list의 항목에 대한 객체를 가지고 있다.

이 객체 안에는 index도 함께 있어, key에 제공해도 되고, 키가 될 객체를 만들어도 된다.

```tsx
  function addGoalHandler() {
    setCourseGoals(currentCouseGoals => [
      ...currentCouseGoals,
      {text : enteredGoalText, id : Math.random().toString() }
    ])
  }
```

그리고 key를 마드는 `keyExtractor`함수도 있다.
