b_day={}
while True:
    name=input("enter the name (enter all to print all):")
    if name in b_day:
        print("birth date of "+name+" is :",b_day[name])
    elif name=='all':
         for i in b_day:
             print(i,":",b_day[i])    
    else:
        x=input("name not found in the dictionary if you want to add (y/n)")
        if x=='y':
            dte=input("enter the date of birth(dd/mm/yyyy):")
            b_day.update({name:dte})
        elif x=='n':
            exit()
        else:
            print("Invalid operator!")