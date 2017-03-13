import math

pagesInBook = int(raw_input("How many pages are in the book? "))
pagesRead = int(raw_input("How many pages have you read already? "))
pagesLeft = pagesInBook - pagesRead
daysToRead = int(raw_input("How many days do you have to finish this book? "))

readingAmount = int(math.ceil(pagesLeft / daysToRead))

howManyReadings = int(math.ceil(pagesLeft / readingAmount))

print "\nDay 1: pg. %d to pg. %d" % (pagesRead + 1, pagesRead + readingAmount)

place = pagesRead + readingAmount + 1

for i in range(howManyReadings - 2):
	print "\nDay %d: pg. %d to pg. %d" % (i + 2, place, place + readingAmount)
	place = place + readingAmount + 1

print "\nDay %d: pg. %d to pg. %d" % (howManyReadings, place, pagesInBook)
