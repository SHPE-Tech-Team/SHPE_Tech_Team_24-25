import React from "react";
import Footer from "../components/footer.jsx";
import CardDeckPrediction from "./card_detection/card_deck_prediction.jsx";
import TitleCard from "../components/title_card.jsx";
// alonso pg to do
/// Do figma concept before programming  !!!!!!!!!!!!
function AboutPage() {
  return (
    <div>
      <TitleCard
        title="About Us"
        description="Learn more about the Society of Hispanic Professional Engineers Tech Team at the University of Illinois at Urbana-Champaign."
      />
      <Footer></Footer>
    </div>
  );
}

export default AboutPage;
