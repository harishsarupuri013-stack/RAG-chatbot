import { useState } from "react";
import axios from "axios";

function App() {

  const [file, setFile] = useState(null);

  const [question, setQuestion] = useState("");

  const [answer, setAnswer] = useState("");

  const uploadPdf = async () => {

    const formData = new FormData();

    formData.append(
      "file",
      file
    );

    const response = await axios.post(
      "http://127.0.0.1:8000/upload",
      formData
    );

    alert(
      response.data.status
    );
  };

  const askQuestion = async () => {

    const response = await axios.post(
      "http://127.0.0.1:8000/ask",
      {
        question
      }
    );

    setAnswer(
      response.data.answer
    );
  };

  return (
    <div style={{ padding: "30px" }}>

      <h1>RAG Chatbot</h1>

      <br />

      <input
        type="file"
        onChange={(e) =>
          setFile(
            e.target.files[0]
          )
        }
      />

      <button
        onClick={uploadPdf}
      >
        Upload PDF
      </button>

      <br />
      <br />

      <input
        type="text"
        value={question}
        onChange={(e) =>
          setQuestion(
            e.target.value
          )
        }
        placeholder="Ask a question..."
        style={{
          width: "500px",
          padding: "10px"
        }}
      />

      <button
        onClick={askQuestion}
      >
        Ask
      </button>

      <br />
      <br />

      <h3>Answer</h3>

      <p>{answer}</p>

    </div>
  );
}

export default App;