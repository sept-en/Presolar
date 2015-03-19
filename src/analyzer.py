import dataset


class Analyzer:
	def __init__(self, datasetsFilename):
		self.datasets = dataset.Dataset.loadDatasets(datasetsFilename)

		if self.datasets is None:
			raise Exception("Invalid datasets file or file is missing.")

	def predict(self, country, city):
		cityDataset = Dataset.getDataset(datasets, country, city)
		energyPerHour = getEnergyPerHour(cityDataset.irradiance, 100, 1)
		costOfPanel = 400
		costPerHour = 0.01
		paybackTermMonths = getPaybackTerm(energyPerHour, costOfPanel, costPerHour)
		return energyPerHour, paybackTermMonths

	@staticmethod
	def getEnergyPerHour(irradiance, pw, area, lossesRatio=0.75):
		r = pw / area
		energyPerHour = r * irradiance * lossesRatio
		return energyPerHour

	@staticmethod
	def getPaybackTerm(energyPerHour, costOfPanel, costPerHour):
		costPerMonth = costPerHour * 24 * 30
		energyPerMonth = energyPerHour * 24 * 30

		monthsCount = 1
		while (costPerMonth * monthsCount) < costOfPanel:
			monthsCount += 1

		return monthsCount
