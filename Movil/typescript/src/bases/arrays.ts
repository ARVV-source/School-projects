import type {Animal} from "./objects"

const perro : Animal = {
  name: "Perrito",
  type: "perro",
  age: 2,
  ownerName: "Juan",
  sound: () => {
    console.log("Guau")
  }
}

const gato : Animal = {
  name: "Miaumiau",
  type: "gato",
  age: 1,
  ownerName: "Juan tambien",
  sound: () => {
    console.log("miau")
  }
}

const pet : Animal[] = []
pet.push(perro, gato)

console.log(pet[1].name)