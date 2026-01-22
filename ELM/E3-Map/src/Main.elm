module Main exposing (..)

canBuyAlcohol : Int -> Bool
canBuyAlcohol age =
  if age > 17 then
    True
  else
    False

allUpperCase : String -> String
allUpperCase name =
  String.toUpper name

approveCourse : Float -> String
approveCourse grade =
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