module Main exposing (..)


lang : List {name : String, releaseYear : Int, currentVersion: String}
lang = [
  {name = "python", releaseYear = 1991, currentVersion = "3.15" },
  {name = "java", releaseYear = 1995, currentVersion = "Java 25" }
  ]

languageNames :  List {name : String, releaseYear : Int, currentVersion: String} -> List String
languageNames list =
  List.map .name list 

users : List {name : String, uType : String}
users = [
  {name = "Juan Perez", uType = "Student"},
  {name = "Mitsiu", uType = "Teacher"},
  {name = "Amauro", uType = "Student"}]

onlyStudents : List {name : String, uType : String} -> List String
onlyStudents list = 
  List.map isStudent list

isStudent : {name : String, uType : String} -> String
isStudent juan =
  if .uType juan == "Student" then
    .name juan
  else 
    ""

games : List {title : String, releaseYear : Int, available : Bool, downloads : Int, genres : List String}
games = [
  {title = "COD", releaseYear = 2006, available = False, downloads = 10, genres = ["action", "Shooter"]},
  {title = "Zelda", releaseYear = 2008, available = False, downloads = 5, genres = ["action", "Adventure"]}]

type alias Videogame =
  {title : String, releaseYear : Int, available : Bool, downloads : Int, genres : List String}
getVideogameGenre : List Videogame -> List (List String)
getVideogameGenre gameList =
  List.map .genres gameList