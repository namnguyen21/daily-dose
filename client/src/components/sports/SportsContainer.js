import React, { useEffect, useState } from "react";
import styled from "styled-components";
import axios from "axios";
import LazyLoad from "react-lazyload";

import Row from "../cardrow/Row";

const Container = styled.div`
  width: 100%;
`;

export default function SportsContainer({ dark }) {
  const [apiResult, setApiResult] = useState([]);
  useEffect(() => {
    axios.get("/api/sports").then((response) => {
      setApiResult(response.data);
    });
  });
  return (
    <Container>
      {apiResult
        ? apiResult.map((el) => (
            <LazyLoad once>
              <Row dark={dark} data={el} />
            </LazyLoad>
          ))
        : null}
    </Container>
  );
}
