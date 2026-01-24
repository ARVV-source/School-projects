module Main exposing (..)

canBuyAlcohol : List Int -> List Bool
canBuyAlcohol edades =
  List.map buyAlc edades 

buyAlc : Int -> Bool
buyAlc age =
  if age > 17 then
    True
  else
    False

indAllUpperCase : String -> String
indAllUpperCase name =
  String.toUpper name

indApproveCourse : Float -> String
indApproveCourse grade =
  if grade >= 6 then
    "Approve"
  else
    "not approved"

ageList : List Int
ageList = [16,11,18,22,23,13]

nameList : List String
nameList = ["emilio", "juan"]

gradeList : List Float
gradeList = [2,6,4,9,2]