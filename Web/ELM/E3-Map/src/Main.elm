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


allUpperCase : List String -> List String
allUpperCase minus =
    List.map minMay minus


minMay : String -> String
minMay name =
    String.toUpper name


approveCourse : List Float -> List String
approveCourse calif =
    List.map compCalif calif


compCalif : Float -> String
compCalif grade =
    if grade >= 6 then
        "Approve"

    else
        "not approved"
