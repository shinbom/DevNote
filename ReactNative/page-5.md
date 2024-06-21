# 레이아웃 플렉스 박스

```jsx
import { StatusBar } from 'expo-status-bar';
import { Button, StyleSheet, Text, View, TextInput } from 'react-native';

export default function HomeScreen() {
  return (
    <View style={styles.appContainer}>
      <View style={styles.inputContainer}>
        <TextInput placeholder="Your course goal!" style={styles.textInput}/>
        <Button title="Add Goal"/>
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

> 플레스 박스(Flext Box) CSS의 플렉스 박스와 유사하다.


