var express = require('express');
var router = express.Router();

const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('data.db');

/* GET home page. */
router.get('/', function(req, res, next) {
  console.log(req)
  res.send({msg: "hi"})
});

router.post('/', function(req, res, next) {
  console.log(req.body)

  
  let query = "SELECT * FROM entries";
  db.all(query, function (err, rows) {
    console.log("FIRST ROW:", rows[0]);
  });


  console.log(db);
  res.send({msg: "hi"})
});

module.exports = router;
