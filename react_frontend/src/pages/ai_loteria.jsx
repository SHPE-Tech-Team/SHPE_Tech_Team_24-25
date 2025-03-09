import React from "react";
import CardDeckDetection from "./card_detection/card_deck_prediction.jsx";
import Toggle from "../components/toggle.jsx";
import "../styles/ai_loteria_style.css";


function AI_loteria() {
  return (
    <div>
      <div style={{ textAlign: "center" }}>
        <h1>AI Loteria - TEDDY AI</h1>
      </div>
      <div className="layout">
        <div className="container-one">
          <CardDeckDetection />
        </div>
        <div className="container-two">
          <CardDeckDetection />
        </div>
      </div>
    </div>
  );
}

export default AI_loteria;
