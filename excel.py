import pandas as pd





class EditExcel:

    def __init__(self, path, data=None):
        self.data = data
        self.path = path


    def read_from_file(self):
        self.data  = pd.read_excel(self.path)

        dic = {}


        for index, row in self.data.iterrows():
            country = row[0]
            place = row[1]
            flag1 = str(place).lower()

            if country not in dic.keys():
                dic[country] = []

            if flag1 != 'nan':
                # Append the country to the list associated with the place key
                dic[country].append(place)
        return dic