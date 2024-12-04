from json import load
f1=open("C:\\Users\\HP\\OneDrive\\Desktop\\pythonworks\\file data sets\\book.json","r")
data1=load(f1)
for book in data1:
    print(book)

all_titles=[book.get("title")for book in data1]
# print(all_titles)

page_filters=[book.get("title")for book in data1 if book.get("pages")<250]
# print(page_filters)

all_genres=[book.get("genre")for book in data1]
# print(set(all_genres)) #set for no repeatatiin

genre_count={genre:all_genres.count(genre)for genre in all_genres}
# print(genre_count)

costly_book=max(data1,key=lambda d:d.get("price"))
# print(costly_book)

all_author=[book.get("author")for book in data1]
# print(all_author)
author_count={auth:all_author.count(auth) for auth in all_author}
# print([k for k,v in author_count.items() if v>1])
