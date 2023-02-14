from abc import ABC, abstractmethod
from datetime import datetime

class Post(ABC):
    def __init__(self, author, date):
        self.__author = author
        self.__date = date

    def get_author(self):
        return self.__author

    def get_date(self, time_format="%Y-%m-%d"):
        return self.__date.strftime(time_format)

    @abstractmethod
    def display_content(self):
        pass

    def display(self):
        print(f"Autor des Posts: {self.get_author()}\n\n{self.display_content()}\n\ngepostet am {self.get_date()}")

class PhotoPost(Post):
    def __init__(self, author, photo, caption, date=datetime.now()):
        super().__init__(author, date)
        self.__photo = photo
        self.__caption = caption

    def display_content(self):
        return f"Dateiname: {self.__photo}\nBeschreibung: {self.__caption}"

class MessagePost(Post):
    def __init__(self, author, message, date=datetime.now()):
        super().__init__(author, date)
        self.__message = message

    def display_content(self):
        return f"Message: {self.__message}"

class NewsFeed:
    def __init__(self):
        self.__posts = []

    def add_post(self, post):
        self.__posts.append(post)

    def print_feed(self):
        for p in self.__posts:
            p.display()

feed = NewsFeed()
feed.add_post(PhotoPost("Ursula Urlauberin", "photo.jpg", "Foto aus meinem Urlaub"))
feed.add_post(MessagePost("Ulf Urlaub", "Ist das Uphuser Meer nicht toll?"))

feed.print_feed()