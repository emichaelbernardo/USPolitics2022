# Using Twitter Data to Identify Political Platforms using NLP (Topic Modeling)
## Introduction
Twitter is the modern political soapbox. We have all seen it used as a vehicle for both information and mis-information and this project aims to use tweets to identify the Democratic and Republican political platforms for the 2022 midterm elections in the United States.

Party platforms were once thought to be essential to the electoral process as they give the candidates a clear political position with which they can campaign. These platforms give voters a sense of what the candidates believe in, the issues they will focus on and if elected, how they will address them in their policy-making.

In the norm-breaking 2020 Presidential Election, the Republican party decided to not have any official platform other than to negate existing and proposed Democratic policies. 

This project hopes to use twitter data from the accounts of members from the 117th US Congress (Senators and Congressmen/women) and determine if / what the political platforms could be for the 2022 Midterm Elections. 

## Project Outline

- Acquire Twitter data
    - get account names of all congress teitter users
    - scrape last 1000 tweets from each user
- Clean data
    - extract: URLs, emojis, hashtags to be used in later analysis
    - remove: URLs, emojis, mentions, stop words, words with numbers, punctuation, special characters, text in brackets
    - transform: to all lower case, tokenize and lemmatize  
- Sentiment Analysis and Topic Modeling
    - score tweets using VADER, TextBlob and Flair models
    - get bigrams and trigrams
    - get topics using LSA, Corex and LDA
    - visualize topics using pyLDAvis
- Conclusion

