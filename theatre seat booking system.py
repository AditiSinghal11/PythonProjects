#theatre seat booking system
#print 25 seats
#ask user to select single seat or multiple
#multiple=multiple random selection or multiple selection from the same row(from where to wear)
#selected sseat shud appear as b
a=[[1,2,3,4,5],
   [6,7,8,9,10],
   [11,12,13,14,15],
   [16,17,18,19,20],
   [21,22,23,24,25]]
booked='B'
for row in a:
    print (row)
d=input("do u want multiple or single seat booking")
if d=='single':
    r=int(input("which row"))
    c=int(input("which column"))
    a[r-1][c-1]=booked
    for row in a:
        print (row)
else:
    s=input("m for multiple selection from anywhere or n for multiple selection from the same row")
    choice=int(input("enter how many seats u want"))
    if s=='m':
        dang=int(input("enter the row you wanna book:"))
        col=int(input("enter the col you wanna book:"))
        def theatre(dang,col):
            a[dang-1][col-1]=booked
        for i in choice:
            theatre(dang,col)

    if s=='n':
        print("selection of the seats from which row")
        v=int(input("which row"))
        j=int(input("enter intial seat from the range"))
        g=int(input("enter the last seat from the range"))
        for kill in len(a):
            for dude in len(a[0]):
                    if j==a[kill][dude]:
                        a[kill][dude]==booked
                        for man in  len(a):
                            for women in len(a[0]):
                                if g==a[man][women]:
                                    a[man][women]==booked
                                while women!=0:
                                    women-=1
                                    a[man][women]==booked
        for row in a :
            print(row)
            print("your seat has been booked")

        
                    


    

   
       

    
