var express = require('express');
var router = express.Router();

router.post('/', function(req, res, next) {
  var data = req.body;
  var Procedure = Number(data.Procedure);
  var Cost = Number(data.Cost);
  var State = data.State;
  var Gender = data.Gender;
  var Age = Number(data.Age);

  var output = [Procedure, Cost, State, Gender, Age]

  const sqlite3 = require('sqlite3').verbose();
  let db = new sqlite3.Database("data.db");

  db.run('INSERT INTO entries VALUES (NULL, ?, datetime("now", "localtime"), ?, ?, ?, ?)', output);

  db.close();
  res.send({msg: "bruh"});
  
});



module.exports = router;
