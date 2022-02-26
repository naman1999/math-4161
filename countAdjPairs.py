# Naman Gera, York University 215515539
def countPairs(str) :

	count = 0
	n = len(str)
	for i in range(n - 1) :
		if (str[i] == str[i+1]) :
			count += 1

	return count

if __name__ == "__main__" :
	
    str = input("Enter text: ")
#print("There are " + countPairs(str) + "pairs and the number of characters is " + len(str))
print(countPairs(str))
print(len(str))