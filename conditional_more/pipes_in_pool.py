v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())
p1_liters = p1 * h
p2_liters = p2 * h
p1_p2 = p1_liters + p2_liters
difference = abs(v - p1_p2)
p1_p2_percent = p1_p2 / v * 100
p1_percent = (p1 / p1_p2) * 100
p2_percent = (p2 / p1_p2) * 100
if p1_p2 < v:
    print(f"The pool is {p1_p2_percent:.2f}% full. Pipe 1: {p1_percent:.2f}%. Pipe 2: {p2_percent:.2f}%.")
else:
    print(f"For {h:.2f} hours the pool overflows with {difference:.2f} liters.")