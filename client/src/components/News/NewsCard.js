import React, { useState } from "react";
import styled from "styled-components";
import ReactTooltip from "react-tooltip";

const Wrapper = styled.div`
  @media (max-width: 800px) {
    width: 80%;
    margin: auto;
  }
  width: 45%;
  padding: 1rem 1rem 5rem 1rem;
  position: relative;
  margin-bottom: 3rem;
`;

const Header = styled.h2`
  font-size: 2.5rem;
  font-weight: 400;
  color: ${(props) => props.theme.palette.blue};
  text-align: left;
`;

const Content = styled.div`
  width: 100%;
  max-height: 245px;
  overflow: auto;
`;

const NewsItem = styled.div`
  width: 100%;
  display: flex;
  &:not(:last-child) {
    border-bottom: solid 1px ${(props) => props.theme.palette.grey};
  }
`;

const NewsHeadline = styled.a`
  flex: 4;
  text-decoration: none;
  color: ${(props) =>
    props.dark ? props.theme.palette.white : props.theme.palette.grey};
  font-size: 1.6rem;
  line-height: 1.5;
  margin-left: 0.5rem;
  &:hover {
    color: ${(props) => props.theme.palette.blue};
  }
`;

const ViewMoreButton = styled.button`
  font-size: 1.6rem;
  color: ${(props) => props.theme.palette.orange};
  text-transform: uppercase;
  /* position: absolute;
  bottom: 1rem;
  right: 1rem; */
  position: absolute;
  right: 0;
  background: transparent;
  border: none;
  outline: none;
  &:hover {
    cursor: pointer;
  }
`;

const StyledTooltip = styled(ReactTooltip)`
  max-width: 30rem;
`;

export default function NewsWrapper(props) {
  const { name, data } = props.data;
  const [count, setCount] = useState(5);
  // const currentDisplay = data.splice(0, count);
  // console.log(data)

  const onClick = () => {
    if (count < 15) {
      setCount(15);
    } else {
      setCount(5);
    }
  };

  const renderCountNumArticles = () => {
    const currentDisplay = [];
    // account for there being less than 15 articles
    if (data.length < count) {
      for (let i = 0; i < data.length; i++) {
        currentDisplay.push(data[i]);
      }
    } else {
      for (let i = 0; i < count; i++) {
        currentDisplay.push(data[i]);
      }
    }
    return currentDisplay.map((el, index) => (
      <NewsItem
        style={{ margin: el.image ? "0.5rem 0" : null }}
        data-tip={el.title.trim()}
        key={index}
      >
        {el.title.split(" ").length > 10 ? (
          <StyledTooltip
            style={{ maxWidth: "30rem" }}
            place="right"
            effect="solid"
          />
        ) : null}
        <NewsHeadline dark={props.dark} target="_blank" href={el.url}>
          {el.title.trim().split(" ").length > 10
            ? el.title.trim().split(" ").splice(0, 10).join(" ") + " ..."
            : el.title.trim()}
        </NewsHeadline>
      </NewsItem>
    ));
  };

  return (
    <Wrapper>
      <Header>{name.toUpperCase()}</Header>

      <Content>{renderCountNumArticles()}</Content>

      <ViewMoreButton onClick={onClick}>
        {count < 15 ? `View More ▼` : "View Less ▲"}
      </ViewMoreButton>
    </Wrapper>
  );
}
