from keybert import KeyBERT

kw_model = KeyBERT(model='sentence-transformers/multi-qa-mpnet-base-dot-v1')
text = input('Bitte schreiben Sie die Anfrage:')
keywords = kw_model.extract_keywords(text,
                                     keyphrase_ngram_range = (2, 5),
                                     stop_words = 'english',
                                     highlight = False,
                                     top_n = 3)

keywords_list = list(dict(keywords).keys())
print(keywords_list)