def find_first_unique_character(text):
    words = text.split() #розбиваю текст на окремі слова
    unique_chars = [] #список для зберігання першого унікального символу

    for word in words:
        char_count = {} #словник де буква ключ, значення - кількість
        for char in word: #цикл для окремих слів, де шукаємо унікальний символ
            if char not in char_count: #унікальність позначається значенням словника 1
                char_count[char] = 1
            else:
                char_count[char] += 1

        for char in word: #знову в циклі збираємо унікальні символи зі значенням 1
            if char_count[char] == 1:
                unique_chars.append(char) #наповнюємо список унікальних символів
                break

    for char in unique_chars: #пошук першого унікального символу
        if unique_chars.count(char) == 1:
            return char #повертаємо цей символ

    return None

text = '''The Tao gave birth to machine language. Machine language gave birth
to the assembler.
The assembler gave birth to the compiler. Now there are ten thousand
languages.
Each language has its purpose, however humble. Each language
expresses the Yin and Yang of software. Each language has its place within
the Tao.
But do not program in COBOL if you can avoid it.
        -- Geoffrey James, "The Tao of Programming"'''
print(find_first_unique_character(text))