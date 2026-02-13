import { Text, View, StyleSheet} from "react-native";
/*import {Title} from "@/Components/Title"*/

export default function Index() {
  let name = "Emilio"

  return (
    <View style={styles.prederminado}>
      <Text style={styles.text}>Mi nombre es {name}</Text>
      <Text style={styles.prederminado}>AH</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  text : {
    color : "rgb(170, 23, 23)",
    fontSize : 30,
  },
  prederminado : {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    fontSize : 70,
  }
});