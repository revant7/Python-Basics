
while True:
    print('press q to quit')
    i = input("Enter A Number : ")
    if i == 'q':
        print('Thanks For Playing This Game!')
        break
    try:
        if int(i)>6:
            print('You Entered a Number Greater Then 6.')

    except Exception as e:
        print(e)
    
    

         
