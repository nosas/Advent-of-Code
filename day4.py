import hashlib

secret_key = "ckczppom"
counter = 0

answer = secret_key + str(counter)
while not answer.startswith("00000"):
    counter += 1
    answer = secret_key + str(counter)
    answer = hashlib.md5(answer).hexdigest()

print counter, answer
