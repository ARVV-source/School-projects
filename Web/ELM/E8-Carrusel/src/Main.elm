module Main exposing (..)
import Html
import Html.Attributes
import Html.Events
import Browser

type Event
  = Left
  | Right

type alias Photos =
  {currentPhoto : String}

type alias Images = {
  first : String,
  other : List String}

images : Images
images = {
  first = "a.png",
  other = ["b.png", "c.png"]}

view : Html.Html msg
view  =
  Html.div [Html.Attributes.style "display" "flex", Html.Attributes.style "align-Items" "center"] [
    Html.button [] [Html.text "<"]
    ,Html.img [Html.Attributes.src ""] []
    ,Html.button [] [Html.text ">"]
  ]

init : Photos
init = {currentPhoto = images.first}

update : Event -> Photos -> Photos
update event model = 
  case event of 
    Right -> {model | currentPhoto = getNext (images.first::images.other) model.currentPhoto}
    Left -> {model | currentPhoto = getPrev (images.first::images.other) model.currentPhoto}

getNext : List String -> String -> String
getNext list current = 
  case list of
    x::y::ys ->
      if x == current then
        y
      else
        getNext (y::ys) current
    _ -> images.first

getPrev : List String -> String -> String
getPrev list current = 
  case list of
    x::y::ys ->
      if y == current then
        x
      else
        getPrev (y::ys) current
    _ -> images.other --