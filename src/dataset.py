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