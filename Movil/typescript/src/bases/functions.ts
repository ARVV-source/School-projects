function exponente (e: number, b: number) : number {
  return b**e
}

function printMessage(msj: String) : void {
  console.log(msj)
}

function saludar (name: String) : String {
  return `Hola ${name}`
}

console.log(exponente(2,3))
printMessage("Hola")

console.log(saludar("Emilio"))