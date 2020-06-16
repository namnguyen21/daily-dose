import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import styled from "styled-components";

const Hover = styled.div`
  position: absolute;
  top: 2rem;
  right: 2rem;
  cursor: pointer;
  z-index: 99999999;
  @media (min-width: 800px) {
    display: none;
  }
`;

const Hamburger = styled.div`
  position: absolute;
  top: 0;
  right: 0;
`;

const Burger = styled.span`
  height: 0.3rem;
  width: 3rem;
  background-color: ${(props) => props.theme.palette.orange};
  display: block;
  &:not(:last-child) {
    margin-bottom: 0.5rem;
  }
`;

const Menu = styled.ul`
  position: absolute;
  top: 2rem;
  right: 0;
  background: ${(props) =>
    props.dark ? "#1f1f1f" : props.theme.palette.white};
  list-style: none;
  display: ${(props) => (props.open ? null : "none")};
  -webkit-box-shadow: -4px 4px 12px -9px rgba(0, 0, 0, 0.75);
  -moz-box-shadow: -4px 4px 12px -9px rgba(0, 0, 0, 0.75);
  box-shadow: -4px 4px 12px -9px rgba(0, 0, 0, 0.75);
`;

const MenuItem = styled.li`
  width: 20rem;
  text-align: center;
  text-transform: uppercase;
  font-size: 1.8rem;
  background: ${(props) =>
    props.dark ? "#1f1f1f" : props.theme.palette.white};
  color: ${(props) =>
    props.dark ? props.theme.palette.white : props.theme.palette.grey};
  &:hover {
    color: ${(props) => props.theme.palette.orange};
  }
  padding: 0.5rem;
`;

const StyledLink = styled(Link)`
  width: 100%;
  text-decoration: none;
  text-transform: uppercase;
  font-size: 1.8rem;
  color: ${(props) => props.theme.palette.grey};
  &:hover {
    color: ${(props) => props.theme.palette.orange};
  }
`;

export default function Dropdown({ dark }) {
  const [open, setOpen] = useState(false);

  useEffect(() => {
    console.log(window);
  }, []);

  const onMouseEnter = () => {
    setOpen(true);
  };

  const onMouseLeave = () => {
    setOpen(false);
  };

  return (
    <Hover
      onClick={() => setOpen(!open)}
      onMouseEnter={onMouseEnter}
      onMouseLeave={onMouseLeave}
    >
      <Hamburger>
        <Burger />
        <Burger />
        <Burger />
      </Hamburger>
      <Menu dark={dark} open={open}>
        <StyledLink to="/">
          <MenuItem dark={dark}>News</MenuItem>
        </StyledLink>
        <StyledLink to="/sports">
          <MenuItem dark={dark}>Sports</MenuItem>
        </StyledLink>
        <StyledLink to="/media">
          <MenuItem dark={dark}>Media</MenuItem>
        </StyledLink>
      </Menu>
    </Hover>
  );
}
