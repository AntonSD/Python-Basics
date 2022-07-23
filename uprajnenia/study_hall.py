w = float(input())  - 100
h = float(input())
whole_area = w * h
restricted_area = (h * 1) + 3 * (0.7 * 1.2)
working_seats = (whole_area - restricted_area) / (0.7 * 1.2)
print(working_seats)