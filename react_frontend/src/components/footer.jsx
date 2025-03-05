import { Link } from "react-router-dom";
import "../styles/nav_style.css";


function Footer() {
  return (
    <div className="footer">
      <div className="footer-background">
        <div className="footer-nav">
          <Link to="/projects">Projects</Link>
          <Link to="/about">About</Link>
          <Link to="/members">Members</Link>
          <Link to="/contact">Contact</Link>
        </div>
        <div className="social-links">
          <a rel="noreferrer" href="https://www.instagram.com/shpe_uiuc/?hl=en" target="_blank"><img src="https://img.icons8.com/win10/512/FFFFFF/instagram-new.png" alt="Instagram Logo in white"></img></a>
          <a rel="noreferrer" href="https://github.com/SHPE-Tech-Team/AI_Loteria_24-25" target="_blank"><img src="https://img.icons8.com/ios11/512/FFFFFF/github.png" alt="Github Logo in white"></img></a>
          <a rel="noreferrer" href="https://www.linkedin.com/groups/13627278/" target="_blank"><img src="https://img.icons8.com/?size=100&id=44914&format=png&color=FFFFFF" alt="LinkedIn Logo in white"></img></a>
        </div>
      </div>
    </div>
  )
}

export default Footer;
