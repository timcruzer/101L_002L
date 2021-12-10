import math
def total(values):
    total = 0
    for num in values:
        total+=num
    return float(total)
def average(values):
    if len(values) == 0:
        return math.nan
    total = 0
    for num in values:
        total+=num
    return float(total / len(values))
def median(values):
    values.sort()
    center = len(values) / 2
    if center // 1 == center: 
        return (values[int(center - 0.5)] + values[int(center + 0.5)]) / 2
    else: 
        return values[int(center)]