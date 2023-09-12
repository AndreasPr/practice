import sys
measurements = list(map(int, input().split()))

if len(measurements) > 10 or len(measurements) < 10:
    sys.exit("Error! Only 10 numbers are allowed")

total_measurements = sum(measurements)
max_measurement = max(measurements)

if total_measurements >= 30 or max_measurement == 6:
    print("CLEAN")
else:
    print("DO NOT CLEAN")
