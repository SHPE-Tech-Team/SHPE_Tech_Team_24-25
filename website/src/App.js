import React,{ useState, useEffect }from "react";
import ObjectDetection from './camera';
import RealtimePrediction from './data_predi';
import myImage from "./dlt.png";



function MyComponent() {
  return <img src={myImage} alt = "3D Printing" width = '500' height = '400' />;
}

function App() {
  return (
    <div>
      <div style = {{textAlign: 'center'}}>
        <h1>SHPE TECH TEAM - AI Loteria</h1>
        <MyComponent />
      </div>

      
      <ObjectDetection />
      <RealtimePrediction /> 
    </div>
  );
}


export default App;