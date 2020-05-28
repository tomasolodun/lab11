'''б) Дан текстовий файл f. Додати в кінець файлу f символи голосних букв, які не
входять до вихідного файлу.'''

def get_data():
    with open("C:\\Users\\Toma\Desktop\\NewFold\\k.txt", encoding="utf-8") as f:
        data = f.read()
    f.close()
    return data

data = get_data()
words = {"а", "у", "ї", "і", "и", "я", "ю", "о", "е", "є"}
with open("C:\\Users\\Toma\\Desktop\\NewFold\\k.txt", "a", encoding="utf-8") as f:
    for i in words:
        if i not in data:
            f.write(i)
f.close()