import nltk

text = input('Bitte schreiben Sie die Anfrage:')
sentences = nltk.sent_tokenize(text) #分句
for sentence in sentences:
    words = nltk.word_tokenize(sentence) #分词
    tags = set(['JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS', 'PRP', 'RB', 'RBR', 'RBS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WP', 'WRB']) #限定词性
    word_tag = nltk.pos_tag(words) #标记词性
    ret = [] #保存所挑选词性的单词
    for word, pos in word_tag:
        if (pos in tags):
            ret.append(word)
    result = [' '.join(ret)]
    print(result)

