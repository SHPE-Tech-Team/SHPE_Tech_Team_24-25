import React,{ useState, useEffect }from "react";
import ObjectDetection from './camera';
import RealtimePrediction from './data_predi';

function App() {
  return (
    <div>
      <h1>Hello, World!</h1>
      <ObjectDetection />
      <RealtimePrediction />
    </div>
  );
}

export default App;