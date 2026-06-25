import numpy as np
class DataAnalytics:
    __arr = None
    def __init__(self):
        self.__arr = None
        self.__TwoD = None
        self.__OneD = None
        self.__ThreeD = None
        self.splitarr = None
        self.ser = None
        self.r = None
        self.c = None
        self.l = None

    def Array_Management(self):
        while True:
            print("Select The Type Of Array To Create")
            print("1 . 1D Array")
            print("2 . 2D Array")
            print("3 . 3D Array")
            print("4 . Exit")

            ch = int(input("Enter Your Choice "))

            if ch == 1:
                self.__One_D_Array()
                break

            elif ch ==2:    
               self.__Two_D_Array()
               break

            elif ch == 3:
                self.__Three_D_Array()

                break

            elif ch == 4:
                break 

            else:
                print("Invalid Input...") 
                     


    def __One_D_Array(self):
        lenght = int(input("Enter Your Lenght Of Array"))
        self.__arr = np.empty((lenght),dtype=int)
        for i in range(lenght):
                self.__arr[i] = int(input("Enter Element"))

        
        self.__OneD = self.__arr  
        self.splitarr = self.__arr   
        self.ser = self.__OneD
        DataAnalytics.__arr = self.__OneD


        print("Array Created Successfully....")       
        print(self.__OneD)  
        print()
        while True:
            print("Choose An Operation")
            print("1 . Indexing")
            print("2 . Slicing")
            print("3 .Go Back")

            ch = int(input("Enter Your Choice"))
            if ch ==1 :
                s = int(input("Enter your  Index Number"))
                print()
                print("Indexing Array")
                try:
                  print(self.__OneD[s])
                except IndexError as e :
                    print(e)  
   

            elif ch ==2 : 
                s = int(input("Enter Starting Slicing Range"))
                e1 = int(input("Enter Ending Slicing Range"))
                print()
                print("sliced Array")
                if s >=e1:
                  print("Invalid Range")
                else:  
                  print(self.__OneD[s:e1])

               
               

            elif ch == 3:
                break
            else:
                print("Invalid Input")        
   

    def __Two_D_Array(self):
        row = int(input("Enter Your Row"))
        col = int(input("Enter Your Cloumn"))
        self.r = row
        self.c = col
        self.__arr = np.empty((row,col),dtype=int)
        print(f"Total [ {row*col}  ] Element Enter ")
        for i in range(row):
            for j in range(col):
                self.__arr[i][j] = int(input(f"Enter element")) 

       
        self.__TwoD = self.__arr 
        self.splitarr = self.__arr
        self.ser = self.__TwoD
        DataAnalytics.__arr = self.__TwoD

        print("Array Created Successfully....")
        print(self.__TwoD)
        print()
        while True:
            print("Choose An Operation")
            print("1 . Indexing")
            print("2 . Slicing")
            print("3 .Go Back")

            ch = int(input("Enter Your Choice"))
            if ch ==1 :
                s = int(input("Enter your row  Index Number"))
                e1 = int(input("Enter Your Column Index Number"))
                print()
                print("Indexing Array")
                try:
                 print(self.__TwoD[s,e1])
                except IndexError as e:
                    print(e) 

            elif ch ==2 : 
                s = int(input("Enter  Row  Slicing Range (start)"))
                s2 = int(input("Enter  Row  Slicing Range (end)"))
                e1 = int(input("Enter Cloumn Slicing Range (start)"))
                e2 = int(input("Enter Cloumn Slicing Range (end)"))
                print()
                print("sliced Array")
                if s>=s2 or e1>e2:
                    print("Invalid Range")
                else:    
                   print(self.__TwoD[s:s2,e1:e2])
                
            elif ch == 3:
                break
            else:
                print("Invalid Input")


    def __Three_D_Array(self):
        layer = int(input("Enter Your Layer"))  
        row = int(input("Enter Your Row"))
        col = int(input("Enter Your Cloumn"))
        self.r = row
        self.c = col
        self.l = layer
        self.__arr = np.empty((layer,row,col),dtype=int) 
        print(f"Total [ {layer*row*col}  ] Element Enter ") 
        for i in range(layer):
            for j in range(row):
                for k in range(col):
                    self.__arr[i][j][k] = int(input("Enter Your Element"))

        
        self.__ThreeD = self.__arr
        self.splitarr = self.__arr
        self.ser = self.__ThreeD
        DataAnalytics.__arr = self.__ThreeD


        print("Array Created Successfully....")
        print(self.__ThreeD)    
        print()
        while True:
            print("Choose An Operation")
            print("1 . Indexing")
            print("2 . Slicing")
            print("3 .Go Back")

            ch = int(input("Enter Your Choice"))
            if ch ==1 :
                l = int(input("Enter Your Layer"))
                s = int(input("Enter your row  Index Number"))
                e1 = int(input("Enter Your Column Index Number"))
                print()
                print("Indexing Array")
                try:
                   print(self.__ThreeD[s,e1,l])

                except IndexError as e:
                    print(e)   

                

            elif ch ==2 : 
                l = int(input("Enter Your Layer"))
                s = int(input("Enter  Row  Slicing Range (start)"))
                s2 = int(input("Enter  Row  Slicing Range (end)"))
                e1 = int(input("Enter Cloumn Slicing Range (start)"))
                e2 = int(input("Enter Cloumn Slicing Range (end)"))
                print()
                print("sliced Array")
                if s>=s2 or e1>=e2:
                  print("Invalid Range")
                else:   
                  print(self.__ThreeD[l,s:s2,e1:e2])
   

            elif ch == 3:
                break
            else:
                print("Invalid Input")     

    def Mathematical_Operations(self):
        while True:
            print("Select The Type Of Array To Create")
            print("1 . Addtion")
            print("2 . Subtraction")
            print("3 . Multiplication")
            print("4 . Division")
            print("5.  Exit")

            ch = int(input("Enter Your Choice "))

            if ch == 1:
                  print(" Addtion ")
                  print("Select The Same Size Array")
                  self.__Addtion()

            elif ch ==2:    
                 print(" Subtraction ")
                 print("Select The Same Size Array")
                 self.__Subtraction()

            elif ch == 3:
                print(" Multiplication ")
                print("Select The Same Size Array")
                self.__Multiplication()

            elif ch == 4:     
                print(" Division ")
                print("Select The Same Size Array")
                self.__Division()

            elif ch == 5:
                break
              

            else:
                print("Invalid Input...") 

    def __Addtion(self):
            self.OneD1 = None
            self.TwoD1 = None
            while True:
                print("Select The Type Of Array To Addtion")
                print("1 . 1D Array")
                print("2 . 2D Array")
                print("3 . 3D Array")
                print("4 . Exit")

                ch = int(input("Enter Your Choice "))

                if ch == 1:
                    l= len(self.__OneD)
                    print(f"Enter the Same Size Array Element ({l} Element Separated By Space)")
                    self.__arr = np.empty((l),dtype=int)
                    for i in range(l):
                            self.__arr[i] = int(input("Enter Element"))


                    self.OneD1 = self.__arr             

                    print("Original Array")
                    print(self.__OneD)

                    print("Second Array")
                    print(self.OneD1)

                    print("Result Of Addition")
                    print(self.OneD1+self.__OneD)

                    break

                elif ch ==2:  

                  if self.__TwoD is None:
                    print("Please Create 2D Array First...")
                    break  
                  
                  r,c = self.__TwoD.shape  
                  self.__arr = np.empty((r,c),dtype=int)
                  print(f" Enter Same Size Array Elements  [ {r*c}  ] Element Separated By Space ")
                  for i in range(r):
                        for j in range(c):
                            self.__arr[i][j] = int(input(f"Enter element")) 

                  self.TwoD1 = self.__arr 
                  print("Original Array")
                  print(self.__TwoD)
                  
                  print()

                  print("Second Array")
                  print(self.TwoD1)

                  print()
                  
                  print("Result Of Addtion")
                  print(self.TwoD1+self.__TwoD)
                  print(len(self.__TwoD))

                  break



                elif ch == 3:
                    self.ThreeD1 = None
                    self.__arr = np.empty((self.l,self.r,self.c),dtype=int) 
                    print(f"Total [ {self.l*self.r*self.c}  ] Element Enter ") 
                    for i in range(self.l):
                        for j in range(self.r):
                            for k in range(self.c):
                                self.__arr[i][j][k] = int(input("Enter Your Element"))


                    self.ThreeD1 = self.__arr
                    print("Original Array ")
                    print(self.__ThreeD) 

                    print()
                    print("Second Array")
                    print(self.ThreeD1)

                    print("Result Of Addtion")
                    print(self.ThreeD1 + self.__ThreeD) 

                    break

                elif ch == 4:
                    break 

                else:
                    print("Invalid Input...")


    def __Subtraction(self):
            self.OneD1 = None
            self.TwoD1 = None
            while True:
                print("Select The Type Of Array To Subtraction")
                print("1 . 1D Array")
                print("2 . 2D Array")
                print("3 . 3D Array")
                print("4 . Exit")

                ch = int(input("Enter Your Choice "))

                if ch == 1:
                    l= len(self.__OneD)
                    print(f"Enter the Same Size Array Element ({l} Element Separated By Space)")
                    self.__arr = np.empty((l),dtype=int)
                    for i in range(l):
                            self.__arr[i] = int(input("Enter Element"))


                    self.OneD1 = self.__arr             

                    print("Original Array")
                    print(self.__OneD)

                    print("Second Array")
                    print(self.OneD1)

                    print("Result Of Subtraction")
                    print(self.OneD1-self.__OneD) 

                    break

                elif ch ==2:  
                    
                  self.__arr = np.empty((self.r,self.c),dtype=int)
                  print(f" Enter Same Size Array Elements  [ {self.r*self.c}  ] Element Separated By Space ")
                  for i in range(self.r):
                        for j in range(self.c):
                            self.__arr[i][j] = int(input(f"Enter element")) 

                  self.TwoD1 = self.__arr 
                  print("Original Array")
                  print(self.__TwoD)
                  
                  print()

                  print("Second Array")
                  print(self.TwoD1)

                  print()
                  
                  print("Result Of Subtraction")
                  print(self.TwoD1-self.__TwoD)
                  print(len(self.__TwoD))

                  break



                elif ch == 3:
                    self.ThreeD1 = None
                    self.__arr = np.empty((self.l,self.r,self.c),dtype=int) 
                    print(f"Total [ {self.l*self.r*self.c}  ] Element Enter ") 
                    for i in range(self.l):
                        for j in range(self.r):
                            for k in range(self.c):
                                self.__arr[i][j][k] = int(input("Enter Your Element"))


                    self.ThreeD1 = self.__arr
                    print("Original Array ")
                    print(self.__ThreeD) 

                    print()
                    print("Second Array")
                    print(self.ThreeD1)

                    print("Result Of Subtraction")
                    print(self.ThreeD1 - self.__ThreeD)

                    break


                elif ch == 4:
                    break 

                else:
                    print("Invalid Input...")  

    def __Multiplication(self): 
        self.OneD1 = None
        self.TwoD1 = None
        while True:
                print("Select The Type Of Array To Multiplication")
                print("1 . 1D Array")
                print("2 . 2D Array")
                print("3 . 3D Array")
                print("4 . Exit")

                ch = int(input("Enter Your Choice "))

                if ch == 1:
                    l= len(self.__OneD)
                    print(f"Enter the Same Size Array Element ({l} Element Separated By Space)")
                    self.__arr = np.empty((l),dtype=int)
                    for i in range(l):
                            self.__arr[i] = int(input("Enter Element"))


                    self.OneD1 = self.__arr             

                    print("Original Array")
                    print(self.__OneD)

                    print("Second Array")
                    print(self.OneD1)

                    print("Result Of Multiplication")
                    dot1 = np.dot(self.OneD1,self.__OneD)
                    print(dot1)

                    break

                elif ch ==2:  
                    
                  self.__arr = np.empty((self.r,self.c),dtype=int)
                  print(f" Enter Same Size Array Elements  [ {self.r*self.c}  ] Element Separated By Space ")
                  for i in range(self.r):
                        for j in range(self.c):
                            self.__arr[i][j] = int(input(f"Enter element")) 

                  self.TwoD1 = self.__arr 
                  print("Original Array")
                  print(self.__TwoD)
                  
                  print()

                  print("Second Array")
                  print(self.TwoD1)

                  print()
                  
                  print("Result Of Multiplication")
                  dot2 = np.dot(self.__TwoD,self.TwoD1.T)
                  print(dot2)
                  

                  break

                elif ch == 3:
                    self.ThreeD1 = None
                    self.__arr = np.empty((self.l,self.r,self.c),dtype=int) 
                    print(f"Total [ {self.l*self.r*self.c}  ] Element Enter ") 
                    for i in range(self.l):
                        for j in range(self.r):
                            for k in range(self.c):
                                self.__arr[i][j][k] = int(input("Enter Your Element"))


                    self.ThreeD1 = self.__arr
                    print("Original Array ")
                    print(self.__ThreeD) 

                    print()
                    print("Second Array")
                    print(self.ThreeD1)

                    print("Result Of Multiplication ")
                    dot3 = np.dot(self.ThreeD1 ,self.__ThreeD)
                    print(dot3)

                    break

                elif ch == 4:
                    break 

                else:
                    print("Invalid Input...")  
    def __Division(self): 
        self.OneD1 = None
        self.TwoD1 = None
        while True:
                print("Select The Type Of Array To Division")
                print("1 . 1D Array")
                print("2 . 2D Array")
                print("3 . 3D Array")
                print("4 . Exit")

                ch = int(input("Enter Your Choice "))

                if ch == 1:
                    l= len(self.__OneD)
                    print(f"Enter the Same Size Array Element ({l} Element Separated By Space)")
                    self.__arr = np.empty((l),dtype=int)
                    for i in range(l):
                            self.__arr[i] = int(input("Enter Element"))


                    self.OneD1 = self.__arr             

                    print("Original Array")
                    print(self.__OneD)

                    print("Second Array")
                    print(self.OneD1)

                    print("Result Of Division")
                    print(self.OneD1/self.__OneD)

                    break

                elif ch ==2:  
                    
                  self.__arr = np.empty((self.r,self.c),dtype=int)
                  print(f" Enter Same Size Array Elements  [ {self.r*self.c}  ] Element Separated By Space ")
                  for i in range(self.r):
                        for j in range(self.c):
                            self.__arr[i][j] = int(input(f"Enter element")) 

                  self.TwoD1 = self.__arr 
                  print("Original Array")
                  print(self.__TwoD)
                  
                  print()

                  print("Second Array")
                  print(self.TwoD1)

                  print()
                  
                  print("Result Of Division")
                  print(self.TwoD1/self.__TwoD)
                  print(len(self.__TwoD))


                  break


                elif ch == 3:
                    self.ThreeD1 = None
                    self.__arr = np.empty((self.l,self.r,self.c),dtype=int) 
                    print(f"Total [ {self.l*self.r*self.c}  ] Element Enter ") 
                    for i in range(self.l):
                        for j in range(self.r):
                            for k in range(self.c):
                                self.__arr[i][j][k] = int(input("Enter Your Element"))


                    self.ThreeD1 = self.__arr
                    print("Original Array ")
                    print(self.__ThreeD) 

                    print()
                    print("Second Array")
                    print(self.ThreeD1)

                    print("Result Of Division ")
                    print(self.ThreeD1 /self.__ThreeD)


                    break

                elif ch == 4:
                    break 

                else:
                    print("Invalid Input...")   

    def Combine_Or_Split_Array(self):
        while True:
            print("Choose An Option")
            print("1) Combine Array")
            print("2) Split Array")
            print("3) Exit")

            ch = int(input("Enter Your Choice"))

            if ch==1:
                print("1) Combine Array")
                self.OneD1 = None
                self.TwoD1 = None
                while True:
                    print("Select The Type Of Array To Combined")
                    print("--------------------------------------")
                    print("Select Same Array Type")
                    print("1 . 1D Array")
                    print("2 . 2D Array")
                    print("3 . 3D Array")
                    print("4 . Exit")

                    ch = int(input("Enter Your Choice "))

                    if ch == 1:
                        l= len(self.__OneD)
                        print(f"Enter the Same Size Array Element ({l} Element Separated By Space)")
                        self.__arr = np.empty((l),dtype=int)
                        for i in range(l):
                                self.__arr[i] = int(input("Enter Element"))


                        self.OneD1 = self.__arr             

                        print("Original Array")
                        print(self.__OneD)

                        print()

                        print("Second Array")
                        print(self.OneD1)

                        print()
                        print("Cloumn Vise Combined")
                        print(np.concatenate((self.__OneD,self.OneD1),axis=0))
                               

                        break       

                    elif ch ==2:  
                        r ,c = self.__TwoD.shape
                        self.__arr = np.empty((r,c),dtype=int)
                        print(f" Enter Same Size Array Elements  [ {r*c}  ] Element Separated By Space ")
                        for i in range(r):
                                for j in range(c):
                                    self.__arr[i][j] = int(input(f"Enter element")) 

                        self.TwoD1 = self.__arr 
                        print("Original Array")
                        print(self.__TwoD)
                        
                        print()

                        print("Second Array")
                        print(self.TwoD1)

                        print()

                        
                        while True:
                            print("Combined Array")
                            print("1) Cloumn Vise Combined")
                            print("2) Row Vise Combined")
                            print("3) Exit")
                            ch1 = int(input("Enter Your Choice"))
                            match ch1:

                                case  1:
                                    print("Cloumn Vise Combined")
                                    print(np.concatenate((self.__TwoD,self.TwoD1),axis=0))
                                case 2 :
                                    print("Row Vise Combined")
                                    print(np.concatenate((self.__TwoD,self.TwoD1),axis=1))
                                case 3:
                                    break
                                case _:
                                 print("Invalid Input")   
                        break

                    elif ch == 3:
                        self.ThreeD1 = None
                        l,r,c = self.ThreeD1.shape
                        self.__arr = np.empty((l,r,c),dtype=int) 
                        print(f"Total [ {l*r*c}  ] Element Enter ") 
                        for i in range(l):
                            for j in range(r):
                                for k in range(c):
                                    self.__arr[i][j][k] = int(input("Enter Your Element"))


                        self.ThreeD1 = self.__arr
                        print("Original Array ")
                        print(self.__ThreeD) 

                        print()
                        print("Second Array")
                        print(self.ThreeD1)

                        while True:
                            print("Combined Array")
                            print("1) Cloumn Vise Combined")
                            print("2) Row Vise Combined")
                            print("3) Exit")
                            ch1 = int(input("Enter Your Choice"))
                            match ch1:

                                case  1:
                                    print("Cloumn Vise Combined")
                                    print(np.concatenate((self.__ThreeD,self.ThreeD1),axis=0))
                                case 2 :
                                    print("Row Vise Combined")
                                    print(np.concatenate((self.__ThreeD,self.ThreeD1),axis=1))
                                case 3:
                                    break
                                case _ :
                                    print("Invalid Input")
                        
                        break 


                    elif ch == 4:
                        break 

                    else:
                        print("Invalid Input...")

                break        


            elif ch ==2:
                print("2) Split Array")
                print("----------------------------")
                print(self.splitarr)
                n1 = int(input("Enter Split Size"))
                d = int(input("Enter your Dimension like [0] or [1]"))
                if n1 > 0 and d >=0:
                    try:
                        print(np.split(self.splitarr,n1,axis=d))
                    except ValueError:
                        print("Not Match Diamation and split Size")
                else:
                    print("Invalid Input")

                break    
                        

            elif ch == 3:
                break
            else:
                print("Invalid input")     





    def Search_Sort_And_Filter(self):
        print("Oroginal Array")
        print(self.ser)
        while True:
            print("Choose An Option")
            print("1) Search A Value")
            print("2) Sort The Array")
            print("3) Filter Value")
            print("4) Exit")

            ch  = int(input("Enter Your Choice"))

            match ch :
                case 1:
                    print("1) Search A Value")
                    num = int(input("Enter Your Number"))
                    print(np.where(self.ser[self.ser==num])) 

                    

                case 2:
                    print("2) Sort The Array")
                    print("-------------------------------------")
                    while True:
                        print("1) Ascending")
                        print("2) Descending")
                        print("3) Exit")
                        ch = int(input("Enter Your Choice"))

                        match ch:
                            case 1:
                                
                                print("Sort Ascending Array")
                                print(np.sort(self.ser,))
                            case 2: 
                             print("Sort Descending Array")
                             print(np.sort(self.ser,axis=0)[::-1])
                            case 3:
                                break
                            case _:
                                print("Invalid Input") 

                            

                case 3 :
                    print("3) Filter Value")  
                    print("------------------------------------")
                    while True:
                        print("Select Fliter")
                        print("1) Odd-Even")
                        print("2) Greater Then")
                        print("3) Less Then")
                        print("4) Exit")

                        ch = int(input("Enter  Your Choice"))

                        match ch:
                            case 1:
                                print("Odd-Even")
                                print(np.where(self.ser[self.ser%2==0]))
                            case 2:
                                print("Greater Then")
                                num = int(input("Enter Your Number")) 
                                print(np.where(self.ser>num)) 
                            case 3:
                                print("Greater Then")
                                num = int(input("Enter Your Number")) 
                                print(np.where(self.ser<num))     
                            case 4:
                                break
                            case _:
                                print("Invalid Input")   

                              
                case 4:
                    break
                case _:
                    print("Invalid Choice")   

    @staticmethod
    def Statistical():
        while True:
            print("Select The Type Of Array To Create")
            print("1 . 1D Array")
            print("2 . 2D Array")
            print("3 . 3D Array")
            print("4 . Exit")

            ch = int(input("Enter Your Choice "))

            if ch == 1:
                lenght = int(input("Enter Your Lenght Of Array"))
                arr = np.empty((lenght),dtype=int)
                for i in range(lenght):
                        arr[i] = int(input("Enter Element"))
   
                print("Array Created Successfully....")       
                print(arr)  
                print()
                while True:
                    print("Choose Statistical Operation")
                    print("1) MiniMum And MAximum Value")
                    print("2) Percentiles")
                    print("3) Correlation Cofficients Between Array")
                    print("4) Exit")

                    ch = int(input("Enter Your Choice"))

                    match ch :
                        case 1:
                            print("MiniMum Value",np.min(arr))
                            print()
                            print("Maximum Value",np.max(arr))
                        case 2:
                            p = int(input("Enter Your Percentiles"))
                            d = int(input("Enter your Dimension like [0] or [1]"))
                            print("Orignal Array")
                            print("--------------------------")
                            print(arr) 
                            print()
                            print("Percentiles Value",np.percentile(arr,p,axis=d) ) 
                        case 3: 
                            arr1 = np.empty((lenght),dtype=int)
                            for i in range(lenght):
                                    arr1[i] = int(input("Enter Element"))
            
                            print("Orignal Array")
                            print(arr) 
                            print()
                            print("Second Array")
                            print(arr1)
                            print("------------------------------------")
                            print("Correlation Cofficients Between Array",np.corrcoef(arr,arr1))
                        case 4:
                             break
                        case _ :
                            print("Invalid Input")        
                                        
                      

                

            elif ch ==2:    
                row = int(input("Enter Your Row"))
                col = int(input("Enter Your Cloumn"))
                arr = np.empty((row,col),dtype=int)
                print(f"Total [ {row*col}  ] Element Enter ")
                for i in range(row):
                    for j in range(col):
                        arr[i][j] = int(input(f"Enter element")) 

                print("Array Created Successfully....")
                print(arr)
                while True:
                    print("Choose Statistical Operation")
                    print("1) MiniMum And MAximum Value")
                    print("2) Percentiles")
                    print("3) Correlation Cofficients Between Array")
                    print("4) Exit")

                    ch = int(input("Enter Your Choice"))

                    match ch :
                        case 1:
                            print("MiniMum Value",np.min(arr))
                            print()
                            print("Maximum Value",np.max(arr))
                        case 2:
                            p = int(input("Enter Your Percentiles"))
                            d = int(input("Enter your Dimension like [0]"))
                            print("Orignal Array")
                            print("--------------------------")
                            print(arr) 
                            print()
                            print("Percentiles Value",np.percentile(arr,p,axis=d) ) 
                        case 3: 
                            arr1 = np.empty((row,col),dtype=int)
                            for i in range(row):
                                    for j in range(col):
                                     arr1[i][j] = int(input("Enter Element"))
            
                            print("Orignal Array")
                            print(arr) 
                            print()
                            print("Second Array")
                            print(arr1)
                            print("------------------------------------")
                            print("Correlation Cofficients Between Array",np.corrcoef(arr,arr1))
                        case 4:
                             break
                        case _ :
                            print("Invalid Input")   

            elif ch == 3:
                layer = int(input("Enter Your Layer"))  
                row = int(input("Enter Your Row"))
                col = int(input("Enter Your Cloumn"))
                arr = np.empty((layer,row,col),dtype=int) 
                print(f"Total [ {layer*row*col}  ] Element Enter ") 
                for i in range(layer):
                    for j in range(row):
                        for k in range(col):
                            arr[i][j][k] = int(input("Enter Your Element"))


                print("Array Created Successfully....")
                print(arr)    
                while True:
                    print("Choose Statistical Operation")
                    print("1) MiniMum And MAximum Value")
                    print("2) Percentiles")
                    print("3) Correlation Cofficients Between Array")
                    print("4) Exit")

                    ch = int(input("Enter Your Choice"))

                    match ch :
                        case 1:
                            print("MiniMum Value",np.min(arr))
                            print()
                            print("Maximum Value",np.max(arr))
                        case 2:
                            p = int(input("Enter Your Percentiles"))
                            d = int(input("Enter your Dimension like [0] or [1]"))
                            print("Orignal Array")
                            print("--------------------------")
                            print(arr) 
                            print()
                            print("Percentiles Value",np.percentile(arr,p,axis=d) ) 
                        case 3: 
                          
                            arr1 = np.empty((layer,row,col),dtype=int)
                            for i in range(layer):
                                for j in range(row):
                                    for k in range(col):
                                        arr1[i][j][k] = int(input("Enter Element"))
            
                            print("Orignal Array")
                            print(arr) 
                            print()
                            print("Second Array")
                            print(arr1)
                            print("------------------------------------")
                            print("Correlation Cofficients Between Array",np.corrcoef(arr,arr1))
                        case 4:
                             break
                        case _ :
                            print("Invalid Input")   

            elif ch == 4:
                break 

            else:
                print("Invalid Input...")

    @classmethod
    def __Sum(cls):
        print(cls.__arr)
        print("---------------------------")
        print("Sum Of Array",np.sum(cls.__arr)) 

    @classmethod
    def __mean(cls):
        print(cls.__arr)
        print("---------------------------")
        print("Mean Of Array",np.mean(cls.__arr))    

    @classmethod
    def __Median(cls):
        print(cls.__arr)
        print("---------------------------")
        print("Median Of Array",np.median(cls.__arr))   

    @classmethod
    def __Std(cls):
        print(cls.__arr)
        print("---------------------------")
        print("Standard Deviation Of Array",np.std(cls.__arr)) 

    @classmethod
    def __variance(cls):
        print(cls.__arr)
        print("---------------------------")
        print("Sum Of Array",np.var(cls.__arr))            



    @classmethod
    def Aggregates(cls):  
        while True:
            print("Choose An Aggregate")
            print("1) Sum")
            print("2) Mean")
            print("3) Median")
            print("4) Standard Deviation")
            print("5) Variance")
            print("6) Exit")

            ch = int(input("Enter Your Choice"))

            match ch:

                case 1:
                    print("1) Sum")
                    cls.__Sum()
                case 2:
                    print("2) Mean")
                    cls.__mean()
                case 3:
                    print("3) Median")
                    cls.__Median()
                case 4:
                    print("4) Standard Deviation")
                    cls.__Std()
                case  5:
                    print("5) Variance")
                    cls.__variance()
                case 6:
                    break
                case _:
                    print("Invalid Input ")


d = DataAnalytics()
while True: 
    print("Welcome To Numpy Analyzer!")
    print("------------------------------------")
    print("Choose An Option:")
    print("1) Create A Numpy Array")
    print("2) Perform Mathematical Operations")
    print("3) Combine Or Split Arrays")
    print("4) Search Sort Or Filter Array")
    print("5) Compute Aggregates And Statistics")
    print("6) Exit")

    ch = int(input("Enter Your Choice"))

    match ch :
        case 1:
            print("1) Create A Numpy Array")
            d.Array_Management()
        case 2:
            print("2) Perform Mathematical Operations")
            d.Mathematical_Operations()
        case 3:
            print("3) Combine Or Split Arrays")
            d.Combine_Or_Split_Array()
        case 4:
            print("4) Search Sort Or Filter Array")
            d.Search_Sort_And_Filter()
        case 5:
            print("5) Compute Aggregates And Statistics")
            while True:
                print("Choose Option")
                print("1) Statistics")
                print("2) Aggregates")
                print("3) Exit")

                ch = int(input("Enter Your Choice"))

                match ch:
                    case 1:
                        DataAnalytics.Statistical()
                    case 2:
                        DataAnalytics.Aggregates()
                    case 3:
                        break
                    case _:
                        print("Invalid Input")    


        case 6:
            print("Thank You For Using The Numpy Analyzer ! GoodBye!")
            exit()
        case _:
            print("Invalid Input....")        




