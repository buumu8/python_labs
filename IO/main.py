from translate import Translator

translator = Translator(to_lang="ja")
try:
    with open("./test.txt", mode="r+") as my_file:
        text = my_file.read()
        print(text)
        translation = translator.translate(text)
        with open("./text.ja.txt", mode="w", encoding="utf-8") as my_file2:
            my_file2.write(translation)
            print(translation)
except FileNotFoundError as e:
    print("check your file path")
