# test_BAD
# Як працює програма?
Алгоритм (сам код містить коментарі та коміти)

1. Вхідний текст розбивається на окремі слова. Для цього використовується роздільник пробілу, який допомагає визначити межі між словами.

2. Для кожного слова в тексті знаходиться перший символ, який більше не повторюється у даному слові. Це означає, що цей символ з'являється лише один раз і не повторюється в подальшому.

3. Отримані перші символи для кожного слова утворюють новий набір символів.

4. З отриманого набору символів вибирається перший унікальний символ, який більше не зустрічається в наборі.

5. Вибраний символ повертається як результат.

# Загальний опис рішення (дуже багато тексту😊)
Розбиваємо текст на окремі слова:

"The", "Tao", "gave", "birth", "to", "machine", "language.", "Machine", "language", "gave", "birth",
"to", "the", "assembler.", "The", "assembler", "gave", "birth", "to", "the", "compiler.", "Now", "there", "are", "ten",
"thousand", "languages.", "Each", "language", "has", "its", "purpose,", "however", "humble.", "Each", "language",
"expresses", "the", "Yin", "and", "Yang", "of", "software.", "Each", "language", "has", "its", "place", "within", "the", "Tao.",
"But", "do", "not", "program", "in", "COBOL", "if", "you", "can", "avoid", "it.", "--", "Geoffrey", "James,", ""The", "Tao", "of", "Programming"

Для кожного слова знаходимо перший символ, який більше не повторюється:

"The" - Перший символ, який більше не повторюється: "T"

"Tao" - Перший символ, який більше не повторюється: "T"

"gave" - Перший символ, який більше не повторюється: "g"

і так далі

Отримуємо такий результат:

"T", "T", "g", "b", "t", "m", "l", "M", "l", "g", "b", "t", "t", "a", "g", "b", "t", "c", "N", "t", "a", "t", "t", "l",
"E", "l", "h", "i", "p", "h", "E", "l", "e", "t", "Y", "a", "o", "s", "E", "l", "h", "i", "p", "w", "t", "T", "B", "d", "n",
"p", "i", "C", "i", "y", "c", "a", "i", "-", "G", "J", """, "T", "o", "P"
Якщо ми пройдемося по цьому набору символів, ми побачимо, що перший символ, який не повторюється, це "m". Ось детальний розбір:

Символ "T" повторюється
Символ "T" повторюється
Символ "g" повторюється
Символ "b" повторюється
Символ "t" повторюється
Символ "m" не повторюється
Отже, перший символ, який не повторюється, в даному наборі - "m".
