import React, {useEffect, useState} from "react";
import {View, Text, Button,TextInput} from "react-native"

export default function IndexScreen() {
  const [counter, setCounter] = useState(0);
  const increment = (()=>setCounter(counter+1));
  const [texto, setTexto] = useState("");

  useEffect(()=> {
    console.log({counter})
  }, [texto])
  useEffect(() => {
    console.log({texto})
  }, [texto])
  
  return (
    <View>
      <Text> Contador: {counter}</Text>
      <Button title="incrementar" onPress={increment}></Button>
      <TextInput
      onChangeText={(input)=>{setTexto(input)}}></TextInput>
    </View>
  )
}