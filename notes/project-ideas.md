# Project Ideas

### Research Question Ideas

###### Sentiment Analysis

-   Is the sentiment towards Republican's in Democrat-based subreddit's more/less severe than the reverse in Republican-based subreddits?
<!-- -   Is there a difference in the language used by both groups? Is one more likely to be agressive, sarcastic, use profanity?

###### Classification

-   Which topics are more often flagged as controversial?
-   Which topics are more likely to be upvoted/downvoted. How does this differ across subreddits?
-   Can we classify subreddits into groups based on common topics, and can this be measured using a small set of explanatory variables?

###### Correlations and Statistics

-   What are the common topics discussed in the subreddit groups? Is there a significant difference between the topics discussed by each group. Where is there overlap? How does opinion differ in this overlap?
-   Time-series analysis of topics. -->

<!-- ###### Predictive Modelling

-   Can you predict the popularity of a comment or post based on its content? -->

### Assumptions

-   Data is all English language.

### Models

1. **Lexicon Model**

    - VADER - Specifically designed to handle social-media data. Handles emojis, emoticons, slang, acronyms etc.
    - AFINN Lexicon - Includes scores for internet slang and abreviations.
    - EmoLex - Detects a larger range of emotions.

2. **Clustering**
3. Using pre-trained models
    - BERT
    - GPT-3

### Model Evaluation

##### Options

1. **Manual Evaluation** Manually reviewing a sample of texts and compare to model scores.
   How many would be necessary?
2. **Comparative Analysis** Compare the results with results from other established sentiment analysis tools.
