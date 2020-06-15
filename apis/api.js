const express = require("express");
const router = express.Router();
const mongojs = require("mongojs");

const db = mongojs("dailydose");

const news = db.collection("news");
const sports = db.collection("sports");
const media = db.collection("media");

//route for home page news feed
router.get("/news", (req, res) => {
  news.find((err, response) => {
    if (err) throw err;
    else {
      res.json(response);
    }
  });
});

router.get("/sports", (req, res) => {
  sports.find((err, response) => {
    if (err) throw err;
    else {
      console.log(response)
      res.json(response);
    }
  });
});

router.get("/media", (req, res) => {
  media.find((err, response) => {
    if (err) throw err;
    else {
      res.json(response);
    }
  });
});

module.exports = router;
