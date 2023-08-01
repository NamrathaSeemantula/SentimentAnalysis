# Emotion Analysis and Sentiment Classification of Text using NLP and NLTK
This project aims to analyze different emotions present in an essay, identify the dominant emotion, plot the emotions on a graph, and predict whether the entire text conveys a positive or negative emotion. Initially, the analysis is performed using manual natural language processing techniques without relying on any external libraries or packages. Later, the NLTK (Natural Language Toolkit) library is utilized to simplify and streamline the process.

**Overview:**

**Step 1: Preprocessing**

The text was converted to lowercase to ensure case-insensitive analysis.
Punctuation, numbers, and special characters were removed to maintain consistency.
The essay was tokenized by splitting it into individual words.
Stopword removal was performed to exclude common, non-emotional words.

**Step 2: Emotion Lexicon**

An emotion lexicon or dictionary was created, mapping words to their corresponding emotions.
The lexicon contained a curated list of words associated with specific emotions, such as happiness, sadness, jealousy, etc.

**Step 3: Emotion Analysis**

Each word in the essay was compared with the emotions in the lexicon.
The count was incremented for each emotion whenever a matching word was found in the lexicon.

**Step 4: Dominant Emotion**

The emotion with the highest count was identified, representing the dominant emotion in the text.

**Step 5: Sentiment Analysis**

Sentiment scores were assigned to words (positive for happy words, negative for sad words, etc.).
The overall sentiment score was calculated for the entire essay.

**Step 6: Plotting Emotions**

A bar chart was created to visualize the distribution of emotions in the text.
The x-axis represented different emotions, while the y-axis showed the frequency or count of each emotion.

**NLTK Integration:**

NLTK library was then introduced to streamline the process and reduce manual effort.
The NLTK provided built-in functions for tokenization and sentiment analysis using 

The project generates insights into the emotional content of the essay, revealing the presence and frequency of various emotions like sadness, happiness, jealousy, etc.
The dominant emotion provides a clear understanding of the primary emotional theme conveyed by the text.
The sentiment prediction indicates whether the overall tone of the text is positive or negative.
It can be used to analyze emotions in different essays or texts, gaining valuable emotional insights and sentiment predictions.
The manual and NLTK-based approaches offer options for users to choose the level of detail and complexity suitable for their specific use cases.

**Dependencies:**

The manual approach doesn't require any external libraries.
To use the NLTK-based approach, ensure you have the NLTK library installed (pip install nltk).
