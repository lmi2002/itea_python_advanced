import keyword


class Language:

    __words = ['age', 'lom']

    def lexicon(self):
        return self.__words


class ProLanguage(Language):

    _keywords = ['ENTER', 'DEL']

    def lexicon(self):
        return self.___keywords

class Python(ProLanguage):
    _keywords = keyword.kwlist