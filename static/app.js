const { useState } = React;

function App() {
    const [question, setQuestion] = useState("");
    const [answer, setAnswer] = useState("");
    const [error, setError] = useState("");
    const [isLoading, setIsLoading] = useState(false);

    async function handleSubmit(event) {
        event.preventDefault();

        const trimmedQuestion = question.trim();

        if (!trimmedQuestion) {
            setError("Please enter a question.");
            setAnswer("");
            return;
        }

        setIsLoading(true);
        setError("");

        try {
            const response = await fetch("/ask", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    question: trimmedQuestion
                })
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || "Unable to get an answer.");
            }

            setAnswer(data.answer);
            
        } catch (requestError) {
            setAnswer("");
            setError(requestError.message);
        } finally {
            setIsLoading(false);
        }
    }

    return React.createElement(
        "main",
        { className: "app-shell" },
        React.createElement(
            "section",
            { className: "chat-panel", "aria-labelledby": "app-title" },
            React.createElement(
                "div",
                { className: "panel-header" },
                React.createElement("p", { className: "eyebrow" }),
                React.createElement("h1", { id: "app-title" }, "RAG Chatbot"),
                React.createElement(
                    "p",
                    { className: "intro" },
                    "Ask a question about the indexed PDF and get an answer from the document context."
                )
            ),
            React.createElement(
                "form",
                { className: "question-form", onSubmit: handleSubmit },
                React.createElement(
                    "label",
                    { htmlFor: "question" },
                    "Question"
                ),
                React.createElement("textarea", {
                    id: "question",
                    value: question,
                    placeholder: "Ask question...",
                    onChange: (event) => setQuestion(event.target.value),
                    disabled: isLoading
                }),
                React.createElement(
                    "button",
                    { type: "submit", disabled: isLoading },
                    isLoading ? "Thinking..." : "Ask"
                )
            ),
            error && React.createElement(
                "div",
                { className: "message error", role: "alert" },
                error
            ),
            answer && React.createElement(
                "section",
                { className: "answer", "aria-label": "Answer" },
                React.createElement("h2", null, "Answer"),
                React.createElement("p", null, answer)
            )
        )
    );
}

ReactDOM.createRoot(document.getElementById("root")).render(
    React.createElement(App)
);
