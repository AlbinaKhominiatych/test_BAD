def find_first_unique_character(text):
    words = text.split() #розбиваю текст на окремі слова
    unique_chars = [] #список для зберігання першого унікального символу






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