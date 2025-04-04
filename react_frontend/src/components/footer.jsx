import { Link } from "react-router-dom";
import "../styles/nav_style.css";
import { FaInstagram, FaGithub, FaLinkedin, FaSlack } from "react-icons/fa";

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
          <a
            rel="noreferrer"
            href="https://www.instagram.com/shpe_uiuc/?hl=en"
            target="_blank"
          >
            <FaInstagram size={32} color="#FFFFFF" />
          </a>
          <a
            rel="noreferrer"
            href="https://github.com/SHPE-Tech-Team/AI_Loteria_24-25"
            target="_blank"
          >
            <FaGithub size={32} color="#FFFFFF" />
          </a>
          <a
            rel="noreferrer"
            href="https://www.linkedin.com/groups/13627278/"
            target="_blank"
          >
            <FaLinkedin size={32} color="#FFFFFF" />
          </a>
          <a
            rel="noreferrer"
            href="https://shpe-uiuc.slack.com/signup#/domain-signup"
            target="_blank"
          >
            <FaSlack size={32} color="#FFFFFF" />
          </a>
        </div>
      </div>
    </div>
  );
}

export default Footer;
