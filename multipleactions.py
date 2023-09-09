class multiplecodes():
    def Subfields():
        print("Sub-fileds in AI are:")
        Tuple1=("Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing")
        a,b,c,d,e,f=Tuple1
        print(a)
        message=a
        print(b)
        message=b
        print(c)
        message=c
        print(d)
        message=d
        print(e)
        message=e
        print(f)
        message=f
        return message
    
    def OddEven():
        a=int(input("Enter a number:"))
        if(a%2==0):
            print(a, "is Even number")
            message=(a, "is Even number")
        else:
            print(a, "is Odd number")
            message=(a, "is Odd number")
            return message
        
    def Elegible():
        Gender=str(input("Your Gender:"))
        age=int(input("Your age:"))
        if((Gender=='Male') and (age<21)):
            print("Not Elegible")
            message="Not Elegible"
        else:
            print("Elegible")
            message="Elegible"
            return message
        
    def percentage():
        a=int(input("Subject1="))
        b=int(input("Subject2="))
        c=int(input("Subject3="))
        d=int(input("Subject4="))
        e=int(input("Subject5="))
        Marks=[a,b,c,d,e]
        print("Total:", sum(Marks))
        print("Percentage:",sum(Marks)/500.0*100)
        message=Marks
        return message
    
    def triangle():
        a=int(input("Height:"))
        b=int(input("Breadth:"))
        print("Area formula:(Height*Breadth)/2")
        print("Area of Triangle:", (a*b)/2)
        message="Area of Triangle"
        num1=int(input("Height1:"))
        num2=int(input("Height2:"))
        num3=int(input("Breadth:"))
        c=[num1,num2,num3]
        print("Perimeter formula:Height1+Height2+Breadth")
        print("Perimeter of Triangle:",sum(c))
        return message
    