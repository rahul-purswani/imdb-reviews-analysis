# Sentiment, Temporal, and Correlational Analysis of IMDB Reviews
<h>Group members: Rahul Purswani, Vijay Verma, Joe Rubalcava<h><br>
<b>Key Components:</b>
1. Data Extraction – Web Scraping:
   - Utilized Selenium and Chromium WebDriver to scrape data from IMDb pages.
   - Collected data from the top 100 highest-rated and lowest-rated movies on IMDb, resulting in 200 movies for analysis.
   - Extracted various attributes including movie titles, release years, genres, and detailed review data.
     
2. Data Pre-processing:
   - Cleaned and formatted the dataset to ensure consistency and accuracy.
   - Performed text preprocessing on user reviews, including punctuation removal, stop word elimination, and stemming.
   - Generated a sentiment column based on review ratings, categorizing them as positive, negative, or neutral.

3. Sentiment Analysis:
   - Created word clouds to visualize common words in positive, negative, and neutral reviews.
   - Developed a sentiment prediction model using TF-IDF vectors and logistic regression, achieving an overall accuracy of 84%.

4. Temporal Analysis:
   - Analyzed how review ratings and sentiments changed over time.
   - Examined seasonal variations in movie review sentiments.
   - Investigated the number of reviews per year and how average user ratings evolved annually.

5. Correlational Analysis:
   - Explored correlations between different movie genres based on frequent reviewers' ratings.
   - Identified positive correlations between certain genres, such as horror and adventure movies.
