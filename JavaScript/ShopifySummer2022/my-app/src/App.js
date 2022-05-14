import logo from "./logo.svg";
import "./App.css";
import React, { useState } from "react";
import Response from "./components/Response";
import Input from "./components/Input";

function App() {
  const [res, setRes] = useState("");
  return (
    <div className="container">
      <div className="grid-item-level1">
        <h1 className="header">Fun with AI</h1>
        <Input res={res} setRes={setRes} />
        <Response res={res} />
      </div>
    </div>
  );
}

export default App;
