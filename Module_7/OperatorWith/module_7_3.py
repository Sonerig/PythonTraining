class WordsFinder:
    def __init__(self, *file_names):
        self.__file_names = file_names

    def get_all_words(self):
        all_words = dict()
        for file_name in self.__file_names:
            with open(file_name) as file:
                line = ""
                for current_line in file:
                    for char in current_line:
                        if not (char in [',', '.', '=', '!', '?', ';', ':', ' - ']):
                            line += char.lower()
                line = line.split()
                all_words.update({file_name: line})
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        list_of_finded_words = list()
        for name, words in all_words.items():
            for counter in range(len(words)):
                if words[counter] == word.lower():
                    list_of_finded_words.append({name: counter + 1})
                    break
        return list_of_finded_words

    def count(self, word):
        all_words = self.get_all_words()
        list_of_counted_words = list()
        for name, words in all_words.items():
            word_counter = 0
            for counter in range(len(words)):
                if words[counter] == word.lower():
                    word_counter += 1
            list_of_counted_words.append({name: word_counter})
        return list_of_counted_words


finder2 = WordsFinder('test_file.txt', "Rudyard Kipling - If.txt")
print(finder2.get_all_words())  # Все слова
print(finder2.find('FoR'))     # 3 слово по счёту
print(finder2.count('for'))    # 4 слова teXT в тексте всего
