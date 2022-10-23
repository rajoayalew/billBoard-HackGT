var express = require('express');
var router = express.Router();

const sqlite3 = require('sqlite3').verbose();
let db = new sqlite3.Database('data.db');

/* GET home page. */
router.get('/', function(req, res, next) {
  console.log(req)
  res.send({msg: "hi"})
});

router.post('/', function(req, res, next) {
  var data = req.body;
  var Procedure = Number(data.Procedure);
  var Cost = Number(data.Cost);
  var State = data.State;
  var Gender = data.Gender;
  var Age = Number(data.Age);

  output = [Procedure, Cost, Age, Gender, State];


  // let query = "INSERT INTO entries VALUES(NULL," +
  //             Procedure + "datetime('now', 'localtime')," +
  //             Cost + "," + Age + "," + Gender + "," + State + ")"
  //let query = "INSERT INTO entries VALUES(NULL, ?, datetime('now', 'localtime'), ?, ?, ?, ?)"
  // db.all(query, [output], (err, rows) => {
  //     console.log("FIRST ROW:", rows[0]);
  //   });

  db.serialize(function() {
    var stmt = db.prepare("INSERT INTO entries VALUES(NULL, ?, datetime('now', 'localtime'), ?, ?, ?, ?)");
    stmt.run(Procedure, Cost, State, Gender, Age);
    stmt.finalize();
  
    db.each("SELECT * FROM entries", function(err, row) {
        console.log(row[1]);
    });
  });
  

  // db.run(query, [output],function(err) {
  //   if (err) {
  //     return console.log(err.message);
  //   }
  // });

  res.send({msg: "hi"})
});

db.close();

module.exports = router;
