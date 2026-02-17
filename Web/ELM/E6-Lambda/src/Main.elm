module Main exposing (..)

double : List Int -> List Int
double list =
  List.map (\x -> x*2) list