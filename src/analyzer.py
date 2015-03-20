import dataset


class Analyzer:
	def __init__(self, datasetsFilename):
		self.datasets = dataset.Dataset.loadDatasets(datasetsFilename)

		if self.datasets is None:
			raise Exception("Invalid datasets file or file is missing.")

	def predict(self, country, city, pw=400, areaOfPanel=1, panelCount=10):
            cityDataset = dataset.Dataset.getDataset(self.datasets, country, city)
            energyPerYear = Analyzer.getEnergyPerYear(cityDataset.irradiance, pw, areaOfPanel)
            energyPerHour = energyPerYear / 12 / 30 / 24
            energyPerHour *= panelCount

            installationCostOfPanel = 15
            costOfPanel = (250 + installationCostOfPanel) * panelCount
            costPerHour = 0.05
            paybackTermMonths = Analyzer.getPaybackTerm(energyPerHour, costOfPanel, costPerHour)
            return energyPerHour, paybackTermMonths

	@staticmethod
	def getEnergyPerYear(irradiance, pw, area, lossesRatio=0.75):
            # convert watts to kW
            pw /= 1000
            
            r = pw #/ area
            energyPerYear = area * r * irradiance * lossesRatio
            return energyPerYear

	@staticmethod
	def getPaybackTerm(energyPerHour, costOfPanel, costPerHour):
		costPerMonth = costPerHour * energyPerHour * 24 * 30

		monthsCount = 1
		while (costPerMonth * monthsCount) < costOfPanel:
			monthsCount += 1

		return monthsCount
