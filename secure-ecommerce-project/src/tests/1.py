import time
import gmpy2

print("\n📊 大整数运算性能测试") 
start_time = time.time() 
big_num = gmpy2.mpz(2) ** 2048 
end_time = time.time() 
print(f"✓ 计算2^2048耗时: {(end_time - start_time)*1000:.2f}ms") 
print(f"✓ 结果位数: {len(str(big_num))}位") 