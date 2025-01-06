import React, { useState, useEffect } from 'react';
import io from 'socket.io-client';

const RealtimePrediction = () => {
  const [prediction, setPrediction] = useState(null);
  
  useEffect(() => {
    const socket = io('http://localhost:8080/predict');
    
    socket.on('prediction_data', (data) => {
      setPrediction(data);
    });
    
    return () => {
      socket.disconnect();
    };
  }, []);
  
  if (!prediction) return <div>Waiting for prediction...</div>;
  
  return (
    <div>
      <h2>Real-time Prediction</h2>
      <p>Class: {prediction.class}</p>
      <p>Confidence: {prediction.confidence.toFixed(2)}</p>
      <p>Index: {prediction.predicted_idx}</p>
    </div>
  );
};

export default RealtimePrediction;
