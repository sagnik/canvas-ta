import csv
import sys
FILELOC='/home/szr163/Downloads/PSUWORLDCAMPUSIST230SylvesterFall2016_report_001_2016-08-24_1030.csv'

def zyBookReader(fileLoc):
    with open(fileLoc) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['Primary email'], row['Total (36)'])

def main():
    #fileLoc=sys.argv[1]
    fileLoc=FILELOC
    zyBookReader(fileLoc)
    
if __name__ == "__main__":
    main() 
       
