Using Twitter 
Minimum Viable Product (MVP) 


The goal of this project is to create a recommendation system to make a movie recommendation based on the favorite Disney movies of two different users.

Solution Path
To do this, I am using movie summaries from Disney A to Z (Links to an external site.)—which generally include a brief plot overview, award highlights, character names, and actor credits (longer than 100 words, on average)—for every movie produced and released by Walt Disney Productions. The data consist of over 2100 movies, spanning films released during the 1920s (Walt Disney's Alice Comedies) through early 2020 (Pixar's Onward).

Work Completed
In pre-processing the data, I removed all digits and punctuation, I used spaCy in order to identify named entities (e.g., characters, actors), and to remove stop words. I also created a custom tokenizer to merge named entities into a single token, and to lemmatize all other tokens.

To begin building a topic model, I created a few baseline models using the CountVectorizer and TfidfVectorizer, with an NMF topic modeler and a small number of topic components (n = 10); however, because large portions of the corpus are made up of extensive film series featuring the same characters/themes (e.g., the Alice Comedies, Mickey Mouse and friends, several educational and safety series), CorEx, which allows "anchoring" of topic words, for semi-supervised topic modeling, can push the topic model towards these specific, previously identified subsets of words/characters.

Recent Findings
I have opted to tune a model using the CountVectorizer and a CorEx topic model. Though I am continuing to tune the number of topics to use in this model, I have determined some important anchors to separate topics, including:

['mickey', 'mickey mouse', 'pluto', 'silly', 'symphony']
['donald', 'donald duck', 'nephew']
['oswald', 'lucky', 'rabbit']
['educational']
['pooh', 'piglet', 'eeyore']
With only minimal tuning of the anchor strength, the topic model [also] produces some interesting sample topics, such as:

Mickey Mouse: cartoon, donald, donald duck, mickey mouse, mickey, pluto, silly, symphony, jack hannah, jack kinney
Animated films: animate, premiere, disney, hollywood, short circuit, artist, program, drawing, the walt disney animation studios short circuit, talent
Award winning films: academy award, nominate, academy, award, best, winner, james algar, featurette, narrate, nature
Sports films: high, team, coach, school, game, football, player, championship, student, teacher
Marvel movies: texas, mission, force, format, marvel studios, threat, international, surface, marvel, protect
Moving Forward
I will continue to tune (1) the anchor words and (2) the number of topics modeled to make the topics more coherent/interpretable. The final topic model will be used to build a basic recommendation system that takes in the favorite Disney movies of two different users and recommends a set of movies that are most similar to both.

 

Project MVP Example Credit: Hannah Lewis, Metis - Data Science & Machine Learning - Class of Oct 2021