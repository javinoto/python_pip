import matplotlib.pyplot as plt

def generate_bar_chart(country, labels, values):
  country_name = country.lower()
  fig, axes = plt.subplots()
  axes.bar(labels, values)
  
  plt.savefig(f'./imgs/{country_name}-bar.png')
  plt.close()

