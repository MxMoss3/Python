height = int(input("How high?(0-23)"))

#checks if the input is valid before continuing
input_good = False
while input_good == False:
    if height < 0 or height > 23:
        height = int(input("How high?(0-23)"))
        pass
    else:
        input_good = True

#prints the stairs
for i in range(height):
    print((' ' * (height - (i + 1))) + 
            ('#' * (i + 1)) +
            ('  ') + 
            ('#' * (i + 1)) +
            (' ' * (height - (i + 1))))  
