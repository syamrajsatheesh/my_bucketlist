import pandas as pd





# Read the Excel file
excel_file = "bucketlist.xlsx"
df = pd.read_excel(excel_file)


dic = {}


for index, row in df.iterrows():
    country = row[0]
    place = row[1]
    flag1 = str(place).lower()
    flag2 = str(row[2]).lower()

    if country not in dic.keys():
        dic[country] = []

    if flag1 != 'nan':
        # Append the country to the list associated with the place key
        dic[country].append(place)

        


# Print the data
print(dic)


