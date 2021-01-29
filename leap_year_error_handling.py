
## start of main

inputYear = 0

## check that input is a valid year

try:
	inputYear  = int(input("Enter a year: "))
except ValueError:
	print("Sorry, that was not an integer. Please try again.")

if inputYear <= 0 :
	print("Sorry, that was not a valid year. Please try again.")


## check if year is a leap year

if inputYear % 4 == 0 :
	if inputYear % 100 == 0:
		if inputYear % 400 == 0:
			print("{} is a leap year.".format(inputYear))
		else:
			print("{} is divisible by 100 but not 400, so it is not a leap year.".format(inputYear))
	else:
		print("{} is a leap year.".format(inputYear))

else :
	print("{} is not divisible by 4, so it is not a leap year.".format(inputYear))

