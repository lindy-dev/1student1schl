# About

1Student1School is a school of multi-agent teachers hyper-personalized to teach you!👋 A privacy first solution that runs completely on your local machine with no data sent to the cloud. Get essay feedback, homework help, and more!

# Installation

1. Make sure you have ollama (https://ollama.com/), uv (https://docs.astral.sh/uv/), and python installed on your system. Additionally, you need to have the google's gemma3n:e4b and gemma3n:e2b model downloaded.
2. Clone this repository to your local machine.
3. Create a virtual environment in the project directory by running the following command:
   ```bash
   uv venv
   ```
4. Download the various packages via the following command:
   ```bash
   uv pip install -r pyproject.toml
   ```
5. Activate the virtual environment by running the following command:
   ```bash
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
   ```
6. Run the application using the following command:
   ```bash
   streamlit run main.py
   ```

# Usage

To use 1Student1School, simply navigate to the main.py file in your terminal or command prompt and run the application using the following command:

```bash
streamlit run main.py
```

# Contributing

1Student1School is an open-source project, and we welcome contributions from anyone who wants to help improve it. If you have any ideas for new features or improvements, feel free to open an issue on our GitHub repository.
