const express = require("express");

const app = express();

app.use(express.urlencoded({ extended: true }));
app.use(express.json());
//app.use(express.static("public"));

const newsAPI = require("./apis/api");
app.use(newsAPI);

app.listen(3001, () => {
  console.log("Now listening on port 3001");
});
