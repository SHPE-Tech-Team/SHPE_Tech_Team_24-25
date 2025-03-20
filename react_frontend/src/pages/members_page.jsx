import React from "react";
import Footer from "../components/footer.jsx";
import TitleCard from "../components/title_card.jsx";
import MemberCard from "../components/member_card";
import "../styles/members_page_style.css";

function MembersPage() {
  return (
    <div>
      <TitleCard
        title="Team Members"
        description="Meet the talented engineers behind SHPE Tech Team's innovative projects. Our diverse team brings together expertise in programming, mechanical  engineering, and more."
      />

      <div className="team-section">
        <h2>The Team</h2>
        <div className="team-row">
          <MemberCard
            member={{
              avatar: "/AI_Loteria_24-25/home_media/dlt.png",
              name: "John Doe",
              email: "john.doe@example.com",
              role: "Developer",
            }}
          />
          <MemberCard
            member={{
              avatar: "/AI_Loteria_24-25/home_media/dlt.png",
              name: "La Flame",
              email: "john.doe@example.com",
              role: "Lead Software Developer",
            }}
          />
          <MemberCard
            member={{
              avatar: "/AI_Loteria_24-25/home_media/dlt.png",
              name: "John Doe",
              email: "john.doe@example.com",
              role: "Developer",
            }}
          />
          <MemberCard
            member={{
              avatar: "/home_media/dlt.png",
              name: "John Doe",
              email: "john.doe@example.com",
              role: "Developer",
            }}
          />
          <MemberCard
            member={{
              avatar: "/home_media/dlt.png",
              name: "La Flame",
              email: "john.doe@example.com",
              role: "Lead Software Developer",
            }}
          />
          <MemberCard
            member={{
              avatar: "/home_media/dlt.png",
              name: "John Doe",
              email: "john.doe@example.com",
              role: "Developer",
            }}
          />
        </div>
      </div>
      <Footer></Footer>
    </div>
  );
}

export default MembersPage;
