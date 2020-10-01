from app import app
import urllib.request,json
from models import book

Book= book.Book
# Getting api key
api_key = app.config['BOOK_API_KEY']

# Getting the movie base url
base_url = app.config["BOOK_API_BASE_URL"]


def get_book():
    '''
    Function that gets the json response to our url request
    '''
    get_book_url = base_url.format(api_key)

    with urllib.request.urlopen(get_book_url) as url:
        get_books_data = url.read()
        get_books_response = json.loads(get_books_data)

        book_results = None

        if get_books_response['items']:
            book_results_list = get_books_response['items']
            book_results = process_results(book_results_list)


    return book_results

# def process_results(book_list):
    
#     book_results = []
#     for book_item in book_list:
#         id = book_item.get('id')
#         title = book_item['volumeInfo' ]['title'] 
#         # import pdb; pdb.set_trace()       
#         poster = book_item.get('volumeInfo',{}).get('imageLinks',{}).get('thumbnails',{})
#         print(poster)
        # poster=book_item['volumeInfo']['imageLinks']['smallThumbnail']
        
        # volumeInfo = book_item.get('volumeInfo')
        # try:
        #     imageLinks = volumeInfo.get('ImageLinks')
        #     poster = imageLinks
        #     print(poster)
        # except Exception:
        #     pass

    #     author=book_item['volumeInfo']['authors']        
    #     publisher=book_item.get('publisher')
    #     publishedDate=book_item.get('publishedDate')

    #     if id:
    #         book_object = Book(id,title,author,poster,publisher,publishedDate)
    #         book_results.append(book_object)
   
    # print(poster) 
    # return book_results
def process_results(book_list):
    book_results = []
    for book_item in book_list:
        id = book_item.get('id')
        title = book_item['volumeInfo' ]['title']
        author=book_item['volumeInfo']['authors']
        poster=book_item['volumeInfo']['imageLinks']['smallThumbnail']
        publisher=book_item.get('publisher')
        publishedDate=book_item.get('publishedDate')
        if id:
            book_object = Book(id,title,author,poster,publisher,publishedDate)
            book_results.append(book_object)
    print(poster)
    return book_results
