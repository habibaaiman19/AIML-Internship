temperatures=[22,24,25,28,30,29,27,26,24,22]
print("first reading",temperatures[0])
print("last reading",temperatures[-1])
print(temperatures)
print("afternoon peak")
afternoon_peak = temperatures[3:6]
print(afternoon_peak)
print("last three hours")
last_3_hours = temperatures[-3:]
print(last_3_hours)