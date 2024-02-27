import nltk
from nltk.corpus import words

# Pobranie angielskich słów
english_words = set(words.words())

def vigenere_decrypt(text_to_decode, keyword):
    keyword = keyword.lower()
    keyword_length = len(keyword)
    plaintext = ''
    for i, char in enumerate(text_to_decode):
        if char.isalpha():
            ascii_offset = 97
            keyword_index = i % keyword_length
            shift = ord(keyword[keyword_index]) - ascii_offset
            decrypted_char = chr((ord(char.lower()) - ascii_offset - shift) % 26 + ascii_offset)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

def break_vigenere(text_to_decode):
    decoded_messages = {}  #Slownik @tab_wyj
    for keyword in english_words: #ograniczenie tez do slownika
        if len(keyword) == 3:
            decrypted_text = vigenere_decrypt(text_to_decode, keyword)
            if decrypted_text in english_words:
                decoded_messages[decrypted_text] = keyword.lower()
    return decoded_messages

#text_to_decode=(input("Napisz tekst do odszyfrowania w Vigenere: "))
text_to_decode = "URYyb, jbeyq!" #dog / nse= key, dog
decoded_messages = break_vigenere(text_to_decode)
decoded_messages_sorted = dict(sorted(decoded_messages.items()))
i=0
if decoded_messages_sorted:
    print("Znalezione poprawne odpowiedzi:")
    for message, keyword in decoded_messages_sorted.items():
        print(f"Odszyfrowany tekst: {message},  Klucz: {keyword}")
        i+=1
else:
    print("Nie znaleziono poprawnych odpowiedzi.")
print(i)