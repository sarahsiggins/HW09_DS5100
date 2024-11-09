import unittest
from booklover import BookLover
import pandas as pd
import numpy as np

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        my_book_list = pd.DataFrame({'book_name':['Jane Eyre','Fight Club','The Divine Comedy','The Popol Vuh'],'book_rating':[4,3,5,5]})
        book_test = BookLover('Sarah','sc8rg@virginia.edu','fiction',4,my_book_list)
        book_test.add_book('Hunger Games',2)
        
        expected = 'Hunger Games'
        self.assertIn(expected, str(book_test.book_list.book_name))
        
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        my_book_list = pd.DataFrame({'book_name':['Jane Eyre','Fight Club','The Divine Comedy','The Popol Vuh'],'book_rating':[4,3,5,5]})
        book_test = BookLover('Sarah','sc8rg@virginia.edu','fiction',4,my_book_list)
        
        
        self.assertRaises(ValueError, book_test.add_book,'Jane Eyre',3)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        my_book_list = pd.DataFrame({'book_name':['Jane Eyre','Fight Club','The Divine Comedy','The Popol Vuh'],'book_rating':[4,3,5,5]})
        book_test = BookLover('Sarah','sc8rg@virginia.edu','fiction',4,my_book_list)
        has_read = book_test.has_read('Jane Eyre')
        self.assertTrue(has_read)
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        my_book_list = pd.DataFrame({'book_name':['Jane Eyre','Fight Club','The Divine Comedy','The Popol Vuh'],'book_rating':[4,3,5,5]})
        book_test = BookLover('Sarah','sc8rg@virginia.edu','fiction',4,my_book_list)
        has_read = book_test.has_read('Harry Potter')
        self.assertFalse(has_read)
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        my_book_list = pd.DataFrame({'book_name':['Jane Eyre','Fight Club','The Divine Comedy','The Popol Vuh'],'book_rating':[4,3,5,5]})
        book_test = BookLover('Sarah','sc8rg@virginia.edu','fiction',4,my_book_list)
        book_test.add_book('Hunger Games',2)
        
        expected = 5
        num_books_test = book_test.num_books_read()
        self.assertEqual(num_books_test, expected)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        my_book_list = pd.DataFrame({'book_name':['Jane Eyre','Fight Club','The Divine Comedy','The Popol Vuh'],'book_rating':[4,3,5,5]})
        book_test = BookLover('Sarah','sc8rg@virginia.edu','fiction',4,my_book_list)
        
        fav_test = (book_test.fav_books().book_rating > 3).all()
        self.assertTrue(fav_test)
        
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)