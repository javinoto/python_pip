def get_population(country_data):
  population = list(map(lambda i: [
                                i['2022 Population'],
                                i['2020 Population'],
                                i['2015 Population'],
                                i['2010 Population'],
                                i['2000 Population']
                                ], country_data))

  population_by_year = {
      '2022' : int(population[0][0]),
      '2020' : int(population[0][1]),
      '2015' : int(population[0][2]),
      '2010' : int(population[0][3]),
      '2000' : int(population[0][4])
    }
  
  labels = list(population_by_year.keys())
  values = list(population_by_year.values())
  return labels, values