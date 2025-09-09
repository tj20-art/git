message = b"Hello, Secure E-commerce!" 
public_key = private_key.public_key() 
     
    # 加密 
ciphertext = public_key.encrypt( 
        message, 
        padding.OAEP( 
            mgf=padding.MGF1(algorithm=hashes.SHA256()), 
            algorithm=hashes.SHA256(), 
            label=None 
        ) 
    ) 
     
    # 解密 
plaintext = private_key.decrypt( 
        ciphertext, 
        padding.OAEP( 
            mgf=padding.MGF1(algorithm=hashes.SHA256()), 
            algorithm=hashes.SHA256(), 
            label=None 
        ) 
    ) 
     
print(f"✓ 加密测试：原文 '{message.decode()}' -> 密文长度 {len(ciphertext)}字节") 
print(f"✓ 解密测试：解密结果 '{plaintext.decode()}'") 
print(f"✓ 加解密正确性：{message == plaintext}") 