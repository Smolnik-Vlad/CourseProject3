import nltk
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


async def preprocess_text(text):
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    filtered_tokens = [
        lemmatizer.lemmatize(token)
        for token in tokens
        if token.isalnum() and token not in stop_words
    ]
    return filtered_tokens


async def get_synonyms(word):
    synonyms = set()
    for synset in wordnet.synsets(word):
        for lemma in synset.lemmas():
            synonyms.add(lemma.name())
    return synonyms


async def get_hyponyms(word):
    hyponyms = set()
    for synset in wordnet.synsets(word):
        for hyp in synset.hyponyms():
            hyponyms.add(hyp.name()[0:-5])
    return hyponyms


async def get_hypernyms(word):
    hypernyms = set()
    for synset in wordnet.synsets(word):
        for hyp in synset.hypernyms():
            hypernyms.add(hyp.name()[0:-5])
    return hypernyms


async def expand_tags(tags):
    expanded_tags = set(tags)
    for tag in tags:
        expanded_tags.update(await get_synonyms(tag))
        expanded_tags.update(await get_hyponyms(tag))
        expanded_tags.update(await get_hypernyms(tag))
    return expanded_tags


async def get_text_tags(text: str):
    tags = await preprocess_text(text)
    expanded_tags = await expand_tags(tags)
    return [tag.replace("_", " ") for tag in expanded_tags]


async def calculate_similarity(tags1, tags2):
    tags1_set = set(tags1)
    tags2_set = set(tags2)
    intersection = tags1_set.intersection(tags2_set)
    # union = tags1_set.union(tags2_set)
    similarity = (
        len(intersection) / len(tags2_set) if len(tags2_set) > 0 else 0
    )
    return similarity
