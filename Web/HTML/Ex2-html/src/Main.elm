module Main exposing (..)
import Html
import Html.Attributes
main : Html.Html msg
main =
  Html.div [Html.Attributes.class "content", Html.Attributes.id "landing" ] [
    Html.h1 [] [Html.text "Nested h1"],
    Html.a [Html.Attributes.href "https://google.com"] [Html.strong [] [Html.text "Matenme porfavor"]] ]
