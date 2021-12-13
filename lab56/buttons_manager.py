from telebot import types
import constants

class ButtonsManager():
    def __init__(self, news_stack):
        self.news_stack = news_stack

    def getSeeNewsButton(self):
        if self.news_stack.pt >= len(self.news_stack.news): return None

        return types.InlineKeyboardButton(
            self.news_stack.see_text(),
            callback_data=constants.SEE_CMD
        )

    def getEjectNewsButton(self):
        if self.news_stack.pt >= len(self.news_stack.news): return None

        return types.InlineKeyboardButton(
            self.news_stack.eject_text(),
            callback_data=constants.EJECT_CMD
        )

    def getAddNewsButton(self):
        return types.InlineKeyboardButton(
            self.news_stack.add_text(),
            callback_data=constants.ADD_CMD
        )

    def getToBeginButton(self):
        if self.news_stack.pt == 0: return None

        return types.InlineKeyboardButton(
            self.news_stack.to_begin_text(),
            callback_data=constants.TO_BEGIN_CMD
        )
