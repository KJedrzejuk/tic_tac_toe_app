# -*- coding: utf-8 -*-
from random import randint
from typing import List


class Management:

    def __init__(self):
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]

        self.match_end = False
        self.gameplay_choice = ['1', '2', 'END']
        self.players_symbol = {"player1": ['X', 'O'], "player2": ['X', 'O']}

    def menu(self) -> None:
        print("Witaj w grze kółko i krzyżyk \n Wybierz co chcesz zrobić: ")
        self.gameplay = input("Wprowadź wartość z nawiasów kwadratowych \n "
                              "Jeden gracz [1], dwóch graczy [2], koniec gry [END]: ").upper()
        while self.gameplay not in self.gameplay_choice:
            self.gameplay = input("Wprowadź poprawną wartość: jeden gracz [1], "
                                  "dwóch graczy [2], koniec gry [END]: ").upper()

    def menu_after_match(self) -> None:
        print("Co chcesz zrobić teraz? ")
        self.gameplay_after_match = input("Wprowadź wartość znajdującą się w nawiasie kwadratowym. [1] aby zagrać z"
                                          "komputerem, [2] aby zagrać z graczem, [END] aby zakończyć grę. ").upper()
        while self.gameplay_after_match not in self.gameplay_choice:
            self.gameplay_after_match = input("Wprowadź wartość znajdującą się w nawiasie kwadratowym. [1] aby zagrać z"
                                              "komputerem, [2] aby zagrać z graczem, [END] aby zakończyć grę. ").upper()

    def choice_after_match(self, choice: str) -> None:
        global game_end
        if choice == "END":
            game_end = True
        else:
            self.gameplay = choice
            game_end = False
            self.match_end = False

    def symbol_selection(self) -> None:
        player1_symbol = input("Podaj swój symbol którym chcesz grać (X/O): ").upper()
        while player1_symbol not in (self.players_symbol['player1']):
            player1_symbol = input("Podaj swój symbol którym chcesz grać (X/O): ").upper()
        if player1_symbol == 'X':
            self.players_symbol["player1"].remove('O')
            self.players_symbol["player2"].remove('X')
        else:
            self.players_symbol["player1"].remove('X')
            self.players_symbol["player2"].remove('O')

    def board_print(self) -> None:
        print(f'{self.board[0][0]}|{self.board[0][1]}|{self.board[0][2]}')
        print("-+-+-")
        print(f'{self.board[1][0]}|{self.board[1][1]}|{self.board[1][2]}')
        print("-+-+-")
        print(f'{self.board[2][0]}|{self.board[2][1]}|{self.board[2][2]}')

    def clear_board(self) -> None:
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]

    def retutrn_dictionary(self) -> None:
        self.players_symbol = {"player1": ['X', 'O'], "player2": ['X', 'O']}

class Logic(Management):

    def win_check(self, player1: list, player2: list) -> None:
        cell_counter = 0
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            if self.board[0][0] in player1:
                print(self.get_winner_label(player1))
                self.match_end = True
                return
            if self.board[0][0] in player2:
                print(self.get_winner_label(player2))
                self.match_end = True
                return

        if self.board[2][0] == self.board[1][1] == self.board[0][2] and self.board[1][1] != ' ':
            if self.board[1][1] in player1:
                print(self.get_winner_label(player1))
                self.match_end = True
                return
            if self.board[1][1] in player2:
                print(self.get_winner_label(player2))
                self.match_end = True
                return

        while cell_counter < len(self.board):
            if self.board[0][cell_counter] == self.board[1][cell_counter] \
                    == self.board[2][cell_counter] and self.board[0][cell_counter] != ' ':
                if self.board[0][cell_counter] in player1:
                    print(self.get_winner_label(player1))
                    self.match_end = True
                    return
                if self.board[0][cell_counter] in player2:
                    print(self.get_winner_label(player2))
                    self.match_end = True
                    return

            if self.board[cell_counter][0] == self.board[cell_counter][1] \
                    == self.board[cell_counter][2] and self.board[cell_counter][0] != ' ':
                if self.board[cell_counter][0] in player1:
                    print(self.get_winner_label(player1))
                    self.match_end = True
                    return
                if self.board[cell_counter][0] in player2:
                    print(self.get_winner_label(player2))
                    self.match_end = True
                    return
            cell_counter += 1

            if ' ' not in self.board[0] and ' ' not in self.board[1] and ' ' not in self.board[2]:
                print("Nastąpił remis ")
                self.match_end = True
                return

    def ai_player(self, symbol: str) -> None:
        print("Komputer wykonał następujący ruch: ")
        row_random = randint(0, 2)
        column_random = randint(0, 2)
        while self.board[row_random][column_random] != ' ':
            row_random = randint(0, 2)
            column_random = randint(0, 2)
        self.board[row_random][column_random] = symbol

    def player(self, symbol: str) -> None:
        print(f'Ruch gracza {symbol}')
        chose_row = int(input("Podaj wiersz w której chcesz postawić znak: "))
        chose_column = int(input("Podaj kolumnę w której chcesz postawić znak: "))
        while self.board[chose_row - 1][chose_column - 1] in ("X", "O"):
            print("To miejsce jest już zajęte, proszę wybrać kolejne")
            chose_row = int(input("podaj wiersz: "))
            chose_column = int(input("podaj kolumnę: "))
        self.board[chose_row - 1][chose_column - 1] = symbol

    def get_winner_label(self, player: List[str]) -> str:
        return f'Gracz {"".join(player)} wygrał!'


logic = Logic()

game_end = False
logic.menu()

if logic.gameplay != "END":
    while not game_end:
        if logic.gameplay == "1":
            logic.symbol_selection()
            logic.board_print()
            while not logic.match_end:
                logic.player(logic.players_symbol["player1"][0])
                logic.board_print()
                logic.win_check(logic.players_symbol["player1"], logic.players_symbol["player2"])

                if not logic.match_end:
                    logic.ai_player(logic.players_symbol["player2"][0])
                    logic.board_print()
                    logic.win_check(logic.players_symbol["player1"], logic.players_symbol["player2"])
                else:
                    break

        if logic.gameplay == "2":
            logic.symbol_selection()
            logic.board_print()
            while not logic.match_end:

                logic.player(logic.players_symbol["player1"][0])
                logic.board_print()
                logic.win_check(logic.players_symbol["player1"], logic.players_symbol["player2"])

                if not logic.match_end:
                    logic.player(logic.players_symbol["player2"][0])
                    logic.board_print()
                    logic.win_check(logic.players_symbol["player1"], logic.players_symbol["player2"])
                else:
                    break

        logic.clear_board()
        logic.retutrn_dictionary()
        logic.menu_after_match()
        logic.choice_after_match(logic.gameplay_after_match)

print("Program zakończył działanie. Miłego dnia!")
