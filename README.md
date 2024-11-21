
# AIChatInference

This project demonstrates how the base agent functions. The user inputs a `.csv` file and a natural language prompt, and receives the `.json` schema and selected entities from the file.

## How to Run?

To run the project, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/AragonerUA/aichatinference.git
   cd aichatinference
   ```

2. **Add an OpenAI API Key**:
   - Go to the `.streamlit` directory.
   - Add your OpenAI API key to the `secrets.toml` in the following format:
     ```
     OPENAI_API_KEY="YOUR_KEY"
     ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:

   ```bash
   streamlit run inference/app.py
   ```

## Project Features

- **Natural Language Interface**: Accepts user prompts in natural language to process `.csv` files.
- **JSON Schema Generation**: Generates a structured `.json` schema based on the provided data.
- **Entity Selection**: Extracts specific entities from the file based on user input.

## Project Structure

```
AIChatInference/
├── data/
├── inference/
│   ├── .streamlit/
│   │   ├── secrets.toml
│   ├── ai_chat.py
│   ├── app.py
│   ├── apply_sequence.py
│   ├── requirements.txt
│   ├── transformations.py
└── README.md
```

## License

This project is licensed under the [MIT License](LICENSE).
