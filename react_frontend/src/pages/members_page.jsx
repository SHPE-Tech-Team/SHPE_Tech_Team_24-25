import React from "react";
import Footer from "../components/footer.jsx"

function MembersPage() {
    return (
      <div className="team">
        <div className="team-background">
          <div className="team-text">
            <h1>Meet the Team</h1>
            <h2>Software</h2>
            <div className="members">
              <p>Jorge Becerra</p>
              <p>Daniel Quillo</p>
              <p>Kevin "LaFlame" Cruz</p>
              <p>Antonio Tapia</p>
            </div>
            <h2>Hardware</h2>
            <div className="members">
              <p>Jorge Becerra</p>
              <p>John Doe</p>
              <p>Jane Doe</p>
            </div>
          </div>
        </div>
        <Footer></Footer>
      </div>
    )
  }

export default MembersPage;
