from operator import itemgetter
from pprint import pprint
from music import Music
from orchestra import Orchestra
from relationship import Relationship
from relationship import Link


musics = [
    imagine := Music('Imagine'),
    stone := Music('Like a Rolling Stone'),
    respect := Music('Respect'),
    vibrations := Music('Good Vibrations'),
    jude := Music('Hey Jude'),
    generation := Music('My Generation'),
]

orcs = [
    miller := Orchestra('Оркестр Гленна Миллера', 2),
    moria := Orchestra('Оркестр под управлением Поля Мориа', 3),
    czech := Orchestra('Чешский филармонический оркестр', 10),
    cleveland := Orchestra('Кливлендский оркестр', 15),
    philadelphia := Orchestra('Филадельфийский оркестр', 10),
]

rel_otm = Relationship(Music, Orchestra, Link.ONE_TO_MANY, fk=Orchestra.fk_music)
rel_otm.link(imagine, miller)
rel_otm.link(stone, moria)
rel_otm.link(respect, czech)
rel_otm.link(imagine, cleveland)
rel_otm.link(imagine, philadelphia)
 
rel_mtm = Relationship(Music, Orchestra, Link.MANY_TO_MANY)
rel_mtm.link(imagine, miller)
rel_mtm.link(stone, moria)
rel_mtm.link(respect, czech)
rel_mtm.link(imagine, cleveland)
rel_mtm.link(imagine, philadelphia)
rel_mtm.link(stone, philadelphia)
rel_mtm.link(jude, cleveland)
 
def main():
    """Основная функция"""
 
    print('Задание А1')

    arr = [(o_name, m_name) for (m_name,), (o_name, _) in rel_otm.iter(musics, orcs)]
    sorted_arr = sorted(arr, key=itemgetter(0))

    pprint(sorted_arr)
    

    print('\nЗадание А2')

    m_names = [m_name for (m_name,), (o_name, _) in rel_otm.iter(musics, orcs)]
    count = {}

    for m_name in m_names:
        count[m_name] = count[m_name] + 1 if count.get(m_name) else 1

    sorted_count = sorted(count.items(), key=itemgetter(1))
    [print(m_name, o_count) for m_name, o_count in sorted_count]

        
    print('\nЗадание А3')
    arr = [(m_name, o_name, o_amount) for (m_name,), (o_name, o_amount) in rel_mtm.iter(musics, orcs)]

    for (m_name, o_name, o_amount) in arr:
        if o_amount == 10:
            print(m_name, o_name)

 
if __name__ == '__main__':
    main()
