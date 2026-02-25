import { Text, TextInput, View, StyleSheet} from "react-native";
import React, { useState } from "react";

export default function Index() {
  const [draft, setDraft] = useState("");
  const [text, setText] = useState("");
  
  return (
    <View>
      <View>
        <TextInput
        value={draft}
        onChangeText = {(input) => setDraft(input)}
        placeholder={"Aun no has escrito nada"}
        onSelectionChange={() => setText("escribiendo...")}
        onSubmitEditing = {() => {setText(draft)
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
    borderRadius : 20,
    backgroundColor : "white",
    height : 35,
    padding : 20},

    textCont : {
    alignItems : "center",
    justifyContent : "center",
    flex: 1}
  })
