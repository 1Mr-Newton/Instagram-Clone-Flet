import time

def generate_random_number(start, end):
    current_time = int(time.time() * 1000)
    return current_time % (end - start) + start

print(generate_random_number(1, 100))
print(generate_random_number(1, 100))
