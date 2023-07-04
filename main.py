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

text = '''C makes it easy for you to shoot yourself in the foot. C++ makes that harder, but when you do, it blows away your whole leg. (с) Bjarne Stroustrup'''
print(find_first_unique_character(text))