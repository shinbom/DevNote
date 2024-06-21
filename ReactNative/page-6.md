# 이벤트 처리하기

```tsx
import {useState} from 'react'
import { StatusBar } from 'expo-status-bar';
import { Button, StyleSheet, Text, View, TextInput } from 'react-native';

export default function HomeScreen() {
  const [enteredGoalText, setEnteredGoalText] = useState('')

  function goalInputHandler(enteredText : string) {
    setEnteredGoalText(enteredText)
  }

  function addGoalHandler() {
    console.log('enteredGoalText', enteredGoalText)
  }

  return (
    <View style={styles.appContainer}>
      <View style={styles.inputContainer}>
        <TextInput
          placeholder="Your course goal!"
          style={styles.textInput}
          onChangeText={goalInputHandler}
        />
        <Button title="Add Goal" onPress={addGoalHandler}/>
      </View>
      <View style={styles.goalsContainer}>
        <Text>List Of Goal</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  appContainer : {
    flex :1,
    paddingTop : 50,
    paddingHorizontal : 16
  },
  inputContainer : {
    flex : 1,
    flexDirection : 'row',
    justifyContent : 'space-between',
    alignItems : 'center',
    marginBottom : 24,
    borderBottomWidth : 1,
    borderBottomColor : '#ccc',
  },
  textInput : {
    borderWidth : 1,
    borderColor : '#ccc',
    width : '50%',
    marginRight: 8,
    padding : 8
  },
  goalsContainer : {
    flex : 5
  }
});

```

React Native에는 onClick이벤트가 없고, 대신 `onPress`가 있다.

그리고 onChange시, 기본적으로 전달되는 매개변수로 `enteredText`가 있다.