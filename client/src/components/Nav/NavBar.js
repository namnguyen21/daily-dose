import React from "react";
import styled from "styled-components";
import { Link } from "react-router-dom";
import Dropdown from "./Dropdown";
import Logo from "../../images/logo.png";

const Nav = styled.nav`
  width: 100vw;
  padding: 1rem;
  position: relative;
`;

const Image = styled.img`
  height: 4rem;
  position: absolute;

  cursor: pointer;
  @media (min-width: 800px) {
    top: 1rem;
    left: 50%;
    transform: translateX(-50%);
  }
  @media (max-width: 800px) {
    top: 1rem;
    left: 1rem;
  }
`;

const Icon = styled.i`
  flex: 1;
  font-size: 2.5rem;
  cursor: pointer;
  color: ${(props) => props.theme.palette.blue};
  @media (min-width: 800px) {
    position: absolute;
    top: 1.5rem;
    right: 30rem;
  }
  @media (max-width: 800px) {
    position: absolute;
    top: 1.5rem;
    right: 7rem;
  }
`;

const ButtonGroup = styled.div`
  position: absolute;
  top: 1.5rem;
  right: 1rem;
  display: flex;
  @media (max-width: 800px) {
    display: none;
  }
`;

const Button = styled.button`
  padding: 0.3rem 2rem;
  font-size: 1.8rem;
  background: transparent;
  color: ${(props) => props.theme.palette.blue};
  border: solid 1px ${(props) => props.theme.palette.blue};
  cursor: pointer;
  &:hover {
    color: ${(props) => props.theme.palette.white};
    background-color: ${(props) => props.theme.palette.blue};
  }
  &:focus {
    outline: none;
  }
`;

export default function NavBar({ changeTheme, dark }) {
  return (
    <Nav>
      <div style={{ display: "block" }}></div>
      <h1>
        <Link to="/" alt='Daily Dose'>
          <Image src={Logo} alt="Daily Dose" title="Daily Dose" />
        </Link>
      </h1>
      <Icon onClick={changeTheme} className="fas fa-lightbulb"></Icon>

      <ButtonGroup>
        <Link to="/">
          <Button>News</Button>
        </Link>
        <Link to="/sports">
          <Button>Sports</Button>
        </Link>
        <Link to="/media">
          <Button>Media</Button>
        </Link>
      </ButtonGroup>
      <Dropdown dark={dark} />
    </Nav>
  );
}
