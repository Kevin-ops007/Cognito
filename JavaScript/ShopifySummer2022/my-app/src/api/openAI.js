const openAI = async (text) => {
  const OPENAI_SECRET = process.env.REACT_APP_SECRET_KEY;
  const data = {
    prompt: text,
    temperature: 0.5,
    max_tokens: 64,
    top_p: 1.0,
    frequency_penalty: 0.0,
    presence_penalty: 0.0,
  };

  try {
    let res = await fetch(
      "https://api.openai.com/v1/engines/text-curie-001/completions",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${OPENAI_SECRET}`,
        },
        body: JSON.stringify(data),
      }
    );
    res = await res.json();
    return res;
  } catch (error) {
    console.log("openAI:", error);
  }
};

export default openAI;
