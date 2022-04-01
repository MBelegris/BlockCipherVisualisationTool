import random

plaintext = []
key = []

for x in range(0, 64):
    plaintext.append(random.randint(0, 1))

for y in range(0, 48):
    key.append(random.randint(0,1))

print("Plaintext: " + str(plaintext))
print("Key: " + str(key))

for i in range(0, 64):
    print(plaintext[i], end="")
print()
for b in range(0, 48):
    print(key[b], end="")

# 1110000000001101011011101011011011111110101110101110001110001010
# 110001101101001100001000110111001000001011010011
# 0101111010011100010011011111010111111001011111011011011011111100
