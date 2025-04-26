# Research Agent: AI-Powered Topic Research Assistant

## Overview

This project is an AI-powered research assistant that leverages multi-agent systems to automate comprehensive topic research. Built with [crewAI](https://crewai.com), it uses a team of specialized AI agents to conduct thorough research on any topic and generate well-structured, detailed reports.

The system features:
- A streamlined web interface built with Streamlit
- Multiple specialized AI agents with different research roles
- Comprehensive data gathering and analysis capabilities
- Automatic report generation with structured content

## Features

- **Multi-Agent System**: Specialized roles including Research Leader and Reporting Analyst
- **Web-Based Interface**: Easy-to-use Streamlit interface for submitting research topics
- **Comprehensive Research**: Gathers information on topics with a focus on recent developments
- **Structured Outputs**: Generates well-formatted research reports with sections and citations
- **Real-time Status Updates**: Tracks research progress with visual status indicators

## Project Structure

```
research_agent/
├── research_crew/              # Main project folder
│   ├── src/                    # Source code
│   │   ├── app.py              # Streamlit web application
│   │   ├── research_crew/      # Core research module
│   │       ├── crew.py         # Agent crew implementation
│   │       ├── main.py         # Entry point
│   │       ├── config/         # Configuration files
│   │       │   ├── agents.yaml # Agent definitions
│   │       │   └── tasks.yaml  # Task definitions
│   │       └── tools/          # Custom tools
│   ├── output/                 # Output reports
│   ├── knowledge/              # Knowledge sources
│   └── tests/                  # Test suite
├── requirements.txt            # Python dependencies
└── .gitignore                  # Git ignore file
```

## Installation

### Prerequisites

- Python 3.10 or higher (and less than 3.13)
- OpenAI API Key

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Prince777a/Research_Agent.git
   cd Research_Agent
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory with:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

### Running the Web Interface

Start the Streamlit web interface:

```bash
cd research_crew/src
streamlit run app.py
```

Then open your browser at http://localhost:8501 to access the research interface.

### Using the Application

1. Enter your research topic in the text input field
2. Click "Start Research" to begin the research process
3. Wait for the agents to complete their tasks
4. Download the resulting research report

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [crewAI](https://crewai.com)
- Uses [Streamlit](https://streamlit.io/) for the web interface
- Powered by OpenAI's language models
