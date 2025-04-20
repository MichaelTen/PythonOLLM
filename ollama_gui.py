import tkinter as tk
from tkinter import ttk, scrolledtext
import requests
import json

OLLAMA_HOST = "localhost"
OLLAMA_PORT = "11434"

def list_ollama_models(base_ip=OLLAMA_HOST, port=OLLAMA_PORT):
    try:
        url = f"http://{base_ip}:{port}/api/tags"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return [model['name'] for model in data.get('models', [])]
    except Exception as e:
        print(f"Error: {e}")
        return []

def send_prompt_to_ollama(model, prompt, base_ip=OLLAMA_HOST, port=OLLAMA_PORT):
    url = f"http://{base_ip}:{port}/api/generate"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        data = response.json()
        return data.get("response", "[No response]")
    except Exception as e:
        return f"Error: {e}"

def on_run_click():
    selected_model = model_var.get()
    prompt = prompt_entry.get("1.0", tk.END).strip()
    if not prompt:
        output_text.insert(tk.END, "[Prompt is empty]\n")
        return

    output_text.insert(tk.END, f"\n→ {prompt}\n", "prompt")
    output_text.insert(tk.END, f"Running {selected_model}...\n", "info")
    output_text.update_idletasks()

    result = send_prompt_to_ollama(selected_model, prompt)
    output_text.insert(tk.END, f"{result}\n\n", "response")
    output_text.see(tk.END)

# GUI setup
root = tk.Tk()
root.title("Ollama Prompt Tester")
root.geometry("600x500")

# Dropdown model selector
ollama_models = list_ollama_models()
model_var = tk.StringVar(value=ollama_models[0] if ollama_models else "None")
dropdown = ttk.Combobox(root, textvariable=model_var, values=ollama_models, state="readonly")
dropdown.pack(fill='x', padx=10, pady=10)

# Output display (scrollable)
output_text = scrolledtext.ScrolledText(root, height=20, wrap=tk.WORD)
output_text.tag_config("prompt", foreground="blue", font=("Consolas", 10, "bold"))
output_text.tag_config("response", foreground="black")
output_text.tag_config("info", foreground="gray")
output_text.pack(fill='both', expand=True, padx=10)

# Prompt input
prompt_entry = tk.Text(root, height=3, wrap=tk.WORD)
prompt_entry.pack(fill='x', padx=10, pady=5)

# Run button
run_button = tk.Button(root, text="Send Prompt", command=on_run_click)
run_button.pack(pady=5)

root.mainloop()
