# 베스트앨범 (Level3)
# https://programmers.co.kr/learn/courses/30/lessons/42579

import unittest


class Album:
    def __init__(self, id, genre, plays):
        self.id = id
        self.genre = genre
        self.plays = plays

    def __lt__(self, other):
        return self.plays < other.plays

    def __le__(self, other):
        return self.plays <= other.plays

    def __gt__(self, other):
        return self.plays > other.plays

    def __ge__(self, other):
        return self.plays >= other.plays

    def __eq__(self, other):
        return self.plays == other.plays

    def __ne__(self, other):
        return self.plays != other.plays


def solution(genres, plays):
    answer = []
    album_list, total = __store_in_db(genres, plays)

    return __calculate(total, album_list)


def __store_in_db(genres, plays):
    album_list = []
    total = {}
    for i in range(len(genres)):
        album_list.append(Album(i, genres[i], plays[i]))
        total[genres[i]] = total.get(genres[i], 0) + plays[i]
    return __sort(album_list, total)


def __sort(album_list, total):
    album_list = sorted(album_list, reverse=True)
    total = sorted(total.items(), key=lambda total: total[1], reverse=True)
    return album_list, total


def __calculate(total, album_list):
    answer = []
    while len(total) > 0:
        play_genre = total.pop(0)
        cnt = 0
        for ab in album_list:
            if play_genre[0] == ab.genre:
                answer.append(ab.id)
                cnt += 1
            if cnt == 2:
                break
    return answer


class TestFirstSolution(unittest.TestCase):
    def test_case1(self):
        # given
        genres = ["classic", "pop", "classic", "classic", "pop"]
        plays = [500, 600, 150, 800, 2500]
        # when
        result = solution(genres, plays)
        # then
        self.assertEqual(result, [4, 1, 3, 0])


if __name__ == '__main__':
    unittest.main()
