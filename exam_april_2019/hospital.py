period = int(input())
patients_for_the_day = int(input())
doctors = 7
rest_patients = 0
day = 0

for number in range(period):
    day += 1
    patients = int(input())
    if day == 3:
        doctors += 1
    if patients_for_the_day > doctors:
        rest_patients += patients_for_the_day - doctors
treated_patients = patients_for_the_day - rest_patients
print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {rest_patients}.")
