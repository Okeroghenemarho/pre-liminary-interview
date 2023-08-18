# A fibonacci sequence uses the first two numbers to calculate consecutive numbers in the sequence
fibonacci_sequence = [1, 2]
sum_of_sequence = sum(fibonacci_sequence)
# to get the consecutive 48 terms,
for num in range(2, 51):
    fibonacci_num = fibonacci_sequence[num-1]+fibonacci_sequence[num-2]
    fibonacci_sequence.append(fibonacci_num)
    sum_of_sequence += fibonacci_num
print(fibonacci_sequence)
print(sum_of_sequence)
