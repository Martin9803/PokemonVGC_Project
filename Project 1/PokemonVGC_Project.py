import csv
from collections import Counter

x = 'z'
while x != 'q':
    x = input("Please select a year you want information from or type q to quit: ")
    if x == '2009':
        with open('VGC Calculations.csv', 'r') as csv_file:
            print("1. Location Of Event.")
            print("2. Standings From Event.")
            print("3. Number of Pokemon in Top Cut.")
            print("4. Go back to year selection.")
            z = input("Which option will you select? ")
            if z == "1":
                print("\nSan Diego, California")
                print()
            if z == "2":
                f = csv.reader(csv_file)
                next(f)
                rank = 1
                for line in f:
                    if line[0] == "2009":
                        print("{}.".format(rank),line[9])
                        rank += 1
            if z == "3":
                l = []
                f = csv.reader(csv_file)
                next(f)
                for line in f:
                    if line[0] == '2009':
                        l.append(line[3])
                        l.append(line[4])
                        l.append(line[5])
                        l.append(line[6])
                        l.append(line[7])
                        l.append(line[8])
                print(Counter(l))
            if z == "4":
                continue
    if x == '2010':
        with open('VGC Calculations.csv', 'r') as csv_file:
            print("1. Location Of Event.")
            print("2. Standings From Event.")
            print("3. Number of Pokemon in Top Cut.")
            print("4. Go back to year selection.")
            z = input("Which option will you select? ")
            if z == "1":
                print("\nWaikoloa Village, Hawaii")
            if z == "2":
                f = csv.reader(csv_file)
                next(f)
                rank = 1
                for line in f:
                    if line[0] == "2010":
                        print("{}.".format(rank),line[9])
                        rank += 1
            if z == "3":
                l = []
                f = csv.reader(csv_file)
                next(f)
                for line in f:
                    if line[0] == '2010':
                        l.append(line[3])
                        l.append(line[4])
                        l.append(line[5])
                        l.append(line[6])
                        l.append(line[7])
                        l.append(line[8])
                print(Counter(l))
            if z == "4":
                continue

    if x == '2011':
        with open('VGC Calculations.csv', 'r') as csv_file:
            print("1. Location Of Event.")
            print("2. Standings From Event.")
            print("3. Number of Pokemon in Top Cut.")
            print("4. Go back to year selection.")
            z = input("Which option will you select? ")
            if z == "1":
                print("\nSan Diego, California")
                print()
            if z == "2":
                f = csv.reader(csv_file)
                next(f)
                rank = 1
                for line in f:
                    if line[0] == "2011":
                        print("{}.".format(rank),line[9])
                        rank += 1
            if z == "3":
                l = []
                f = csv.reader(csv_file)
                next(f)
                for line in f:
                    if line[0] == '2011':
                        l.append(line[3])
                        l.append(line[4])
                        l.append(line[5])
                        l.append(line[6])
                        l.append(line[7])
                        l.append(line[8])
                print(Counter(l))
            if z == "4":
                continue

    if x == '2012':
        with open('VGC Calculations.csv', 'r') as csv_file:
            print("1. Location Of Event.")
            print("2. Standings From Event.")
            print("3. Number of Pokemon in Top Cut.")
            print("4. Go back to year selection.")
            z = input("Which option will you select? ")
            if z == "1":
                print("\nWaikoloa Village, Hawaii")
                print()
            if z == "2":
                f = csv.reader(csv_file)
                next(f)
                rank = 1
                for line in f:
                    if line[0] == "2012":
                        print("{}.".format(rank),line[9])
                        rank += 1
            if z == "3":
                l = []
                f = csv.reader(csv_file)
                next(f)
                for line in f:
                    if line[0] == '2012':
                        l.append(line[3])
                        l.append(line[4])
                        l.append(line[5])
                        l.append(line[6])
                        l.append(line[7])
                        l.append(line[8])
                print(Counter(l))
            if z == "4":
                continue

    if x == '2013':
        with open('VGC Calculations.csv', 'r') as csv_file:
            print("1. Location Of Event.")
            print("2. Standings From Event.")
            print("3. Number of Pokemon in Top Cut.")
            print("4. Go back to year selection.")
            z = input("Which option will you select? ")
            if z == "1":
                print("\nVancouver, British Columbia")
                print()
            if z == "2":
                f = csv.reader(csv_file)
                next(f)
                rank = 1
                for line in f:
                    if line[0] == "2013":
                        print("{}.".format(rank),line[9])
                        rank += 1
            if z == "3":
                l = []
                f = csv.reader(csv_file)
                next(f)
                for line in f:
                    if line[0] == '2013':
                        l.append(line[3])
                        l.append(line[4])
                        l.append(line[5])
                        l.append(line[6])
                        l.append(line[7])
                        l.append(line[8])
                print(Counter(l))
            if z == "4":
                continue

    if x == '2014':
        with open('VGC Calculations.csv', 'r') as csv_file:
            print("1. Location Of Event.")
            print("2. Standings From Event.")
            print("3. Number of Pokemon in Top Cut.")
            print("4. Go back to year selection.")
            z = input("Which option will you select? ")
            if z == "1":
                print("\nWashington, D.C.")
                print()
            if z == "2":
                f = csv.reader(csv_file)
                next(f)
                rank = 1
                for line in f:
                    if line[0] == "2014":
                        print("{}.".format(rank),line[9])
                        rank += 1
            if z == "3":
                l = []
                f = csv.reader(csv_file)
                next(f)
                for line in f:
                    if line[0] == '2014':
                        l.append(line[3])
                        l.append(line[4])
                        l.append(line[5])
                        l.append(line[6])
                        l.append(line[7])
                        l.append(line[8])
                print(Counter(l))
            if z == "4":
                continue

    if x == '2015':
        with open('VGC Calculations.csv', 'r') as csv_file:
            print("1. Location Of Event.")
            print("2. Standings From Event.")
            print("3. Number of Pokemon in Top Cut.")
            print("4. Go back to year selection.")
            z = input("Which option will you select? ")
            if z == "1":
                print("\nBoston, Massachusetts")
                print()
            if z == "2":
                f = csv.reader(csv_file)
                next(f)
                rank = 1
                for line in f:
                    if line[0] == "2015":
                        print("{}.".format(rank),line[9])
                        rank += 1
            if z == "3":
                l = []
                f = csv.reader(csv_file)
                next(f)
                for line in f:
                    if line[0] == '2015':
                        l.append(line[3])
                        l.append(line[4])
                        l.append(line[5])
                        l.append(line[6])
                        l.append(line[7])
                        l.append(line[8])
                print(Counter(l))
            if z == "4":
                continue

    if x == '2016':
        with open('VGC Calculations.csv', 'r') as csv_file:
            print("1. Location Of Event.")
            print("2. Standings From Event.")
            print("3. Number of Pokemon in Top Cut.")
            print("4. Go back to year selection.")
            z = input("Which option will you select? ")
            if z == "1":
                print("\nSan Franciso, California")
                print()
            if z == "2":
                f = csv.reader(csv_file)
                next(f)
                rank = 1
                for line in f:
                    if line[0] == "2016":
                        print("{}.".format(rank),line[9])
                        rank += 1
            if z == "3":
                l = []
                f = csv.reader(csv_file)
                next(f)
                for line in f:
                    if line[0] == '2016':
                        l.append(line[3])
                        l.append(line[4])
                        l.append(line[5])
                        l.append(line[6])
                        l.append(line[7])
                        l.append(line[8])
                print(Counter(l))
            if z == "4":
                continue

    if x == '2017':
        with open('VGC Calculations.csv', 'r') as csv_file:
            print("1. Location Of Event.")
            print("2. Standings From Event.")
            print("3. Number of Pokemon in Top Cut.")
            print("4. Go back to year selection.")
            z = input("Which option will you select? ")
            if z == "1":
                print("\nAnaheim, California")
                print()
            if z == "2":
                f = csv.reader(csv_file)
                next(f)
                rank = 1
                for line in f:
                    if line[0] == "2017":
                        print("{}.".format(rank),line[9])
                        rank += 1
            if z == "3":
                l = []
                f = csv.reader(csv_file)
                next(f)
                for line in f:
                    if line[0] == '2017':
                        l.append(line[3])
                        l.append(line[4])
                        l.append(line[5])
                        l.append(line[6])
                        l.append(line[7])
                        l.append(line[8])
                print(Counter(l))
            if z == "4":
                continue

    if x == '2018':
        with open('VGC Calculations.csv', 'r') as csv_file:
            print("1. Location Of Event.")
            print("2. Standings From Event.")
            print("3. Number of Pokemon in Top Cut.")
            print("4. Go back to year selection.")
            z = input("Which option will you select? ")
            if z == "1":
                print("\nNashville, Tennessee")
                print()
            if z == "2":
                f = csv.reader(csv_file)
                next(f)
                rank = 1
                for line in f:
                    if line[0] == "2018":
                        print("{}.".format(rank),line[9])
                        rank += 1
            if z == "3":
                l = []
                f = csv.reader(csv_file)
                next(f)
                for line in f:
                    if line[0] == '2018':
                        l.append(line[3])
                        l.append(line[4])
                        l.append(line[5])
                        l.append(line[6])
                        l.append(line[7])
                        l.append(line[8])
                print(Counter(l))
            if z == "4":
                continue

    if x == '2019':
        with open('VGC Calculations.csv', 'r') as csv_file:
            print("1. Location Of Event.")
            print("2. Standings From Event.")
            print("3. Number of Pokemon in Top Cut.")
            print("4. Go back to year selection.")
            z = input("Which option will you select? ")
            if z == "1":
                print("\nWashington, D.C.")
                print()
            if z == "2":
                f = csv.reader(csv_file)
                next(f)
                rank = 1
                for line in f:
                    if line[0] == "2019":
                        print("{}.".format(rank),line[9])
                        rank += 1
            if z == "3":
                l = []
                f = csv.reader(csv_file)
                next(f)
                for line in f:
                    if line[0] == '2019':
                        l.append(line[3])
                        l.append(line[4])
                        l.append(line[5])
                        l.append(line[6])
                        l.append(line[7])
                        l.append(line[8])
                print(Counter(l))
            if z == "4":
                continue

    if x == '2022':
        with open('VGC Calculations.csv', 'r') as csv_file:
            print("1. Location Of Event.")
            print("2. Standings From Event.")
            print("3. Number of Pokemon in Top Cut.")
            print("4. Go back to year selection.")
            z = input("Which option will you select? ")
            if z == "1":
                print("\nLondon, England")
                print()
            if z == "2":
                f = csv.reader(csv_file)
                next(f)
                rank = 1
                for line in f:
                    if line[0] == "2022":
                        print("{}.".format(rank),line[9])
                        rank += 1
            if z == "3":
                l = []
                f = csv.reader(csv_file)
                next(f)
                for line in f:
                    if line[0] == '2022':
                        l.append(line[3])
                        l.append(line[4])
                        l.append(line[5])
                        l.append(line[6])
                        l.append(line[7])
                        l.append(line[8])
                print(Counter(l))
            if z == "4":
                continue

    if x == "2023":
        with open('VGC Calculations.csv', 'r') as csv_file:
            print("1. Location Of Event.")
            print("2. Standings From Event.")
            print("3. Number of Pokemon in Top Cut.")
            print("4. Go back to year selection.")
            z = input("Which option will you select? ")
            if z == "1":
                print("\nYokohama, Kanagawa")
                print()
            if z == "2":
                f = csv.reader(csv_file)
                next(f)
                rank = 1
                for line in f:
                    if line[0] == "2023":
                        print("{}.".format(rank),line[9])
                        rank += 1
            if z == "3":
                l = []
                f = csv.reader(csv_file)
                next(f)
                for line in f:
                    if line[0] == '2023':
                        l.append(line[3])
                        l.append(line[4])
                        l.append(line[5])
                        l.append(line[6])
                        l.append(line[7])
                        l.append(line[8])
                print(Counter(l))
            if z == "4":
                continue
    if x == "q":
        break
    if x == "q" or x == "2009" or x == "2010" or x == "2011" or x == "2012" or x == "2013" or x == "2014" or x == "2015" or x == "2016" or x == "2017" or x == "2018" or x == "2019" or x == "2022" or x == "2023":
        continue
    else:    
        print("Input invalid please try again.")

