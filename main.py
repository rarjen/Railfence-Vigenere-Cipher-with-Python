# Fungsi Encrypt Vigenere
def vigenere_encrypt(plaintext, key):
    result = ""
    key_index = 0

    for char in plaintext:

        # Melakukan checking apakah plaintext alphabet atau bukan
        if char.isalpha():

            # mengubah plaintext ke lowercase
            plaintext_char = char.lower()
            key_char = key[key_index].lower()

            # Menghitung nilai offset untuk lookup table
            offset = (ord(key_char) - ord('a'))

            # Enkripsi plaintext dengan menggunakan lookup table
            result_char = chr(
                ((ord(plaintext_char) - ord('a') + offset) % 26) + ord('a'))

            # Menambahkan hasil ke string hasil
            result += result_char.upper() if char.isupper() else result_char

            # Memindahkan indeks kunci ke karakter selanjutnya
            key_index = (key_index + 1) % len(key)
        # Jika plaintext bukanlah alfabet, maka menambahkan string hasil tanpa perubahan
        else:
            result += char

    return result


# Fungsi Rail Fence Cipher
def rail_fence_encrypt(plaintext, rails):

    # Inisialisasi variable dan list
    fence = [['\n' for i in range(len(plaintext))] for j in range(rails)]
    rail = 0
    direction = 1
    result = ""

    print("fence init")
    print(fence)

    # Membuat Pagar Rel Transposisi dengan menempatkan plaintext pada rel-rel yang teredia
    for char in plaintext:
        fence[rail][fence[rail].index('\n')] = char
        rail += direction
        if rail == rails-1 or rail == 0:
            direction = -direction

    print("fence")
    print(fence)
    # Mengambil karakter pada setiap rel untuk membentuk cipher text
    for rail in range(rails):
        for char in fence[rail]:
            if char != '\n':
                result += char

    return result


plaint_text = "ini adalah pesan"
key_viginere = "rahasia"

hasil_enkripsi_viginere = vigenere_encrypt(plaint_text, key_viginere)
print("hasil_enkripsi_viginere")
print(hasil_enkripsi_viginere)

key_rail_fence = 4
hasil_enkripsi_rail_fence = rail_fence_encrypt(hasil_enkripsi_viginere, 4)
print("hasil_enkripsi_rail_fence")
print(hasil_enkripsi_rail_fence)
