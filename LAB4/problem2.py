from pylfsr import LFSR

def encrypt_decrypt_pylfsr(plaintext, init_state, poly_taps):
    # 初始化LFSR    
    lfsr = LFSR(initstate=init_state, fpoly=poly_taps)
    
    # 生成key長度耀明文的8倍(明文變成8倍的二進制)
    keystream = []
    for _ in range(len(plaintext) * 8):  
        keystream.append(lfsr.next())  # 將每個文字用到key中

 # 將字串轉為二禁制
    plaintext_binary = ''
    for c in plaintext:
        plaintext_binary += format(ord(c), '08b')

    # 把key跟轉成二進制的明文XOR
    encrypted_binary = ''
    for pb, ks in zip(plaintext_binary, keystream):
        encrypted_binary += str(int(pb) ^ int(ks))

    # 把加密的明文回傳
    encrypted_text = ''
    for i in range(0, len(encrypted_binary), 8):
        encrypted_text += chr(int(encrypted_binary[i:i+8], 2))
    return encrypted_text

def main():
    plaintext = ("ATNYCUWEARESTRIVINGTOBEAGREATUNIVERSITYTHATTRAN"
                 "SCENDSDISCIPLINARYDIVIDESTOSOLVETHEINCREASINGLYCO"
                 "MPLEXPROBLEMSTHATTHEWORLDFACESWEWILLCONTINUET"
                 "OBEGUIDEDBYTHEIDEATHATWECANACHIEVESOMETHINGMU"
                 "CHGREATERTOGETHERTHANWECANINDIVIDUALLYAFTERALLT"
                 "HATWASTHEIDEATHATLEDTOTHECREATIONOFOURUNIVERSI"
                 "TYINTHEFIRSTPLACE")
    init_state = [0,0,0,0,0,0,0,1]  # 00000001
    poly_taps = [8, 4, 3, 2]  # x^8 + x^4 + x^3 + x^2 + 1

    # 加密
    ciphertext = encrypt_decrypt_pylfsr(plaintext, init_state, poly_taps)
    print(f"Ciphertext: {ciphertext}")

    # 解密
    decrypted_text = encrypt_decrypt_pylfsr(ciphertext, init_state, poly_taps)
    print(f"Decrypted Text: {decrypted_text}")

    # 檢查是否加密正確
    if decrypted_text == plaintext:
        print("Encryption and decryption are correct!")
        
    else:
        print("There was an error in the encryption/decryption process.")

if __name__ == "__main__":
    main()
