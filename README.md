# Project Title: Sentiment Analysis of Reddit Political Posts and Comments

### Description

### Project Structure

```shell
reddit-political-opinion/
    data/                                                    # Directory for storing datasets.
    notebooks/
        initial_exploration/                                 # Notebooks for exploring the datasets.
        transform_data/                                      # Notebooks for transforming downloaded datasets (text normalisation, word embeddings etc).
        download_data.ipynb                                  # Notebook for downloading the original datasets from Kaggle (using `download_data.py`).
        sandbox.ipynb                                        # Unstructured notebook for implementing quick ideas.
    notes/
        progress-log.md                                      # Markdown file for tracking progress on the project.
        project-ideas.md                                     # Markdown file for managing ideas for the project.
        project-outline.md                                   # Markdown file for the outline and structure of the proejct.
    src/
        utils/
            download_data.py                                 # Function for downloading datasets from Kaggle using the Kaggle API.
            text_process.py                                  # Encapsulation of text normalisation functionality.
            vectorize_text.py                                # Encapsulation of text vectorisation functionality.
    test/                                                    # Unit tests for the modules in `src` using `pytest`.
    requirements.txt                                         # requirements.txt file with all necessary external dependencies.
```
