import React,{ useState, useEffect }from "react";
import ObjectDetection from './camera';

function App() {
  const [data, setData] = useState(null);
  useEffect(() => {
    const fetchData = async () => {
      const result = await fetch("http://localhost:8080/data");
      result.json().then(json => {
        console.log(json.data)
        setData(json.data)

      })
    };
    fetchData();
  }, []);
  return (
    <div>
      <h1>Hello, World!</h1>
      <ObjectDetection />
      <p style={{ color: "blue", fontSize: "18px" }}>
        {data && data.confidence !== undefined ? data.confidence : "Loading data..."}
      </p>
    </div>
  );
}

export default App;