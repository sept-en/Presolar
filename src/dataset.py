import json


class Dataset:
	def __init__(self, country, city, irradiance, powerPrice):
		"""
		Construct Dataset object
		"""
		self.country = country
		self.city = city
		self.irradiance = irradiance
		self.powerPrice = powerPrice

	def __str__(self):
		return "Country: " + self.country + "; City: " + self.city + "; Irradiance: " + str(self.irradiance)

	@staticmethod
	def loadDatasets(filename):
		"""
		Load JSON weather data

		param filename: filename...
		"""

		retVal = []

		try:
			with open(filename) as jsonData:
				datasets = json.load(jsonData)
				
				for country in datasets.keys():
					# currently, power price is in the cents,
					# convert it to dollars
					for cityItem in datasets[country]:
						retValItem = Dataset(country, cityItem["city"], 
							int(cityItem["irradiance"]), int(cityItem["price"]) / 100)
						retVal.append(retValItem)
		except:
			retVal = None
			
		return retVal

	@staticmethod
	def getCountries(datasets):
		"""
		Get all countries in datasets. TODO: redo comment
		"""
		countries = set()

		for dataset in datasets:
			countries.add(dataset.country)

		retVal = list(countries)
		retVal.sort()
		return retVal

	@staticmethod
	def getCitiesByCountry(datasets, country):
		"""
		Get cities in @country
		"""
		retVal = [dataset.city for dataset in datasets if dataset.country == country]
		retVal.sort()
		return retVal

	@staticmethod
	def getDataset(datasets, country, city):
		"""
		Get dataset with given country and city
		"""
		return list(filter(lambda x: x.country == country and x.city == city, datasets))[0]
