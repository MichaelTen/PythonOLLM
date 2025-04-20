# PythonOLLM
python ollama interface. simple. basic. 

# 🧠 Ollama Model Selector GUI

This is a minimal Python GUI tool for interacting with [Ollama](https://ollama.com/) via its REST API. The application provides:

- A dropdown menu for selecting from locally available Ollama models
- A multi-line prompt entry field
- A scrollable output pane that displays the LLM's response

It's intended as a quick, local interface for testing prompts and inspecting responses from any Ollama-compatible model (e.g., `llama3`, `mistral`, etc.).

---

## 📂 Files in This Repository

- `ollama_gui.py` – Main GUI script (you will create this manually)
- (Other files if applicable...)

---

## ⚙️ Requirements

- Python 3.7 or higher
- [Ollama installed and running locally](https://ollama.com/download)
- At least one model pulled via Ollama (e.g. `ollama pull llama3`)

---

## 🚀 How to Use

1. **Start Ollama**  
   Make sure Ollama is running in the background. You should be able to open this link in your browser:  
   [http://localhost:11434/api/tags](http://localhost:11434/api/tags)

2. **Open a Text Editor**  
   Open your preferred editor (e.g., VS Code, Notepad, Sublime Text).

3. **Create a new Python file**  
   Save it as:

   ```plaintext
   ollama_gui.py
   ```

4. **Copy the script contents**  
   Paste in the full GUI code found in this repository under `ollama_gui.py`.

5. **Run the application**  
   Open a terminal and execute:

   ```bash
   python ollama_gui.py
   ```

---

## 💡 Example Workflow

- Select a model from the dropdown.
- Type your prompt into the text area.
- Click **Send Prompt**.
- View the model’s response in the scrolling display area above.

---

## 📌 Notes

- This is a local tool: no internet is required once the model is downloaded.
- Useful for quick LLM experimentation without needing a full web app.
- Built using Python’s built-in `tkinter` and `requests` libraries — no external dependencies required.
