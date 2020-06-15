import React from "react";
import styled from "styled-components";
import LazyLoad from "react-lazyload";

const CardContainer = styled.div`
  width: 25rem;
  border-radius: 2px;
  margin: 1rem;
  transition: all 0.5s;
  &:hover {
    transform: scale(1.05);
  }
  overflow-y: visible;
`;

const CardImage = styled.img`
  width: 100%;
  height: 20rem;
`;
const CardBody = styled.div`
  width: 25rem;
  font-size: 1.6rem;
`;

const CardContent = styled.p`
  max-width: 30rem;
  max-width: 30rem;
  font-size: 1.6rem;
  color: ${(props) =>
    props.dark ? props.theme.palette.white : props.theme.palette.grey};
  word-break: break-word;
`;

const Iframe = styled.iframe`
  width: 100%;
  height: 20rem;
  border: none;
`;

export default function Card({ data, dark }) {
  return (
    <a
      href={data.url}
      target="_blank"
      rel="noopener noreferrer"
      style={{ textDecoration: "none" }}
    >
      <CardContainer>
        {data.image || data.thumbnail ? (
          <LazyLoad overflow={true}>
            <CardImage
              alt={data.title}
              src={data.image ? data.image : data.thumbnail}
            />
          </LazyLoad>
        ) : (
          <LazyLoad>
            <Iframe src={data.embed_url} />
          </LazyLoad>
        )}
        <CardBody>
          <CardContent dark={dark}>{data.title}</CardContent>
        </CardBody>
      </CardContainer>
    </a>
  );
}
