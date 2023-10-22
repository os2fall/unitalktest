import hashlib
import string
inp = input().split()
pre = inp[8].encode()
end = inp[13]
print(pre)
print(end)
for i in range(1, 2**24):
   pps = pre + str(i).encode()
   happs = hashlib.sha256(pps).hexdigest()
   if happs.startswith(end):
       print(str(pps))
