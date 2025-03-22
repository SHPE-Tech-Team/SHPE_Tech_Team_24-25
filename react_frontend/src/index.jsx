import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import reportWebVitals from "./reportWebVitals.jsx";

try {
  const root = ReactDOM.createRoot(document.getElementById("root"));
  root.render(
    <React.StrictMode>
      <App />
    </React.StrictMode>
  );

  reportWebVitals();
} catch (error) {
  console.error("Application initialization failed:", error);
  document.body.innerHTML = `<div style="color: red; padding: 20px;">
    <h1>Initialization Error</h1>
    <pre>${error.message}</pre>
    <pre>${error.stack}</pre>
  </div>`;
}
