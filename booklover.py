import pandas as pd
class BookLover:
    
    def __init__(self,name,email,fav_genre,num_books=0, book_list=pd.DataFrame({'book_name':[],'book_rating':[]})):
        self.name = str(name)
        self.email = str(email)
        self.fav_genre = str(fav_genre)
        self.num_books = num_books
        self.book_list = book_list
        #self.book_list = pd.DataFrame({'book_name':[],'book_rating':[]})
                
                 
    def add_book(self,book_name,book_rating):
        new_book = pd.DataFrame({
            'book_name': [book_name], 
            'book_rating': [book_rating]})
        if str(book_name) in str(self.book_list.book_name):
            raise ValueError("Book already in List")
        else:
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
                 
    
    def has_read(self,book_name):
        if str(book_name) in str(self.book_list.book_name):
            return True
        else:
            return False
        
                 
    def num_books_read(self):
        num_read = self.book_list.book_name.count()
        return num_read
        #print(self.num_books)
                 #or sum the data frame?
        
    def fav_books(self):
        favBook = self.book_list[self.book_list.book_rating > 3]
        return favBook
        #x for x in range(1, 101) if IsHappy((GetX(x)))
        #favBooks = self.book_list.book_rating > 3.0
        #print(favBooks)