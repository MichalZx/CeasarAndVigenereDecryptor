import unittest

from ceasar import caesar_decrypt
from vigenere import vigenere_decrypt


class TestCaesarCipherDecryption(unittest.TestCase):
    def test_caesar_cipher_decryption_single_word(self):
        # Testowanie poprawności odszyfrowania pojedynczego słowa
        ciphertext = "ecv"
        shift = 2
        expected_plaintext = "cat"
        self.assertEqual(caesar_decrypt(ciphertext, shift), expected_plaintext)

    def test_caesar_cipher_decryption_empty_text(self):
        # Testowanie obsługi pustego tekstu
        ciphertext = ""
        shift = 3
        expected_plaintext = ""
        self.assertEqual(caesar_decrypt(ciphertext, shift), expected_plaintext)

    def test_caesar_cipher_decryption_large_shift(self):
        # Testowanie obsługi przesunięcia większego od długości alfabetu
        ciphertext = "lipps"
        shift = 30
        expected_plaintext = "hello"
        self.assertEqual(caesar_decrypt(ciphertext, shift), expected_plaintext)

    def test_caesar_cipher_decryption_special_characters(self):
        # Testowanie obsługi znaków specjalnych
        ciphertext = "khoor, zruog!"
        shift = 3
        expected_plaintext = "hello, world!"
        self.assertEqual(caesar_decrypt(ciphertext, shift), expected_plaintext)


class TestVigenereCipherDecryption(unittest.TestCase):
    def test_vigenere_cipher_decryption_single_word(self):
        # Testowanie poprawności odszyfrowania pojedynczego słowa
        ciphertext = "nse"
        keyword = "key"
        expected_plaintext = "dog"
        self.assertEqual(vigenere_decrypt(ciphertext, keyword), expected_plaintext)

    def test_vigenere_cipher_decryption_uppercase_keyword(self):
        # Testowanie obsługi wielkich liter w kluczu
        ciphertext = "NsE"
        keyword = "KEY"
        expected_plaintext = "dog"
        self.assertEqual(vigenere_decrypt(ciphertext, keyword), expected_plaintext)

if __name__ == '__main__':
    unittest.main()
