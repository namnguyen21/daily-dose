import React, { useState } from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import { ThemeProvider } from "styled-components";

import NavBar from "./components/Nav/NavBar";
import Container from "./components/Container";
import NewsContainer from "./components/News/NewsContainer";
import SportsContainer from "./components/sports/SportsContainer";
import MediaContainer from "./components/media/MediaContainer";

const theme = {
  palette: {
    blue: "#3E82FC",
    orange: "#FE2C54",
    white: "#ffffff",
    grey: "#616161",
  },
};

export default function App({ darkMode }) {
  const [dark, setDark] = useState(false);

  const changeTheme = () => {
    setDark((dark) => !dark);
  };

  return (
    <ThemeProvider dark={dark} theme={theme}>
      <div
        style={{
          width: "100%",
          height: "100%",
          backgroundColor: dark ? "#1f1f1f" : "#ffffff",
          minHeight: "100vh",
          overflowX: "hidden",
        }}
      >
        <Router>
          <NavBar changeTheme={changeTheme} dark={dark} />
          <Container>
            <Route
              path="/"
              exact
              render={(props) => <NewsContainer {...props} dark={dark} />}
            />
            <Route
              path="/sports"
              exact
              render={(props) => <SportsContainer {...props} dark={dark} />}
            />
            <Route
              path="/media"
              exact
              render={(props) => <MediaContainer {...props} dark={dark} />}
            />
          </Container>
        </Router>
      </div>
    </ThemeProvider>
  );
}
