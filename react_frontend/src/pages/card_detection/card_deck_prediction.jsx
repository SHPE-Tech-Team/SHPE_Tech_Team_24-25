import {React, useState, useRef, useEffect} from "react";

const CardDeckPrediction = () => {
  const [isConnected, setIsConnected] = useState(false);
  
  return (
    <div>
      <h2>Card Deck Prediction</h2>
      <div >
        <img
          src="http://localhost:8080/predict_card_deck"
          alt="Video feed"
          width="720"
          height="480"
          className="video"
          onLoad={() => setIsConnected(true)}
          onError={() => setIsConnected(false)}
        />
        {!isConnected && (
          <div className="error-message">
            Cannot connect to video stream. Please check that the server is running.
          </div>
        )}
      </div>
    </div>
  );
};

export default CardDeckPrediction;