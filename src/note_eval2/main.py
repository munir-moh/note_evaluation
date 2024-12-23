#!/usr/bin/env python
import sys
import warnings
import logging
from note_eval2.crew import NoteEval2
from litellm import APIError

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

logging.basicConfig(level=logging.DEBUG)

def run():
    """
    Run the crew.
    """
    logging.debug("Starting 'run' command")
    
    try:
        NoteEval2().crew().kickoff()
    except APIError as e:
        logging.error(f"APIError occurred: {e}")
    except Exception as e:
        logging.error(f"An error occurred while running the crew: {e}")

def train():
    """
    Train the crew for a given number of iterations.
    """
    logging.debug("Starting 'train' command")
    inputs = {
        "task": "note_summary_task"
    }
    try:
        logging.debug("Training the crew with inputs: %s", inputs)
        NoteEval2().crew().train(n_iterations=int(sys.argv[2]), filename=sys.argv[3], inputs=inputs)
    except IndexError:
        logging.error("Please provide the number of iterations and filename for training")
    except APIError as e:
        logging.error(f"APIError occurred: {e}")
    except Exception as e:
        logging.error(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    logging.debug("Starting 'replay' command")
    try:
        logging.debug("Replaying the crew with task_id: %s", sys.argv[2])
        NoteEval2().crew().replay(task_id=sys.argv[2])
    except IndexError:
        logging.error("Please provide the task ID for replaying")
    except APIError as e:
        logging.error(f"APIError occurred: {e}")
    except Exception as e:
        logging.error(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    logging.debug("Starting 'test' command")
    inputs = {
        "task": "note_summary_task"
    }
    try:
        logging.debug("Testing the crew with inputs: %s", inputs)
        NoteEval2().crew().test(n_iterations=int(sys.argv[2]), openai_model_name=sys.argv[3], inputs=inputs)
    except IndexError:
        logging.error("Please provide the number of iterations and OpenAI model name for testing")
    except APIError as e:
        logging.error(f"APIError occurred: {e}")
    except Exception as e:
        logging.error(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        logging.error("Please provide a command: run, train, replay, or test")
    else:
        command = sys.argv[1]
        if command == "run":
            run()
        elif command == "train":
            train()
        elif command == "replay":
            replay()
        elif command == "test":
            test()
        else:
            logging.error(f"Unknown command: {command}")
