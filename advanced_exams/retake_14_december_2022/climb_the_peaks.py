from collections import deque

portions = [int(x) for x in input().split(', ')]
stamina = deque([int(x) for x in input().split(', ')])
peaks = deque(['Vihren', 'Kutelo', 'Banski Suhodol', 'Polezhan', 'Kamenitza'])

peaks_dict = {
    'Vihren': 80,
    'Kutelo': 90,
    'Banski Suhodol': 100,
    'Polezhan': 60,
    'Kamenitza': 70
}

conquered_peaks = []
days = 7

while portions and stamina and days > 0 and peaks:
    days -= 1
    last_portion = portions.pop()
    first_stamina = stamina.popleft()
    sum_values = last_portion + first_stamina

    current_peak = peaks[0]
    if sum_values >= peaks_dict[current_peak]:
        conquered_peaks.append(current_peak)
        peaks.popleft()
  
if not peaks:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print(f"Conquered peaks:")
    print('\n'.join(conquered_peaks))
