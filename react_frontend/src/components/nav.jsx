import React, { useRef } from "react";
import { FaBars, FaTimes } from "react-icons/fa";
import { Link, NavLink, useNavigate } from "react-router-dom";
import "../styles/nav_style.css";
function NavBar() {
  const useNav = useRef();
  const navigate = useNavigate();

  const showNav = () => {
    useNav.current.classList.toggle("res_nav");
  };

  const goHome = () => {
    navigate("/");
  };

  return (
    <header>
      <img className="logo" src="SHPE_logo.avif" alt="SHPE Logo" />
      <h1 style={{ cursor: "pointer" }} onClick={goHome}>
        SHPE
      </h1>
      <nav ref={useNav}>
        <NavLink
          to="/projects"
          className={({ isActive }) => (isActive ? "active-link" : "")}
        >
          Projects
        </NavLink>
        <NavLink
          to="/about"
          className={({ isActive }) => (isActive ? "active-link" : "")}
        >
          About
        </NavLink>
        <NavLink
          to="/members"
          className={({ isActive }) => (isActive ? "active-link" : "")}
        >
          Members
        </NavLink>
        {/* <NavLink
          to="/vex"
          className={({ isActive }) => (isActive ? "active-link" : "")}
        >
          Vex Members
        </NavLink> */}
        <NavLink
          to="/contact"
          className={({ isActive }) => (isActive ? "active-link" : "")}
        >
          Contact
        </NavLink>
        <button className="nav-btn nav-close" onClick={showNav}>
          <FaTimes/>
        </button>
      </nav>
      <button className="nav-btn" onClick={showNav}>
        <FaBars />
      </button>
    </header>
  );
}

export default NavBar;
