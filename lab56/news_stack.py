import constants

class NewsStack():
    def __init__(self):
        self.news = []
        self.pt = 0
        self.last_message = ''

    def see(self):
        news = self.news[self.pt]
        self.pt += 1
        return news
    
    def see_text(self):
        return constants.SEE_CMD_TEXT.format(len(self.news) - self.pt)
    
    def eject(self):
        news = self.news[self.pt]
        del self.news[self.pt]
        return news

    def eject_text(self):
        return constants.EJECT_CMD_TEXT.format(len(self.news) - self.pt)
    
    def add_text(self):
        return constants.ADD_CMD_TEXT.format()

    def add_last_message(self):
        self.news.append(self.last_message)
    
    def to_begin_text(self):
        return constants.TO_BEGIN_CMD_TEXT.format()
