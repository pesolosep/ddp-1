def caesar_cipher(text: str, c: int) -> str:
    key = "abcdefghijklmnopqrstuvwxyz"
    ciph = ""
    for w in text:
        ciph += key[(key.index(w) + c) % 26]
    return ciph


print(caesar_cipher("abc", 3))
