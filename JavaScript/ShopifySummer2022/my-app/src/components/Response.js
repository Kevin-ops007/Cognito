import React from "react";
import { useState } from "react";
import { useEffect } from "react";
import Output from "./Output";

function Response({ res }) {
  const [items, setItems] = useState(res);

  useEffect(() => {
    const getLocalData = JSON.parse(localStorage.getItem("prompt")) ?? res;
    setItems(getLocalData);
  }, [res]);

  const display = () => {
    const rItems = Array.from(items).reverse();
    return rItems && rItems.map((item) => <Output key={item.id} item={item} />);
  };
  return (
    <div>
      <h2>Responses</h2>
      {display()}
    </div>
  );
}

export default Response;
