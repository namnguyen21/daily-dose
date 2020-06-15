import React from "react";
import styled from "styled-components";

const Wrapper = styled.div`
  margin: 5rem auto 0 auto;
  @media (min-width: 800px) {
    width: 70vw;
  }
  @media (max-width: 800px) {
    width: 95vw;
  }
`;

export default function Container(props) {
  return <Wrapper>{props.children}</Wrapper>;
}
