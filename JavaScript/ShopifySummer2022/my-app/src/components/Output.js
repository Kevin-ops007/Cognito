import React from "react";

function Output({ item }) {
  return (
    <div id="output">
      <label className="outputLable1">Prompt:</label>
      <span className="outputSpan1">{item.input}</span>
      <br />
      <label className="outputLable2">Response:</label>
      <span className="outputSpan2">{item.res}</span>
    </div>
  );
}

export default Output;
