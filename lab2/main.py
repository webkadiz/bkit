from lab_python_oop import Rect, Square, Cicle
import emoji

if __name__ == '__main__':
    n = 5
    rect = Rect(n, n, 'blue')
    cicle = Cicle(n, 'green')
    square = Square(n, 'red')

    print(rect)
    print(cicle)
    print(square)
    print(emoji.emojize('Python is :thumbs_up:'))

