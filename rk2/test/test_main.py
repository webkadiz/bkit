import pytest
from music import Music
from orchestra import Orchestra
from relationship import Relationship, Link
from table import Table


def test_autoincrement_id():
    Music.id = 0
    music1 = Music('first')
    music2 = Music('second')

    assert music2.id == 2


def test_one_to_many_link():
    Music.id = 0
    Orchestra.id = 0
    music = Music('music')
    orc = Orchestra('orc', 100)

    rel = Relationship(Music, Orchestra, Link.ONE_TO_MANY, fk=Orchestra.fk_music)
    rel.link(music, orc)

    assert music.id == 1
    assert orc.music_id == 1


def test_many_to_many_link():
    Music.id = 0
    Orchestra.id = 0
    music = Music('music')
    orc = Orchestra('orc', 200)

    rel = Relationship(Music, Orchestra, Link.MANY_TO_MANY)
    rel.link(music, orc)

    assert rel.many_to_many == [[1,1]]
