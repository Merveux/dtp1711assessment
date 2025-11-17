records = data.split(";")
list_of_lists = [record.split(",") for record in records]
print(list_of_lists)
