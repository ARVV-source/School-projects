import { Stack } from "expo-router";

export default function RootLayout() {
  return (
  <Stack>
    <Stack.Screen name="login"></Stack.Screen>
    <Stack.Screen name="(tabs)"></Stack.Screen>
  </Stack>
  );
}
