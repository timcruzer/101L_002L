num_Value=0
def get_school(lib_card):
    if lib_card[5]=='1':
       return ("School of Computing and Engineering SCE")
    elif lib_card[5]=='2':
        return ("School of Law")
    elif lib_card[5]=='3':
        return ("College of Arts and Sciences")
    else:
        return ("Invalid School")
def get_grade(lib_card):
    if lib_card[6]=='1':
        return ("Freshman")
    elif lib_card[6]=='2':
        return ("Sophomore")
    elif lib_card[6]=='3':
        return ("Junior")
    elif lib_card[6]=='4':
        return ("Senior")
    else:
        return ("Invalid Grade")
def character_value(c):
    num_Value=ord(c)
    if(num_Value>=48 and num_Value<=57):
        return num_Value-48
    elif(num_Value>=65 and num_Value<=90):
        return num_Value-65
def get_check_dig(lib_card):
    sum=0
    for i in range(len(lib_card)):
        num_Value=character_value(lib_card[i])
        sum+=num_Value*(i+1)
    return sum%10
def verify_check_dig(lib_card):
    if len(lib_card)!=10:
        error_to_read='The length of the number given must be 10'
        return (False,error_to_read)
    for i in range(5):
        if lib_card[i]<"A"or lib_card>'Z':
            error_to_read="The first 5 characters must be A-Z, the invalid character is at index"
            return(False,error_to_read,i,'is', lib_card[i])
    for i in range(7,10):
        if lib_card[i]<'0' or lib_card[i]>'9':
            error_to_read='The last three characters must be 0-9, the invalid character is at'
            return(False,error_to_read,i,'is',lib_card[i])
        elif lib_card[5]!='1' and lib_card[5]!='2' and lib_card[5]!='3':
            error_to_read="The sixth character must be 1, 2, or 3"
            return(False,error_to_read)
        elif lib_card[6]!='1' and lib_card[6]!='2' and lib_card[6]!='3' and lib_card[6]!='4':
            error_to_read='The seventh chacter must be 1, 2, 3, or 4'
            return(False,error_to_read)
        this_value=int(lib_card[9])
        correct_value=get_check_dig(lib_card)
        if this_value!=correct_value:
            error_to_read='Check Digit',str(this_value),'does not match calculated value',str(correct_value)
            return(False,error_to_read,num_Value)
    return(True,'Library card is valid.')
def main():
    while(1):
        lib_card=input('Enter Library Card. Hit Enter to Exit ==>')
        is_valid,error_to_read=verify_check_dig(lib_card)
        
        if is_valid==True:
            print(error_to_read)
            print('The card belongs to a student in', get_school(lib_card))
            print("The card belongs to a",get_grade(lib_card))
        else:
            print("Library card is invalid")
            print(error_to_read)
if __name__=="__main__":
    main()