start = int(input("Start: "))
stop = int(input("Stop: "))
step = int(input("Step: "))
odd_counter = 0
even_sum = 0
for x in range(start, stop, step):
    if x%2 != 0:
        odd_counter+=1
    if x%2 == 0:
        even_sum+=x
print(f"2nd value in range = {range(start, stop, step)[1]}")
print(f"Last value in range = {range(start, stop, step)[-1]}")
print(f"odd_counter = {odd_counter}")
print(f"even_sum = {even_sum}")


