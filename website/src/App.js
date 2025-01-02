import React,{ useState, useEffect }from "react";
import ObjectDetection from './camera';

function App() {
  // const [data, setData] = useState(null);

  // useEffect(() => {
  //   fetch("/predict/data")
  //     .then(response => response.json())
  //     .then(data => {console.log("Received data:", data)
  //       setData(data)})

  //     .catch(error => console.error('Error fetching data:', error));
  // });
  return (
    <div>
      <h1>Hello, World!</h1>
      <ObjectDetection />
      {/* <p>{data.probabilities}</p> */}
    </div>
  );
}

export default App;