def main():
	months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	rain_list = []

	total = 0

	for n in months:
		rain = float(input(f'Enter the amount of rain for {n}: '))
		rain_list.append(rain)
		total += rain

	average = total / len(rain_list)
	least = min(rain_list)
	most = max(rain_list)
	least_rain_index = rain_list.index(least)
	most_rain_index = rain_list.index(most)

	print('The total rain in the entire year was' , total)
	print('The average rain was' , average)
	print(f'The month with the lowest amount of rain was: {months[least_rain_index]}, {least} inches')
	print(f'The month with the highest amount of rain was: {months[most_rain_index]}, {most} inches')

	write('yearly_rain.txt', rain_list, total, months, average, least, most, least_rain_index, most_rain_index)


def write(name, list, total, months, average, least, most, least_rain_index, most_rain_index):
	output = open(name, 'w')

	index = 0
	for rain in list:
		output.writelines(f'{months[index]}: {rain} inches\n')
		index += 1

	output.writelines(f'Total rain: {total} inches\n')
	output.writelines(f'Average rain: {average} inches\n')
	output.writelines(f'The month with the lowest amount of rain was: {months[least_rain_index]}, {least} inches\n')
	output.writelines(f'The month with the highest amount of rain was: {months[most_rain_index]}, {most} inches\n')

main()