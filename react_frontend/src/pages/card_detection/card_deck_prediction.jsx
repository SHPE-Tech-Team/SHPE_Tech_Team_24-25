import {React, useState, useRef, useEffect} from "react";
import "../../styles/ai_loteria_style.css";

const CardDeckPrediction = () => {
  const [isConnected, setIsConnected] = useState(false);
  
    return (
      <div className="layout">
        <div className="container-one video-container">
          <div className="content-wrapper">
            <h2>Card Deck Prediction</h2>
            <div className="video-wrapper">
              <img
                src="http://localhost:8080/predict_card_deck"
                alt="Video feed"
                className="video-feed"
                onLoad={() => setIsConnected(true)}
                onError={() => setIsConnected(false)}
              />
              {!isConnected && (
                <div className="error-message">
                  Cannot connect to video stream. Please check that the server
                  is running.
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    );
};

export default CardDeckPrediction;