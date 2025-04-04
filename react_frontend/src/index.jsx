import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import reportWebVitals from "./reportWebVitals.jsx";

try {
  // Check if we need to redirect to a specific path stored in sessionStorage
  const redirectPath = sessionStorage.getItem('redirectPath');
  if (redirectPath) {
    sessionStorage.removeItem('redirectPath');
    // Use history API to change the URL without a full page reload
    window.history.replaceState(null, null, redirectPath);
  }

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
