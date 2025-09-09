import time
from cryptography.hazmat.primitives.asymmetric import rsa
print("\n🔐 RSA功能测试") 
start_time = time.time() 
private_key = rsa.generate_private_key( 
    public_exponent=65537, 
    key_size=1024 
) 
end_time = time.time() 
print(f"✓ 生成1024位RSA密钥耗时: {(end_time - start_time)*1000:.2f}ms") 
     