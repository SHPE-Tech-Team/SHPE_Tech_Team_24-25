import React from "react";
import Footer from "../components/footer.jsx";
import CardDeckPrediction from "./card_detection/card_deck_prediction.jsx";
import TitleCard from "../components/title_card.jsx";
import "../styles/about_style.css";

function AboutPage() {
  return (
    <div>
      <TitleCard
        title="About Us"
        description="Learn more about the Society of Hispanic Professional Engineers Tech Team at the University of Illinois at Urbana-Champaign."
      />

      <div className="about-content">
        <h2>Our Mission</h2>
        <p>
          The Society of Hispanic Professional Engineers is a technical
          organization with a mission to empower the Hispanic community to
          realize its fullest potential and to impact the world through STEM
          awareness, access, support, and development.
        </p>
        <p>
          SHPE's Technical Team is dedicated to providing members with valuable
          technical experience while developing real-world engineering
          solutions. Our team works on various projects that allow members to
          apply classroom knowledge to practical challenges.
        </p>
        <p>
          We strive to create an inclusive environment where Hispanic engineers
          can grow professionally, develop leadership skills, and build a strong
          network of peers and mentors in the engineering field.
        </p>
      </div>
      <Footer></Footer>
    </div>
  );
}

export default AboutPage;
