import React, { useEffect, useRef, useState } from 'react';

const ObjectDetection = () => {
  const videoRef = useRef(null);
  const [detectionResult, setDetectionResult] = useState(null);

  useEffect(() => {
    const fetchVideoStream = () => {
      if (videoRef.current) {
        videoRef.current.src = 'http://localhost:8080/predict';
      }
    };

    fetchVideoStream();

    const fetchDetectionData = async () => {
      try {
        const response = await fetch('http://localhost:8080/data');
        const data = await response.json();
        setDetectionResult(data.data);
      } catch (error) {
        console.error('Error fetching detection data:', error);
      }
    };

    const intervalId = setInterval(fetchDetectionData, 1000);

    return () => clearInterval(intervalId);
  }, []);

  return (
    <div>
      <h2>Object Detection</h2>
      <img
        ref={videoRef}
        alt="Video feed"
        width="720"
        height="480"
      />
      {detectionResult && (
        <div>
          <p>Detected: {detectionResult.class}</p>
          <p>Confidence: {detectionResult.confidence.toFixed(2)}</p>
        </div>
      )}
    </div>
  );
};

export default ObjectDetection;
