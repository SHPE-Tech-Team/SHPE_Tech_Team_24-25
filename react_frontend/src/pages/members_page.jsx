import React from "react";
import Footer from "../components/footer.jsx";
import TitleCard from "../components/title_card.jsx";

function MembersPage() {
  return (
    <div>
      <TitleCard
        title="Team Members"
        description="Meet the talented engineers behind SHPE Tech Team's innovative projects. Our diverse team brings together expertise in programming, mechanical  engineering, and more."
      />
      <Footer></Footer>
    </div>
  );
}

export default MembersPage;
