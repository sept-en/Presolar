def getYearsOrMonths(months):
	years = months // 12
	months = months % 12
	retVal = ""

	if years != 0:
		retVal += str(years) + " years"

	if months != 0:
		retVal += " " + str(months) + " months"

	return retVal