module Helper exposing (..)


double : number -> number
double inputNum =
    2 * inputNum


square : number -> number
square num =
    num ^ 2


greet : String -> String
greet nom =
    "Hola " ++ nom


above5 : number -> Bool
above5 num =
    num > 5


ifBoolTranslate : Bool -> String
ifBoolTranslate expr =
    if expr == True then
        "positivo"

    else
        "falso"


ifNumberSign : number -> String
ifNumberSign num =
    if num > 0 then
        "positivo"

    else if num == 0 then
        "neutral"

    else
        "negativo"


getNameById : Int -> String
getNameById id =
    case id of
        1 ->
            "Fernanda"

        2 ->
            "Miguel"

        3 ->
            "Juan"

        _ ->
            "Desconocido"


getGradeByName : String -> Float
getGradeByName name =
    case name of
        "Fernanda" ->
            9.4

        "Miguel" ->
            8.7

        "Juan" ->
            9.3

        _ ->
            0
