import pandas as pd
df = pd.read_csv('2017.csv')
# print(df.head)
print(df['ValidDate'])
print(df[df['ValidDate'] != " "])
all_dat=df[df['ValidDate'] != " "]
print("alldog bree", all_dat['Breed'])

# data = dataset.iloc[:,1,:2].values
# print(data)


# import csv
#
# with open('2017.csv') as csvfile:
#     heading = next(csvfile)
#     csv_reader = csv.reader(csvfile)
#     for row in csv_reader:
#         print(row)


# f= open('2017.csv','r')
# ro= csv.reader(f,delimiter= ',')
# ld= list(ro)
# for row in ld:
#     print(row[3])
    # print(row)
