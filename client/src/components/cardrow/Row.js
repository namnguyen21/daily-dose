import React from "react";
import styled from "styled-components";
import Card from "./Card";

const RowContainer = styled.div`
  max-width: 100%;
  display: flex;
  flex-direction: row;
  overflow-x: scroll;
  overflow-y: visible;
`;

const Header = styled.h2`
  font-size: 2.5rem;
  color: ${(props) => props.theme.palette.orange};
  text-transform: uppercase;
`;

export default function Row({ data, dark }) {
  return (
    <div>
      <Header>{data.name}</Header>
      <RowContainer>
        {data ? data.data.map((el) => <Card dark={dark} data={el} />) : null}
      </RowContainer>
    </div>
  );
}
