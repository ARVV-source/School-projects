module Main exposing (..)
import Html
import Html.Attributes
import Html.Events
import Browser

type alias Model = 
        {currentNum : Int}
init : Model
init = 
        { currentNum = 0 }

type Msg
  = Increment
  | Decrement

update : Msg -> Model -> Model
update msj model =
  case msj of 
    Increment ->
      {model | currentNum = model.currentNum + 1}
    Decrement ->
      {model | currentNum = model.currentNum - 1}

view : Model -> Html.Html Msg
view model =
  Html.div [Html.Attributes.style "display" "flex" ] [
    Html.button [Html.Events.onClick Decrement] [Html.text "-"],
    Html.p [] [Html.text (String.fromInt model.currentNum)],
    Html.button [Html.Events.onClick Increment] [Html.text "+"]
  ]

type alias Cinco =
  {count : Int}
estado : Cinco
estado =
  {count = 10}

type Nmsg
  = Nincrement
  | Ndecrement
  | Ma20
actualizacion : Nmsg -> Cinco -> Cinco 
actualizacion msg model =
  case msg of
    Nincrement ->
      {model | count = model.count + 5}
    Ndecrement ->
      {model | count = model.count - 5}
    Ma20 ->
      {model | count = model.count + 20}
  
vista : Cinco -> Html.Html Nmsg
vista model =
  Html.div [Html.Attributes.style "display" "flex" ] [
    Html.button [Html.Events.onClick Ndecrement] [Html.text "-"],
    Html.p [] [Html.text (String.fromInt model.count)],
    Html.button [Html.Events.onClick Nincrement] [Html.text "+"],
    Html.button [Html.Events.onClick Ma20] [Html.text "+20"]
  ]

main : Program () Cinco Nmsg
main = Browser.sandbox {init=estado, update=actualizacion, view=vista}
