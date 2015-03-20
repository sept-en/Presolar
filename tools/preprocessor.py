import json
import sys
import random


def preprocess(filename):
	json_data = None

	# load original json city data
	try:
		with open(filename) as original:
			json_data = json.load(original)
	except Exception as e:
		print(e)
		return

	# output file
	output_filename = filename + ".processed"
	with open(output_filename, "w") as output:
		output_json = {}

		for country in json_data.keys():
			output_json[country] = []
			cities = json_data[country]

			for city in cities:
				random_irradiance = random.randrange(800, 1500)
				city_item = {
					"city": city,
					"irradiance": random_irradiance
				}

				output_json[country].append(city_item)

		json.dump(output_json, output, indent=4, sort_keys=True)


if __name__ == '__main__':
	if len(sys.argv) < 2:
		sys.exit()

	for f in sys.argv[1:]:
		preprocess(f)