import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as f:
                    words = []
                    for line in f:
                        line = line.lower()
                        # Убираем пунктуацию, пробелы и определенные символы
                        line = line.translate(str.maketrans('', '', string.punctuation))
                        words.extend(line.split())

                    # Удаляем дубликаты и сохраняем в словарь
                    all_words[file_name] = list(set(words))  # Преобразуем в список уникальных слов

            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
            except Exception as e:
                print(f"Произошла ошибка при обработке файла {file_name}: {e}")

        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word)

        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            count = words.count(word)
            if count > 0:
                result[file_name] = count

        return result

# Пример использования
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все уникальные слова
print(finder2.find('text'))  # Индекс слова 'text'
print(finder2.count('text'))  # Количество слов 'text' в тексте
