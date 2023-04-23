# Proyecto: Crear app con módulos
import read_csv, utils, charts

def run(path, country):
  country_data = read_csv.get_csv(path, country)
  labels, values = utils.get_population(country_data)
  charts.generate_bar_chart(country, labels, values)
  

if __name__ == '__main__':
  path = './data.csv'
  country = input('Ingresa el nombre del país: ')
  run(path, country)