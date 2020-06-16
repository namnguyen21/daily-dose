import React, { useState, useEffect } from "react";
import axios from "axios";
import styled from "styled-components";
import NewsWrapper from "./NewsCard";

const Wrapper = styled.div`
  width: 100%;
  @media (min-width: 800px) {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    flex-wrap: wrap;
  }
  @media (max-width: 800px) {
    display: flex;
    flex-direction: column;
  }
`;

export default function NewsContainer({ dark }) {
  const [apiResult, setApiResult] = useState([]);

  useEffect(() => {
    console.log("getting information");
    axios.get("/api/news").then((response) => {
      setApiResult(response.data);
    });
  }, [dark]);
  return (
    <Wrapper>
      {apiResult
        ? apiResult.map((el) => {
            return <NewsWrapper dark={dark} key={el._id} data={el} />;
          })
        : null}
    </Wrapper>
  );
}
