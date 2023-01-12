#!/usr/bin/python3
initial = float(input('Please input your initial investment: '))
rate  = input('Please input your proposed yearly percentage % interest rate: ')
year = int(input('How many years is your investment: '))

print(f"Initial investment = {initial}, for a {year} year period, on a {rate}% return yearly")

rate = float(rate)/100

compound = (initial * rate) + initial

for i in range(year):
	print(f'For {i+1} years your compound return is {compound:.2f}')#converting float compound to 2 decimal places
	compound = (compound * rate) + compound
