# word, document, corpus
import math
class MyTFIDF():
    def __init__(self):
        self.maxTermFrequency = None

    def calculateMaxTermFrequency(self, document):
        print("calculating maxTermFrequency")
        max = 0
        for word in document:
            c = document.count(word)
            if c > max:
                max = c
        return max

    def words(self, document):
        doc = str(document)
        return doc.split(' ')

    def termFrequency(self, word, document):
        if self.maxTermFrequency is None:
            self.maxTermFrequency = self.calculateMaxTermFrequency(document)

        return 0.5 + 0.5 * (document.count(word) / len(document)) / (self.maxTermFrequency / len(document))
        # return document.count(word) / len(document)

    def inverseDocumentFrequency(self, word, corpus):
        count = 0
        # print('len(corpus): ' , len(corpus))
        for document in corpus:
            if word in document:
                count += 1
        return math.log((len(corpus) / (1+ count)),10)

    def tfidf(self, word, document, corpus):
        return self.termFrequency(word,document) * self.inverseDocumentFrequency(word,corpus)


    def test(self):
        _document1 = self.words("""Python is a 2000 made-for-TV horror movie directed by Richard
            Clabaugh. The film features several cult favorite actors, including William
            Zabka of The Karate Kid fame, Wil Wheaton, Casper Van Dien, Jenny McCarthy,
            Keith Coogan, Robert Englund (best known for his role as Freddy Krueger in the
            A Nightmare on Elm Street series of films), Dana Barron, David Bowe, and Sean
            Whalen. The film concerns a genetically engineered snake, a python, that
            escapes and unleashes itself on a small town. It includes the classic final
            girl scenario evident in films like Friday the 13th. It was filmed in Los Angeles,
             California and Malibu, California. Python was followed by two sequels: Python
             II (2002) and Boa vs. Python (2004), both also made-for-TV films.""")

        _document2 = self.words("""Python, from the Greek word (πύθων/πύθωνας), is a genus of
            nonvenomous pythons[2] found in Africa and Asia. Currently, 7 species are
            recognised.[2] A member of this genus, P. reticulatus, is among the longest
            snakes known.""")

        _document3 = self.words("""The Colt Python is a .357 Magnum caliber revolver formerly
            manufactured by Colt's Manufacturing Company of Hartford, Connecticut.
            It is sometimes referred to as a "Combat Magnum".[1] It was first introduced
            in 1955, the same year as Smith &amp; Wesson's M29 .44 Magnum. The now discontinued
            Colt Python targeted the premium revolver market segment. Some firearm
            collectors and writers such as Jeff Cooper, Ian V. Hogg, Chuck Hawks, Leroy
            Thompson, Renee Smeets and Martin Dougherty have described the Python as the
            finest production revolver ever made.""")

        _corpus = [_document1, _document2, _document3]

        # print(self.termFrequency('for', _document1))
        # print(self.termFrequency('for', _document2))
        # print('tfidf: ', self.tfidf('for', _document1, _corpus))


        for document in _corpus:
            dict = {word: self.tfidf(word, document, _corpus) for word in document}
            sorted_dict = sorted(dict.items(),key=lambda x: x[1],reverse=True)
            for i, word in enumerate(sorted_dict[:3]):
                print(i, ' : ',word)
            print('-------------------')


if __name__ == '__main__':
    myTFIDF = MyTFIDF()
    myTFIDF.test()
