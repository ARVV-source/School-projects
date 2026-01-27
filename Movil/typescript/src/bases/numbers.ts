let productPriceOne : number = 10
let productPriceTwo : number = 15
let productPriceThree : number = 23
let productPriceFour : number = 76
let productPriceFive : number = 8

let total : number = productPriceOne+productPriceTwo+productPriceThree+productPriceFour+productPriceFive
let descuento : number = total*0.03
let totalDescuento : number = total-(total*0.03)

console.log("Producto: Leche ", productPriceOne)
console.log("Producto: Galletas ", productPriceTwo)
console.log("Producto: Miel ", productPriceThree)
console.log("Producto: popo ", productPriceFour)
console.log("Producto: qnsabe ", productPriceFive)
console.log("Total: ", total)
console.log("Descuento: ", descuento)
console.log("Total con descuento: ", totalDescuento)

let nombre : String = "Emilio"
console.log(`
Hola ${nombre}`
)