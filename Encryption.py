#Chris Elliott

#
#The program should encrypt the data by converting letter to either capital
#or lowercase of given code and then use the given function to change the digits
#and then swap the first digit with the third, the second with the fourth.
#the program should then decode the encrypted data so that it undoes the encoded message
#The program will end once the user enters q.
#Generate Ascii Function
def codealphabet(datalist):
    letter = datalist[0]
    ascii_num = ord(letter)
    if ascii_num >= 97:
        datalist.remove(letter)
        datalist.insert(0, letter.upper())
    else:
        datalist.remove(letter)
        datalist.insert(0, letter.lower())
    return datalist

#rearrange elements function
def rearrange_elements(datalist):
    #swap first and second digit
    num = datalist[3]
    datalist.insert(1, str(num))
    datalist.pop(4)
    num = datalist[2]
    datalist.insert(4, str(num))
    datalist.pop(2)
    #swap 3rd and 4th digits
    num = datalist[2]
    datalist.insert(4, str(num))
    datalist.pop(2)
    num = datalist[4]
    datalist.insert(2, str(num))
    datalist.pop(5)
    return datalist
 
#Encode function
def encodeNumber(datalist):
    #change data
    i = 1
    while i < 5:
        numlist = ((int(datalist[i]) + 7) % 10)
        #update data list
        datalist.insert(i, numlist)
        datalist.pop(i+1)
        i += 1
    #rearrange data
    #call function rearrangelemements
    rearrange_elements(datalist)
    return datalist

#Convert list to string
def listToString(datalist):
    return (''.join(datalist))

#Decode function
def decodeNumber(datalist):
    pass


        
        
#Main program   
loop_statement = True
while loop_statement == True:
    inputnum = input('(E)ncode, (D)ecode, or (Q)uit: ')
    if (inputnum == 'E') or (inputnum == 'e'):
        data = input('Enter the data to be encoded: ')
        datalist = list(data)
        encodeNumber(datalist)
        codealphabet(datalist)
        print('Encoded message:', listToString(datalist))
    elif (inputnum == 'D') or (inputnum == 'd'):
        data = input('Enter the data to be encoded: ')
        datalist = list(data)
        codealphabet(datalist)
        
    else:
        loop_statement = False
        print('Thank you for using the encryption-decryption program.')
