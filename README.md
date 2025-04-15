## **OlimpusChat**

<p align="center">
  <img src="./images/olimpus_logo.png" alt="estuda-ai" width="30%">
</p>

### **Instructions to Start the Project**

This is the **OlimpusChat** project, where the gods of Olympus debate various topics using artificial intelligence. Follow the steps below to get started:

### **1. Creating and Activating a Virtual Environment**

First, create a virtual environment for the project:

```bash
python -m venv venv
```

Activate the virtual environment:

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```

- **Mac/Linux**:
  ```bash
  source venv/bin/activate
  ```

### **2. Installing Dependencies**

With the virtual environment activated, install the required dependencies:

```bash
pip install -r requirements.txt
```

### **3. Configuring the .env**

The project uses environment variables to configure the AI model usage. You will need either a configured **Ollama** model or a valid **Google API** key.

- **Set up the .env**: Create a `.env` file in the root of the project using the `.env.example` template as a guide.

Example of a `.env` file:

```bash
GOOGLE_API_KEY=your_google_api_key_here
```

### **4. Execution Parameters**

The parameters can be checked using the `-h` or `--help` flag:

```bash
python main.py --help
```

#### **Available Arguments**:

- `--file`: Name of the file to save the conversation. **(Optional)**
- `--file_type`: The type of output text. Can be **txt**, **json**, or **md**. **(Optional)**
- `--language`: The language of the conversation. Can be **pt** (Portuguese) or **en** (English). **(Optional)**
- `--supervisioned`: If the model is supervised or not. **(Optional)**
- `--n_rounds`: Number of debate rounds. **(Optional)**

### **5. Running the Project**

Example of running with parameters:

```bash
python main.py --language en --n_rounds 5 --file "debate.txt" --file_type json
```

---

### **TODO List**

- **Support for Multiple Languages**: Implement full support for more languages in the debate (e.g., adding more languages to the system beyond Portuguese and English).
- **Add Support for More Models**: Integrate additional AI models such as **OpenAI**, or other models via API (e.g., HuggingFace, etc.).
- **Add a Visual Interface with Streamlit**: Build a visual interface in the browser using **Streamlit** to interact with the project more intuitively.
- **Fine-Tuning Models for Debate Simulation**: Perform fine-tuning on the models to simulate debates more realistically and enhance the quality of the generated debates.

---
