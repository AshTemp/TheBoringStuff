twinkies = input('How many twinkies do you have:')
converted_twinkies = int(twinkies)
if converted_twinkies < 100 or converted_twinkies > 500:
    print ('Too few or too many')
else:
    print ('Just enough twinkies')