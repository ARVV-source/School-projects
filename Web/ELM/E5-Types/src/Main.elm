module Main exposing (..)

type GradeStatus = Approved | Failed | Pending

categoricalGradeInd : Float -> GradeStatus
categoricalGradeInd calif = 
  if 0 > calif then
    Pending
  else if calif > 7 then
    Approved
  else
    Failed

categoricalGrade : List Float -> List  GradeStatus
categoricalGrade list =
  List.map categoricalGradeInd list
  
type AirPlaneStatus = OnTime | Boarding | Delayed | Cancelled

airportAction : AirPlaneStatus -> String
airportAction status =
  case status of
    Cancelled ->
      "Pedir Reembolso"
    Delayed ->
      "Esperar"
    OnTime ->
      "Esperar"
    Boarding ->
      "Buscar boleto"

airplaneScheduleAction : List AirPlaneStatus -> List String
airplaneScheduleAction list =
  List.map airportAction list