import React from "react";
import {Tabs} from "expo-router"

export default function TabLayout() {
  return (
    <Tabs
    screenOptions={{
        tabBarActiveTintColor: "#06847aff",
        tabBarInactiveTintColor: "gray",
        headerShown: false,
      }}>
      <Tabs.Screen name="home"></Tabs.Screen>
      <Tabs.Screen name="counter"></Tabs.Screen>
      <Tabs.Screen name="calculator"></Tabs.Screen>
      <Tabs.Screen name="poke-api"></Tabs.Screen>
    </Tabs>
  )
}