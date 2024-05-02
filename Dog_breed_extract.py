import pandas as pd
all_unique_breed = []

df = pd.read_csv('2017.csv') #reading the csv

# It will print the total number of items in a column
print("total rows",len(df))

#all_breed will get all the breeds
all_breed=df['Breed']

# for loop is for getting each breed from  all the breeds
for breed in all_breed:
    breed = breed.strip() # it will remove the whitespace from the string

    # it checks whether breed is already stored in all_unique_breed list or not. if it is not stored then it will append to the list
    if breed.lower() not in all_unique_breed:
        all_unique_breed.append(breed.lower()) #breed.lower will convert uppercase to lowercase

print("all unique breeds are", all_unique_breed) #print all unique breeds
print("total unique breed",len(all_unique_breed)) # print total unique breeds


