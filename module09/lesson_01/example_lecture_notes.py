import requests
from bs4 import BeautifulSoup
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

from model import Book, Base


def parse_data():
    rate_to_number = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    url = 'http://books.toscrape.com/'
    store_ = []
    html_doc = requests.get(url)

    if html_doc.status_code == 200:
        soup = BeautifulSoup(html_doc.content, 'html.parser')
        books = soup.select('section')[0].find_all('article', attrs={'class': 'product_pod'})
        for book in books:
            img_url = f"{url}{book.find('img')['src']}"
            rating = rate_to_number.get(book.find('p', attrs={'class': 'star-rating'})['class'][1])
            title = book.find('h3').find('a')['title']
            price = float(book.find('p', attrs={'class': 'price_color'}).text[1:])
            store_.append({
                'img_url': img_url,
                'rating': rating,
                'title': title,
                'price': price
            })

    return store_


if __name__ == '__main__':
    store = parse_data()
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()
    for el in store:
        book = Book(img_url=el.get('img_url'), rating=el.get('rating'), title=el.get('title'), price=el.get('price'))
        session.add(book)
    session.commit()
    books = session.query(Book).all()
    for b in books:
        print(vars(b))
    session.close()
