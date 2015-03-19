import json


class Dataset:
	def __init__(self, country, city, irradiance):
		"""
		Construct Dataset object
		"""
		self.country = country
		self.city = city
		self.irradiance = irradiance

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
				weatherList = datasets["list"]

				for weatherItem in weatherList:
					retValItem = Dataset(weatherItem["country"], weatherItem["city"], int(weatherItem["irradiance"]))
					retVal.append(retValItem)
		except:
			retVal = None
			
		return retVal

	@staticmethod
	def saveDatasets(filename, datasets):
		"""
		Save datasets

		param filename: filename....
		param dataset: list of datasets
		"""
		with open(filename, "w") as jsonFile:
			tmp = {
				"list": []
			}

			for dataset in datasets:
				item = {
					"country": dataset.country,
					"city": dataset.city,
					"irradiance": dataset.irradiance
				}
				tmp["list"].append(item)

			json.dump(tmp, jsonFile, indent=4, sort_keys=True)

	@staticmethod
	def getDataset(datasets, country, city):
		return list(filter(lambda x: x.country == country and x.city == city, datasets))[0]