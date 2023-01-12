if __name__ == "__main__":
    report = open("input.txt").read().strip().split("\n")
    report_ox = report[:] 
    for col in range(len(report[0])):
        more_ones = sum(int(report_ox[j][col]) for j in range(len(report_ox)))*2>=len(report_ox)
        report_ox = [row for row in report_ox if int(row[col]) == more_ones]
        if len(report_ox) == 1:
            report_ox = int(report_ox[0], 2)
            break
    report_co2 = report[:]
    for col in range(len(report[0])):
        more_ones = sum(int(report_co2[j][col]) for j in range(len(report_co2)))*2>=len(report_co2)
        report_co2 = [row for row in report_co2 if int(row[col]) != more_ones]
        if len(report_co2) == 1:
            report_co2 = int(report_co2[0], 2)
            break
    print(report_ox*report_co2)
