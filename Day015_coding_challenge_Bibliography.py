#Day015 OOP code challenge: Book biblio
class Book:
    def __init__(self,authorfirstname, authorlastname, booktitle, publish_place, publisher, publish_year):
        self.first = authorfirstname
        self.last = authorlastname
        self.title = booktitle
        self.place = publish_place
        self.publisher = publisher
        self.year = publish_year
        
    def bib_entry(self):
        print(self.first \
               + ', ' + self.last \
               + ', ' + self.title + ', ' + self.place \
               + ':  ' + self.publisher + ', ' \
               + str(self.year) ,end='.')

beauty = Book('Thomas','Dubay','The Evidential Power of Beauty','San Francisco','Ignatius press',1999)
pynut = Book('Alex','Martelli','python in a nutshell','Sebastopol, CA',"O'Reilly Media, Inc.",2003)

pynut.bib_entry()

beauty.bib_entry()

beauty.year = 2021

beauty.bib_entry()

"""
'\' with print or return can be used to print the desired output 
if our content inside print or return is very long.
"""


