import { react, useRef } from "react";
// import {FaBars, FaTimes} from "react-icons/fa"
import { Link } from "react-router-dom";
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
        <Link to="/projects">Projects</Link>
        <Link to="/about">About</Link>
        <Link to="/members">Members</Link>
        <Link to="/contact">Contact</Link>
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
