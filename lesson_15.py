"""
Делать код ревью порой не проще, чем писать сам код. А то и сложнее. Давайте попробуем? Вашей задачей будет изучить код и описать на своей страничке
гугл-дока - для чего он замышлялся и что должен делать.
Код написан на придуманном языке программирования, но по примерно общим правилам.


Функция helper получает на вход строку, число и еще одну строку и возвращает строку, где длина слов не больше переданного числа. В конец новой строки
добавляется вторая переданная строка (символ конца строки).


class Helper {
    public helper(STRING str, INT maxLen, STRING end) -> STRING {
        if (str.length < maxLen) {
            return str
        }

        STRING[] split = str.split(" ");
        STRING newStr = ""

        for (String strPart IN split) {
            if (newStr.length > maxLen) {
                break
            }

            newStr += strPart
        }

        newStr += end
        return newStr
    }
}

Функция получает на вход строку, число и еще одну строку. Что-то делает и возвращает строку. Вопрос - что он делает :)
"""

import string


class Helper:

    @staticmethod
    def _modify_string(text):
        return text.translate(str.maketrans('', '', string.punctuation))

    @staticmethod
    def helper(text: str, max_len: int, end: str):
        """
        :param text: Исходная строка
        :param max_len: Максимальная длина символов слова
        :param end: Символ конца строки
        :return: Получившаяся строка, с длиной слов, не превышающей max_len
        """

        modify_string = Helper._modify_string(text)

        if len(modify_string) <= max_len:
            return modify_string

        word_list = [word for word in modify_string.split(" ") if len(word) <= max_len]
        return " ".join(word_list) + end


def main():
    string = "It is the some string, test me now."
    print(Helper.helper(text=string, max_len=4, end="!"))


if __name__ == "__main__":
    main()
