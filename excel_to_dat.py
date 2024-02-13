from dat import EditFile
from excel import EditExcel




dat_path = "bucketlist.dat"
excel_path = "bucketlist.xlsx"


excel = EditExcel(excel_path)
excel_data = excel.read_from_file()

dat = EditFile(dat_path, excel_data)
dat_data = dat.overwrite_file()

data = dat.read_from_file()
print(data)