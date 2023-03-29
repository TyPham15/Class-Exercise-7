def main():
	names = ['Howard','Jamie','Jill']

	print('the list before the insert or remove')
	print(names)

	NameRemove = input('enter the name to remove ')

	names.insert(0,'Joe')
	
	names.remove(NameRemove)
	
	print('the list after the insert')
	print(names)
#main()

def total():
	numbers = [1,2,3,4,5,6,7,8,9,10]
	sum = 0

	for value in numbers:
		sum+=value

	average = sum / len(numbers)
	print(f'the total is {sum}, the average is {average}')

	file = open('numbers.txt', 'w')
	file.writelines(str(numbers) + '\n')
	file.write(str(sum) + '\n')
	file.write(str(average) + '\n')
total()