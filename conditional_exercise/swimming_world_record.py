record_sec = float(input())
lenght_meters = float(input())
seconds_per_meter = float(input())
swimming = lenght_meters * seconds_per_meter
slowing = lenght_meters // 15 * 12.5
total_time = swimming + slowing
needed_time = total_time - record_sec
if total_time < record_sec:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {needed_time:.2f} seconds slower.")