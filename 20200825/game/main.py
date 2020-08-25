# 게임 개발

from .GameMap import GameMap
from .Character import Character


def solution(size, start, location):
    start_character_x, start_character_y, start_character_direction = start

    game_map = GameMap(size, location)
    character = Character(start_character_x, start_character_x, start_character_direction, game_map)

    cnt = 1
    turn_time = 0
    character.check_in(start_character_x, start_character_y)

    while True:
        character.turn_left()
        if character.can_move_forward():
            character.move_forward()
            cnt += 1
            turn_time = 0
        else:
            turn_time += 1

        if turn_time == 4:
            if character.can_move_back():
                character.move_back()
            else:
                break
    return cnt
