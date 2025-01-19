# Gemini-Pro Chatbot with Streamlit

This repository contains a Streamlit application for interacting with the Google Gemini-Pro AI model. The chatbot uses Streamlit's user-friendly interface to facilitate conversational AI interactions.


## Features
- **Streamlit-based Chat Interface**: A simple, clean interface for interacting with the chatbot.
- **Google Gemini-Pro Integration**: Utilizes the Gemini-Pro generative AI model for advanced conversational capabilities.
- **Customizable Themes**: Includes a custom dark theme with white background for better readability.
- **Session Persistence**: Maintains chat history within the session.

## Requirements

- Python 3.9 or above
- `streamlit`
- `python-dotenv`
- `google-generativeai`

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Create a virtual environment and activate it**:
   ```bash
   python -m venv env
   source env/bin/activate # On Windows, use `env\\Scripts\\activate`
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the root directory.
   - Add your Google API key:
     ```env
     GOOGLE_API_KEY=your_google_api_key
     ```

## Usage
1. **Run the Streamlit application**:
   ```bash
   streamlit run app.py
   ```

2. **Open the application**:
   - The application will open in your default web browser, or you can access it at `http://localhost:8501`.

3. **Interact with the chatbot**:
   - Type your query in the input field labeled "Ask Gemini-Pro..." and view the responses from Gemini-Pro AI.

## File Structure

- `app.py`: Main Streamlit application file.
- `.env`: Environment variables file (not included; you need to create this).
- `requirements.txt`: Python dependencies for the project.

## Customization

### Page Theme
The custom theme uses CSS injected via Streamlit's `st.markdown` to provide a white background and dark text for better readability. You can modify the theme by editing the CSS block in the `app.py` file:
```python
st.markdown(
    """
    <style>
        body {
            background-color: white;
            color: #333333;
        }
        .st-bq {
            background-color: #f5f5f5 !important;
            color: #333333 !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)
```

### Google Gemini-Pro API Configuration
The Google Gemini-Pro AI model is configured using the `google-generativeai` library. Ensure that you have a valid API key and that it is stored in the `.env` file as `GOOGLE_API_KEY`.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue to discuss changes or new features.

## Acknowledgments
- [Streamlit](https://streamlit.io/) for the interactive UI framework.
- [Google Generative AI](https://cloud.google.com/generative-ai) for the Gemini-Pro model.
- [Dotenv](https://pypi.org/project/python-dotenv/) for managing environment variables.
```
