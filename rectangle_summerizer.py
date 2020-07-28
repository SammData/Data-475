import csv
from statistics import mean

with open("rectangles.csv", newline="") as f:
    reader = csv.reader(f)
    next(reader)

    # List Comprehension
    areas = [float(line[1]) * float(line[2]) for line in reader]
    # for line in reader:
    #     print(line)
    #     w = float(line[1])
    #     l = float(line[2])
    #     area = w * l
    #     areas.append(area)
        
    print(max(areas))
    print(min(areas))
    print(sum(areas))
    print(mean(areas))
    print(len(areas))

    column_names = {
        "Total Count": len(areas),
        "Total Area": sum(areas),
        "Ave area": mean(areas),
        "Max area": max(areas),
        "Min area": min(areas),
    }

for key, value in column_names.items():
    print(f"{key}: {value}")

with open("summary.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(column_names.keys())
    writer.writerow(column_names.values())