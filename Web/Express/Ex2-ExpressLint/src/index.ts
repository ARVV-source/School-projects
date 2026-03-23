import express, {Request, Response, Express} from 'express';
const app : Express= express()
const port : number | string = process.env["PORT"] || 3000;
app.get('/', (req : Request, res : Response) => {res.send('Hola mundo')});
app.listen(port, ()=>{console.log()})

const list = [true, false]
function rev(y : any) {
  return (y.map((x:boolean)=>!x))
}
const newlist = rev(list)

app.get('/rev', (req, res)=>{
  res.send(`Lista anterior: ${list} Nueva lista: ${newlist}`)})

app.get('/saludo', (req, res) => {
  res.send("hola")})

app.get('/saludo/:nombre', (req, res) => {
  console.log(req)
  res.send(`hola ${req.params.nombre}`)
})

const cal = [10,9,8,3,2,6,8,8,10,8]
app.get('/califs', (req, res) => {
  res.send(cal)
})

app.get('/califs/:index', (req, res) => {
  res.send(cal[Number(req.params["index"])])
})