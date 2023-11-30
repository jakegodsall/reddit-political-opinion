## Republican Opinions Dataset

### Initial Exploration

##### Understanding the Dataset:

###### Credibility

Generally, Kaggle datasets are reliable.
The dataset has been given a usability score by Kaggle of 10, which indicates that it is complete.

###### License

The dataset is licensed by OCD Attribution License.

###### Size

The dataset consists of 4,776,912 rows.

###### Structure

Columns:

`comment_id`: Unique identifier for each comment.

`score`: Popularity of the comment. Calculated as the number of upvotes minus the number of downvotes (`ups - downs`.)

`self_text`: The textual content of the comment.

`subreddit`: The subreddit where the comment was posted.

`created_time`: Timestampe of the comment's creation.

`post_id`: Unique identifier for the post.

`author_name`: Username of the comment author. Perhaps anonymatise this and use a numeric identifier to represent comments from the same user?

`controversiality`: Indicator of the comment's controversial nature. Boolean value. What determines this? Is it directly connected to score?

`ups`: Number of upvotes.

`downs`: Number of downvotes.

`user_is_verified`: Boolean of whether user is verified.

`user_account_creation`: Timestamp of when the account was created.

`user_awardee_karma`:

`user_awarder_karma`:

`user_link_karma`:

`user_total_karma`:

`post_score`: Score or popularity of the associated post. Caclulated as above.

`post_self_text`: Text content of the post.

`post_title`: Title of the post.

`post_upvote_ratio` Ratio of upvotes to downvotes.

`post_thumbs_up`: Total number of thumb's up for the post.

`post_total_award`:

`post_created_time`:

###### Accuracy

Missing Data:

-   4677 with missing user account information. Is this important?
-   155,275 missing `post_self_text`. Could this be because they are comments?
