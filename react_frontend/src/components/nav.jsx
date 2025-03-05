import { react, useRef } from "react";
// import {FaBars, FaTimes} from "react-icons/fa"
import { Link, NavLink} from "react-router-dom";
import "../styles/nav_style.css";
function NavBar() {
  const useNav = useRef();

  const showNav = () => {
    useNav.current.classList.toggle("res_nav");
  };
  return (
    <header>
      <img className="logo" src="SHPE_logo.avif" alt="SHPE Logo" />
      <h1>SHPE</h1>
      <nav ref={useNav}>
        <NavLink to="/projects" className={({ isActive }) => (isActive ? 'active-link' : '')} >Projects</NavLink>
        <NavLink to="/about" className={({ isActive }) => (isActive ? 'active-link' : '')}>About</NavLink>
        <NavLink to="/members" className={({ isActive }) => (isActive ? 'active-link' : '')} >Members</NavLink>
        <NavLink to="/contact" className={({ isActive }) => (isActive ? 'active-link' : '')} >Contact</NavLink>
        <button className="nav-btn nav-close" onClick={showNav}>
          OUT
        </button>
      </nav>
      <button className="nav-btn" onClick={showNav}>
        daddy
      </button>
    </header>
  );
}

export default NavBar;
