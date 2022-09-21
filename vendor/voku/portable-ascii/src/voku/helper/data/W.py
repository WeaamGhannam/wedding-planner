class publication:


    def _initialize_instance_fields(self):
        #instance fields found by C++ to Python Converter:
        self.title = ""
        self.price = 0


#ORIGINAL LINE: publication()
    def __init__(self):

        self._initialize_instance_fields()


        self.title = " "

        self.price = 0.0

#ORIGINAL LINE: publication(str t,float p)
    def __init__(self, t, p):

        self._initialize_instance_fields()


        self.title = t

        self.price = p









    def getdata(self):


        print("Enter title of publication: ", end = '')

        cin>> self.title

        print("Enter price of publication: ", end = '')

        cin>> self.price




    def putdata(self):


        print("Publication titles :", end = '')
        print(self.title, end = '')
        print("\n", end = '')

        print("Publication price :", end = '')
        print(self.price, end = '')
        print("\n", end = '')





class book(publication):


    def _initialize_instance_fields(self):
        #instance fields found by C++ to Python Converter:
        self._pagecount = 0


#ORIGINAL LINE: book()
    def __init__(self):

        self._initialize_instance_fields()


        self._pagecount = 0


    #After : base class constructor is called 

#ORIGINAL LINE: book(str t,float p,int pc):publication(t,p)
    def __init__(self, t, p, pc):

        self._initialize_instance_fields()

        super().__init__(t, p)

        self._pagecount = pc




    def getdata(self):


        super().getdata() #call publication class function to get getdata

        print("Enter Book Page Count :", end = '')

        cin>> self._pagecount




    def putdata(self):


        super().putdata() #Show Publication data

        print("Book page count:", end = '')
        print(self._pagecount, end = '')
        print("\n", end = '')





class CD(publication):


    def _initialize_instance_fields(self):
        #instance fields found by C++ to Python Converter:
        self._time1 = 0




#ORIGINAL LINE: CD()
    def __init__(self):

        self._initialize_instance_fields()


        self._time1 = 0.0


    #After : base class constructor is called

#ORIGINAL LINE: CD(str t, float p, float tim):publication(t,p)
    def __init__(self, t, p, tim):

        self._initialize_instance_fields()

        super().__init__(t, p)

        self._time1 = tim




    def getdata(self):


        super().getdata()

        print("Enter tape's playing time:", end = '')

        cin>> self._time1




    def putdata(self):


        super().putdata()

        print(" Tape's playing time :", end = '')
        print(self._time1, end = '')
        print("\n", end = '')



def main():


    print("\n", end = '')
    print("Book data", end = '')
    print("\n", end = '')

    b = book("C++", 230, 300)

    b.putdata()

    print("\n", end = '')
    print("CD Data", end = '')
    print("\n", end = '')

    c = CD("C++", 100, 120.5)

    c.putdata()



    print("\n Enter New Details Of Book :\n", end = '')

    b.getdata()

    c.getdata()

    print("\n\n Book data entered by user:\n", end = '')

    b.putdata()

    c.putdata()

if __name__ == "__main__":
    main()