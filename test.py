for num in range(5):


    for jum in range(num):
        print("o",end=' ')
    print('')
print("------------------------------------")
for num in range(5,1,-1):
    for jum in range(0,num-1):
        print(jum,end=' ')

    print('')

for i in range(0, 5):

    # inner loop to handle number spaces
    # values changing acc. to requirement
    for j in range(0, 5):
        print(end=" ")

    # decrementing k after each loop


    # inner loop to handle number of columns
    # values changing acc. to outer loop
    for j in range(0, i + 1):
        # printing stars
        print("* ", end="")

    # ending line after each row
    print(" ")
