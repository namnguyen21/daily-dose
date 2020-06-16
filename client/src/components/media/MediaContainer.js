import React, { useEffect, useState } from "react";
import styled from "styled-components";
import axios from "axios";

import Row from "../cardrow/Row";

const Container = styled.div`
  width: 100%;
`;

export default function MediaContainer({dark}) {
  const [api, setApi] = useState([]);

  useEffect(() => {
    axios.get("/api/media").then(({ data }) => {
      setApi(data);
      console.log(data)
    });
  }, []);

  return (
    <Container>
      {api ? api.map((result) => <Row dark={dark} data={result} />) : null}
    </Container>
  );
}
