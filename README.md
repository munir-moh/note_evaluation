# NoteEvaluation Crew

Welcome to the NoteEvaluation Crew project. This project helps analyze and enhance your study notes using AI agents that collaborate to provide comprehensive understanding and learning recommendations.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customization

**Required Configuration:**
Add the following environment variables to your `.env` file:
1. `OPENAI_API_KEY` - Your OpenAI API key
2. `SERPER_API_KEY` - Your Serper API key for web searches
3. `MODEL` - The OpenAI model to use (e.g., gpt-4o)

**Optional Customizations:**
- **Agent Configuration** (`src/note_eval2/config/agents.yaml`):
  - Modify existing agents (note_summarizer, note_complementer, learning_advisor)
  - Add new agents with specialized roles
  - Configure agent parameters like temperature, model, and tools

- **Task Configuration** (`src/note_eval2/config/tasks.yaml`):
  - Customize existing task descriptions and goals
  - Define new tasks for additional analysis
  - Adjust task dependencies and output requirements

- **Code Customization:**
  - `src/note_eval2/crew.py`: Extend agent capabilities, add custom tools, or modify the workflow
  - `src/note_eval2/main.py`: Configure input handling and execution flow

All configurations can be adjusted to better suit your specific note analysis needs and preferences.

## Running the Project

To analyze your notes, place your note file as `note.txt` in the root folder and run:

```bash
$ crewai run
```

This will generate three output files:
- `note_summary_output.md`: A concise summary of your notes
- `note_complement_output.md`: Additional context and information related to your notes
- `learning_advice_output.md`: Personalized recommendations for further study

## Understanding Your Crew

The note_eval2 Crew consists of three specialized agents:
- **Note Summarizer**: Analyzes and creates concise summaries of your notes
- **Note Complementer**: Enriches your notes with additional relevant information
- **Learning Advisor**: Provides personalized learning recommendations

These agents work together using the tasks defined in `config/tasks.yaml`, and their capabilities are configured in `config/agents.yaml`.
