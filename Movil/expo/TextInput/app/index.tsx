import { Text, TextInput, View, StyleSheet} from "react-native";
import React, { useState } from "react";

export default function Index() {
  const [draft, setDraft] = useState("Aun no has escrito nada");
  const [text, setText] = useState("No hay mensajes");
  return (
    <View style = {styles.view}>
      <View >
        <TextInput
        value={draft}
        onChangeText = {(input) => setDraft(input)}
        onSelectionChange={() => setText("escribiendo...")}
        onSubmitEditing = {() => {
          setText(draft)
          setDraft("")
        }}
        //blurOnSubmit={false}
        style = {styles.cuadroText}
      />
      </View>
      <View style = {styles.textCont}>
        <Text>{text}</Text>
      </View>
    </View>
  )
}
const styles = StyleSheet.create ({
  cuadroText : {
    backgroundColor : "white",
    borderRadius : 20,
    padding : 10},
    

  textCont : {
    alignItems : "center",
    justifyContent : "center",
    height : 40},

  view : {
    flex : 1,
    alignItems : "center",
    justifyContent : "center",
    }
  })

  