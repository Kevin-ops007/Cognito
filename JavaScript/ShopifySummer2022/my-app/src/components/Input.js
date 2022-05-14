import React from "react";
import { useState } from "react";
import openAI from "../api/openAI.js";

const Input = ({ setRes }) => {
  const [input, setInput] = useState("");

  const clickHandler = async (e) => {
    e.preventDefault();
    try {
      if (input.trim() !== "") {
        const response = await openAI(input);
        const uid = response.id;
        const text = response.choices[0].text;
        const getLocalData = JSON.parse(localStorage.getItem("prompt")) ?? [];
        getLocalData.push({ input: input, res: text, id: uid });
        localStorage.setItem("prompt", JSON.stringify(getLocalData));
        setRes(getLocalData);
      }
    } catch (error) {
      console.log("Input:", error);
    }
  };

  const inputHandler = (e) => {
    setInput(e.target.value);
  };

  return (
    <div>
      <label>Enter prompt</label>
      <br />
      <textarea
        rows="15"
        cols="80"
        placeholder="Feel free to leave the page, all responses are saved!"
        onChange={inputHandler}
      ></textarea>
      <br />
      <button onClick={clickHandler} className="button">
        Submit
      </button>
    </div>
  );
};

export default Input;
