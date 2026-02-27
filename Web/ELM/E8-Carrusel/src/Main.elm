module Main exposing (..)
import Html
import Html.Attributes
import Html.Events
import Browser

type Event
  = Left
  | Right

type alias Fotos =
  {currentPhoto : String}

view : Html. Html msg
view Event =
  Html.div [Html.Attributes.style "display" "flex"] [
    Html.button [Html.Event.onClick Left] [Html.text "<"]
    ,Html.img [Html.Attributes.src ""] []
    ,Html.button [Html.Event.onClick Right] [Html.text ">"]
  ]