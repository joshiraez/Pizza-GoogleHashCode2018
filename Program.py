def readPizza(file):
	with open(file) as file:
		rowSize, colSize, minStuff, maxStuff = [ int(data) for data in file.readline().split(' ')]
		pizza = []
		for line in file:
			pizza.append([0 if letter=='T' else 1 for letter in line.strip()])

		return rowSize, colSize, minStuff, maxStuff, pizza

rowSize, colSize, minStuff, maxStuff, pizza = readPizza('small.in')

possibleSegments = []
for startRow in range(0, rowSize):
	for endRow in range(startRow, rowSize):
		for startCol in range(0, colSize):
			for endCol in range(startCol, colSize):
				area = (endRow - startRow + 1) * (endCol - startCol + 1)
				if minStuff * 2 <= area <= maxStuff:
					ingredients = 0
					for iRow in range(startRow, endRow+1):
						for iCol in range(startCol, endCol+1):
							ingredients += pizza[iRow][iCol]
					if minStuff == ingredients or ingredients == area-minStuff:
						segmentFound = (startRow, endRow, startCol, endCol, area)
						possibleSegments.append(segmentFound)

def checkValid(currentSegments, segment):
	for otherSegment in currentSegments:
		if( not (segment[1] < otherSegment[0] or segment[0] > otherSegment[1] or
				 segment[3] < otherSegment[2] or segment[2] > otherSegment[3] ) ):
			return False
	return True

print(possibleSegments)
print(len(possibleSegments))

#The next function looks ugly because I had some problems with how python handles variables. I have to improve it.
def lookValidSegments(currentSegments, currentArea, iterator):
	maxArea = currentArea
	maxSegments = currentSegments

	for i in range(iterator, len(possibleSegments)):
		segment = possibleSegments[i]
		if checkValid(currentSegments, segment):
			max = lookValidSegments(currentSegments+[segment], currentArea+segment[4], i+1)
			if max[1] > maxArea:
				maxSegments = max[0]
				maxArea = max[1]
				print(maxArea, maxSegments)

	return maxSegments, maxArea

print(lookValidSegments([], 0, 0))
