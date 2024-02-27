import nltk

nltk.download('words')
english_words = set(nltk.corpus.words.words())

# Funkcja do deszyfrowania szyfru Cezara
def caesar_decrypt(ciphertext, shift):
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = 97 if char.islower() else 65
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

# Funkcja do łamania szyfru Cezara
def break_caesar(ciphertext):
    possible_messages = []
    for i in range(26):
        decrypted_text = caesar_decrypt(ciphertext, i)
        words = decrypted_text.split()
        valid_words = [word for word in words if word.lower() in english_words]
        if valid_words:
            possible_messages.append((i, decrypted_text))
    return possible_messages

# txt do odszyfrowania
#text_to_decode=(input("Napisz tekst do odszyfrowania w Cesarze: "))
#text_to_decode = "fqi" #dog
text_to_decode = "ecv" #cat
possible_messages = break_caesar(text_to_decode)
# Wyświetlenie poprawnych odpowiedzi z liczba k
if possible_messages:
    print("Znalezione poprawne odpowiedzi:")
    for shift, message in possible_messages:
        print(f"Przesunięcie: {shift}, Tekst: {message}")
else:
    print("Nie znaleziono poprawnych odpowiedzi.")
