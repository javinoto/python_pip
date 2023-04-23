import csv


def get_csv(path, country):
  with open(path, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    row_data = []
    
    for row in reader:
      iterable = zip(header, row)
      dic = {key : value for key, value in iterable}
      row_data.append(dic)
  
  data = list(filter(lambda item : item['Country/Territory'] == country, row_data))
  return data
