import React from "react";
import "../styles/home_style.css";

function Home() {
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
            <button className="button-projects">Projects</button>
            <button className="button-team">Team</button>
          </div>
        </div>
        <div className="welcome-image">
          <img
            src="/home_media/dlt.png"
            alt="adolfo"
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
          <button className="button-learn">Learn More</button>
        </div>
      </div>
    </div>
  );
}

export default Home;