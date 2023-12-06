# Project Outline

### Abstract:

-   Brief overview of the research topic, objectives, and significance.
-   Summary of methodology and key findings.

### Introduction:

-   Background information on sentiment analysis and its relevance in social media context.
-   Specific focus on Reddit as a platform for political discourse.
-   Overview of the datasets (Republican and Democrat-related subreddits).
-   Purpose and importance of the study.

### Literature Review:

-   Review of existing literature on sentiment analysis techniques, especially in political contexts.
-   Discussion on challenges with unlabelled data in sentiment analysis.
-   Overview of approaches used in similar studies and their outcomes.

### Objectives and Research Questions:

##### Objectives

-   Implement and compare the effectiveness of various sentiment analysis models, including lexicon-based methods, unsupervised learning (clustering with Word2Vec embeddings), and semi-supervised learning techniques on unlabelled Reddit datasets.
-   Utilise sentiment analysis to understand the nature of political discourse on Reddit, focusing on differences and similarities in sentiment between posts and comments from left-wing and right-wing subreddits.

##### Specific Goals of the Project

-   What are the Patterns of Sentiment in Political Discussions on Reddit, and How Do They Vary Across Different Political Orientations?
-   How do Different Sentiment Analysis Models Perform on Unlabelled Political Discourse Data from Reddit?
-   To What Extent Do Contextual Factors (such as Subreddit) and User Metadata Influence the Sentiment Analysis of Political Discussions on Reddit?
    -   Consider thumbs up, thumbs down, verified user etc.

### Methodology:

##### Data:

-   Description of the datasets (structure, content, and sources).
-   Ethical considerations

##### Preprocessing:

-   Steps for cleaning and preparing the data for analysis.

##### Sentiment Analysis Models:

-   Overview of different sentiment analysis models and methods to be compared.
-   Describe unsupervised sentiment analysis.
-   Rationale for selecting these models.

##### Model Implementation:

-   _Detailed description of the implementation process for each model_.
-   **Lexicon-Based Models**
    -   VADER
    -   AFINN
    -   SentiWordNet
-   **Clustering**
    -   Using word embeddings (Word2Vec, GloVe) to convert text to vectors, then compare clustering algorithms.
-   **Semi-supervised Learning**
    -   Consider using label propagation to generate a subset of labelled training data to test supervised learning methods.
-   **Deep Learning**
    -   Fine-tune pre-trained models on the data.

### Evaluation Metrics:

We don't have labelled sentiment data but we have other indicators such as upvotes, downvotes. Perhaps this could be used as a proxy somehow?

-   **Lexicon-Based Models**
    -   Lexicon coverage: Check whether the lexicon covers the vocabulary present in the dataset.
-   **Clustering**
    -   Distance of centroids, Sillouette Coefficient etc.
    -   Qualitative Review: Manually evaluate a sample of texts from each cluster to ensure they align with the expected sentiment categories (might be explanatory but is not quantitative).
-   **Semi-supervised Learning**
    -   Compare the performance of the model against a baseline model trained only on the initally labelled data.

### Expected Challenges and Limitations:

##### Data-Related Challenges

-   Lack of labelled data.
-   Representativeness. It will be difficult to get a subset of the data that contains equal numbers of positive, neutral, and negative texts without labels.
-   Sarcasm in the text.

##### Evaluating Model Performance

-   Evaluating the efficacy of models without labelled data is not straightforward.
-   Will be required to use a combination of quantitative and qualitative evaluation techniques.

### Timeline and Project Management:

Week 1: Data Preparation and Exploratory Analysis. Start writing initial sections of paper, introduction, literature review.
Week 2: Model Development and Training.
Week 3: Model Training and Evaluation.
Week 4: Complete draft of paper.
