import sys

"Task is to create a list containing 1M values."
"This approach is using without iterator and generator"

lst = [i for i in range(1_000_000)]
print(lst[:5])
print("TRADITIONAL APPROACH:", sys.getsizeof(lst))  # Memory consumption in this case

print("----------------------")
"This approach is using I&G"


def generate_numbers(limit):
    for num in range(1, limit+1):
        yield num


itr = generate_numbers(1_000_000)

for _ in range(5):
    print(next(itr))

print("I&G Approach:", sys.getsizeof(itr))  # Memory consumption in this case
