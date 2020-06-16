const express = require("express");
const router = express.Router();
const mongojs = require("mongojs");
require('dotenv').config()

const db = mongojs(process.env.MONGODB_URI);

const news = db.collection("news");
const sports = db.collection("sports");
const media = db.collection("media");

//route for home page news feed
router.get("/api/news", (req, res) => {
  news.find((err, response) => {
    if (err) throw err;
    else {
      res.json(response);
    }
  });
});

router.get("/api/sports", (req, res) => {
  sports.find((err, response) => {
    if (err) throw err;
    else {
      res.json(response);
    }
  });
});

router.get("/api/media", (req, res) => {
  media.find((err, response) => {
    if (err) throw err;
    else {
      res.json(response);
    }
  });
});

module.exports = router;
