import React from "react";
import "../styles/home_style.css";
import MemberCard from "../components/member_card.jsx";
import Footer from "../components/footer.jsx";
import { Link, useNavigate } from "react-router-dom";


function Home() {
  const navigate = useNavigate();
  const viewProjects = () => {
      navigate("/projects");
  }
  const viewTeam = () => {
    navigate("/members");
  }

  return (
    <div>
      <div className="welcome">
        <div className="welcome-content">
          <h1>Society of Hispanic Professional Engineers</h1>
          <h2>Tech Team</h2>
          <p>
            Empowering Hispanic engineers through technical excellence,
            professional development, and community engagement.
          </p>
          <div>
            <button onClick={viewProjects} className="button-projects">
              Projects
            </button>
            <button onClick={viewTeam} className="button-team">
              Team
            </button>
          </div>
        </div>
        <div className="welcome-image hide-on-mobile">
          <img
            src={import.meta.env.BASE_URL + "home_media/dlt.png"}
            alt="SHPE member in front 3D Printer"
            className="image-properties"
          />
        </div>
      </div>
      <div className="eoh">
        <div className="eoh-container">
          <h1>Engineering Open House 2025</h1>
          <p>
            The SHPE Tech Team is proud to present our innovative project for
            the Engineering Open House 2025. Join us as we showcase cutting-edge
            technology and engineering solutions.
          </p>
          <Link to="/projects">
            <button className="button-learn">Learn More</button>
          </Link>
        </div>
      </div>
      <div className="team-section">
        <h2>The Team</h2>
        <div className="team-row">
          <MemberCard
            member={{
              avatar: import.meta.env.BASE_URL + "members_images/erick.jpg",
              name: "Erick",
              email: "eayal5@illinois.edu",
              role: "EOH Lead",
            }}
          />
          <MemberCard
            member={{
              avatar: import.meta.env.BASE_URL + "members_images/goat.jpg",
              name: "Kevin Cruz (La Flame)",
              email: "kcruz28@illinois.edu",
              role: "Lead Software Developer / Full Stack Developer",
            }}
          />
          <MemberCard
            member={{
              avatar: import.meta.env.BASE_URL + "members_images/juan.jpg",
              name: "Juan Fraguso",
              email: "juanjf2@illinois.edu",
              role: "Mechanical",
            }}
          />
        </div>
        <button onClick={viewTeam} className="button-view-team">
          View All
        </button>
      </div>
      <Footer />
    </div>
  );
}

export default Home;