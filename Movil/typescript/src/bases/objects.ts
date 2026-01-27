/* 
Que es un objeto en JS
En JavaScript, un objeto es un entidad independiente 
con propiedades y tipos. Compáralo con una taza, por 
ejemplo. Una taza es un objeto con propiedades. Una 
taza tiene un color, un diseño, un peso, un material
del que está hecha, etc

Como puedo acceder a la propiedad(key) de un objeto
Object.keysdevuelve un arreglo cuyos elementos son 
cadenas correspondientes a las propiedades enumerables
que se encuentran directamente en el object

Que es una interface y para que sirve Typescript
si w ahorita 

Como marco una propiedad como opcional
*/ 
//Objeto
interface User {
  printMessage: () => void //Funcion flecha
  nombre: String,
  age: number,
  isAdmin: boolean,
  address: {
    city: String
  }
  tags: String[]
}

const user : User = {
  printMessage: () => {
    console.log("Hola")
  },
  nombre: "Emilio",
  age: 19,
  isAdmin: false,
  address: {
    city: "Aguascalientes"
  },
  tags: ["hola"]
}

interface Animal {
  name: String,
  type: String,
  age: number,
  ownerName: String,
  sound : () => void
}

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

gato.sound()
perro.sound()