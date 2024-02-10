# Voice-assisted-e-commerce-shopping
A conversational interface that assists with details of products with a voice input and output model

## Description  
The project uses **sentence transformers** to convert user-given sentences into embeddings and derives a **cosine similarity** between the query and the available product specifications from the Flipkart website. The embedding with the highest similarity will be displayed on the screen and read aloud using the **ResponsiveVoice** API.

Scraping mechanisms are built from scratch, **BeautifulSoup (bs4)** is used to parse into HTML, and selectors extract meaningful text information. The program iterates through all the available specifications listed for a product and stores them in dictionaries.

## Working
The model works by getting raw HTML from the product webpage using Beautiful Soup and pinpointing meaningful product specification details using HTML tags - A process known as _Web scraping_.

The extracted information is then converted into key-value pairs, meaning that each specification name is matched to its corresponding specification detail - _A Dictionary_

The user adds a query or request stating the desired specification name intuitively. This is achieved either through the text entry box or the [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API) which converts voice input to text.

[Sentence transformers](https://pypi.org/project/sentence-transformers/) convert this query or request into word embeddings - a type of word representation that allows words with similar meanings to have a similar representation.
Each of the keys in the key-value pairs (specification names) also goes through the same process.

We then find the similarity scores between each query and every specification name that exists in the key-value pair. The specification name with the highest similarity score to the query will be selected as the result to be displayed on the screen and read out loud using the [ResponsiveVoice text-to-speech API](https://responsivevoice.org/).
_Note that if the highest similarity value obtained does not cross a similarity score of 0.5 (50%), no result will be displayed._

## Modules used
1. Flask  
   `pip install Flask`
   <br><br>
2. Beautiful Soup  
   `pip install beautifulsoup4`
   <br><br>
3. Requests  
   `pip install requests`
   <br><br>
4. Sentence Transformers  
   `pip install sentence-transformers`
   <br><br>

## Cloning instructions
1. Clone the repository locally  
   `git clone https://github.com/keert04/-FLASK-Voice-assisted-e-commerce-shopping`
   <br> <br>
2. Navigate into the repository  
   `cd FLASK-Voice-assisted-e-commerce-shopping`
    <br><br>
3. Run app.py  
    `python app.py`
