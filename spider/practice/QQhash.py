import hashlib
# 77a2ff8529901bc015298c62952e2b3143b91020f59ec8cfe09edef9b8d4198501b6e6a166827e8f
# 77a2ff8529901bc06f215e728760a7673c0880c421c6a1131c865247c8a15b4ab0931905590860f6
# 77a2ff8529901bc04e1f32fb6b9d3a74d6a86b52543aa6bfce3fa87f315f88fe36fd1e49cb3d69ca

k = '4e1f32fb6b9d3a74d6a86b52543aa6bfce3fa87f315f88fe36fd1e49cb3d69ca'
s = '15298c62952e2b3143b91020f59ec8cfe09edef9b8d4198501b6e6a166827e8f'
m = '6f215e728760a7673c0880c421c6a1131c865247c8a15b4ab0931905590860f6'
print(k, len(k))
qq_num = '123456'.encode()
hash_num_1 = hashlib.md5(qq_num).hexdigest()
hash_num_2 = hashlib.sha256(hash_num_1.encode()).hexdigest()
print(hash_num_1)
print(hash_num_2)

n = '77a2ff8529901bc0'
first = 'qq'.encode()
result = hashlib.sha256(first).hexdigest()
print(result, len(n))

