import booklover
import pandas as pd

my_book_list = pd.DataFrame({'book_name':['Jane Eyre','Fight Club','The Divine Comedy','The Popol Vuh']
                          ,'book_rating':[4,3,5,5]})
book_test = BookLover('Sarah','sc8rg@vt.edu','fiction',4,my_book_list)