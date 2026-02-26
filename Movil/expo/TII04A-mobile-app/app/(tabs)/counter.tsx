import React, { useState } from "react";
import {View, Text, Pressable, StyleSheet} from "react-native"

export default function IndexScreen() {
  const [value, setValue] = useState <number>(0);
  const increment = () => {setValue(value+1)}
  const decrement = () => {setValue(value-1)}
  return (
    <View style={styles.cont}>
      <View style={styles.textCont}>
        <Text style={styles.text}> {value} </Text>
      </View>
      <View style={styles.btnCont}>
        <Pressable onPress={decrement} style={styles.increment}>
          <Text style={styles.button}>
            -
          </Text>
        </Pressable>
        <Pressable onPress={increment} style={styles.decrement}>
          <Text style={styles.button}>
            +
          </Text>
        </Pressable>
      </View>
    </View>
  )
};
const styles = StyleSheet.create ({
  cont : {
    flex: 1,
  },
  textCont : {
    alignItems : "center",
    justifyContent : "center",
    flex: 1
  },
  text : {
    fontSize : 100,
    alignItems : "center",
    justifyContent : "center",
  },
  btnCont : {
    flexDirection: "row",
    justifyContent : "space-between"

  },
  increment : {
    backgroundColor : "orange",
    borderRadius : 8,
    padding : 8,
    justifyContent : "flex-start"
  },
  decrement : {
    backgroundColor : "orange",
    borderRadius : 8,
    padding : 8
  },
  button : {
    fontSize : 30
  }
});