module Main exposing (main)
import Html
import Html.Events
import Browser

main : Program () Model Msg
main = Browser.sandbox {view = view, init = init, update = update }

type alias Model = {
  currentNum : Int
  }

init : Model 
init = {
  currentNum = 0
  }

type Msg = 
  Set0
  |Set1
  |Set2
  |Set3
  |Set4
  |Set5
  |Set6
  |Set7
  |Set8
  |Set9
  |Set10

view : Model -> Html.Html Msg
view model=
  Html.div [] [
    Html.p [] [Html.text (String.fromInt model.currentNum)],
    createButton Set0 "0",
    createButton Set1 "1",
    createButton Set2 "2",
    createButton Set3 "3",
    createButton Set4 "4",
    createButton Set5 "5",
    createButton Set6 "6",
    createButton Set7 "7",
    createButton Set8 "8",
    createButton Set9 "9",
    createButton Set10 "10"
  ]

createButton : Msg -> String -> Html.Html Msg
createButton msg num=
  Html.button [Html.Events.onClick msg] [Html.text num]

update : Msg -> Model -> Model
update msg model =
  case msg of 
    Set0 -> 
      { model | currentNum = 0 }
    Set1 -> 
      { model | currentNum = 1 }
    Set2 -> 
      { model | currentNum = 2 }
    Set3 -> 
      { model | currentNum = 3 }
    Set4 -> 
      { model | currentNum = 4 }
    Set5 -> 
      { model | currentNum = 5 }
    Set6 -> 
      { model | currentNum = 6 }
    Set7 -> 
      { model | currentNum = 7 }
    Set8 -> 
      { model | currentNum = 8 }
    Set9 -> 
      { model | currentNum = 9 }
    Set10 -> 
      { model | currentNum = 10 }