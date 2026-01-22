module Helper exposing (..)

isEmpty : List a -> Bool
isEmpty x =
  case x of 
    [] -> True
    _ -> False

head : List Int -> Int
head lista = 
  case lista of
    [] -> -100
    x :: _ -> x
