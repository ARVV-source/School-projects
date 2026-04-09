import express, { Request, Response, Express } from "express";
import mysql, {
  PoolOptions,
  Connection,
  RowDataPacket,
  FieldPacket,
} from "mysql2/promise";

interface Calif extends RowDataPacket {
  id: Number;
  name: String;
  grade: Number;
}

const app: Express = express();

const port: number = Number(process.env["MYPORT"]) || 3000;

const access: PoolOptions = {
  host: process.env["DB_HOST"] || "",
  port: Number(process.env["DB_PORT"]) || 0,
  user: process.env["DB_USER"] || "",
  password: process.env["DB_PASSWORD"] || "",
  database: process.env["DB_NAME"] || "",
};

const conn: Connection = mysql.createPool(access);

app.get("/", async (req: Request, res: Response) => {
  try {
    const resultDb = await conn.query("SELECT 1 + 1 AS 'test'");
    res.send(resultDb);
  } catch (error) {
    console.log(error);
    res.send("Ha habido un error en la base de datos");
  }
});

app.get("/info", async (req: Request, res: Response) => {
  try {
    const dbInfo: [Calif[], FieldPacket[]] =
      await conn.query(`SELECT * FROM califs`);
    res.send(dbInfo[0]);
  } catch (error) {
    console.log(error);
    res.send("Ha habido un error en la base de datos");
  }
});

app.get("/info/:index", async (req: Request, res: Response) => {
  try {
    const dbInfo: [Calif[], FieldPacket[]] = await conn.query(
      `SELECT * FROM califs WHERE id=?`,
      req.params["index"],
    );
    res.send(dbInfo[0]);
  } catch (error) {
    console.log(error);
    res.send("Ha habido un error en la base de datos");
  }
});

app.listen(port, () => {
  console.log(`Escuchando en puerto ${port}`);
  console.log("http://localhost:3010");
});
