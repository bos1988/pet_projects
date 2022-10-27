import numpy as np
import random as rnd
from itertools import product
from ipywidgets import IntProgress
from dsbudin.formattext import text

# make_deck_str()
# make_deck_tuple()
# get_sample_cards(deck, n=1)
# remove_cards(deck, cards)
# print_deck(deck, sep=2)

def make_deck_str():
    deck = []
    for a, n in product(['A', 'B', 'C', 'D'], range(2, 15)):
        deck.append(a+str(n))
    return deck



def make_deck_tuple():
    deck = []
    for a, n in product(range(1, 5), range(2, 15)):
        deck.append((a, n))
    return deck



def get_sample_cards(deck, n=1):
    return [deck.pop(rnd.randrange(i)) for i in range(len(deck), len(deck)-n, -1)]



def remove_cards(deck, cards):
    for card in cards:
        if deck.count(card) > 0:
            deck.remove(card)
    return deck



def print_deck(deck, sep=2):
    st = deck[0][0]
    l = len(str(deck[-1]))+sep
    for card in deck:
        if not card[0] == st:
            st = card[0]
            print()
        print(str(card).ljust(l), end='')


# cards_to_tuple(func)
# make_res_combination(pos, kickers)
# quick_get_best_combination(cards:list) #передается список кортежей
# get_best_combination(cards:list) #передается список типа 'A13'
# count_combination(cards, *, deck=None, combinations=None, n_cards=1)
# prob_victory_river_1opp(hand, table)
# prob_victory_1opp(hand, table, *, deck=None, n_cards=1)
# prob_victory_n(hand:list, table:list)

# Декоратор для преобразования набора карт в список кортежей
def cards_to_tuple(func):
    suits = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
    def wrapper(*args, **kwargs):
        res = []
        for arg in args:
            res.append([(suits[i[0]], int(i[1:])) for i in arg])
        return func(*res, **kwargs)
    return wrapper



# Формирование результата работы (наименование комбинации и score по кикеру)
def make_res_combination(pos, kickers):
    c = [
        'High_Card',
        'Pair',
        'Two_Pair',
        'Three_of_a_Kind',
        'Straight',
        'Flush',
        'Full_House',
        'Four_of_a_Kind',
        'Straight_Flush',
        'Royal_Straight_Flush'
    ]
    score = pos * 10**11
    for i in range(len(kickers)):
        score += kickers[i] * 100**(4-i)
    
    return (c[pos], score)




# Функция получения лучшей комбинации
def quick_get_best_combination(cards:list): #передается список кортежей
    # Счетчики для стритов:
    delta_ones_indexes = []
    count_ones = 0
    straight_indexes = []
    # Счетчик мастей для флешей
    suits_indexes = [[], [], [], [], []]
    # Счетчики достоинств для парных
    ranks = {}
    
    cards.sort(key=lambda x: (x[1], x[0]), reverse=True)
    # тот же набор карт, но изменяемый в случае если в стит-флеш попадает туз и нужен ранг туза=1
    straight_cards = cards.copy()
    
#     print(cards, '\n')
    
    # Главный цикл по картам:
    for i in range(len(cards) - 1):
        # заполняем счетчики мастей и достоинств:
        rank_i = cards[i][1]    # еще одна после цикла
        suits_indexes[cards[i][0] - 1].append(i)    # еще одна после цикла
        ranks[rank_i] = ranks.get(rank_i, 0) + 1    # еще одна после цикла
        
        # Счетчик для стрита:
        delta = rank_i - cards[i+1][1]
        if delta > 1:
            delta_ones_indexes = []
            count_ones = 0
            continue #                !!!
        elif delta == 1:
            delta_ones_indexes.append(i)
            count_ones += 1
            if count_ones >= 4:
                straight_indexes = delta_ones_indexes + [i+1]
        elif delta == 0:
            delta_ones_indexes.append(i)
        else:
            print('Ошибка: Карты не отсортированы по убыванию!')
            return None
    # Завершение цикла !!!:
    rank_i = cards[i+1][1]
    suits_indexes[cards[i+1][0] - 1].append(i+1)
    ranks[rank_i] = ranks.get(rank_i, 0) + 1
    
    # Если до стрита не хватило одной карты и есть 2 с конца и Туз в начале, то формируем мылый стрит
    if count_ones >= 3 and cards[delta_ones_indexes[0]][1] < 14 and ranks.get(14, 0) * ranks.get(2, 0) > 0:
        straight_indexes = delta_ones_indexes + [i+1]
        for i in range(ranks[14]):
            # заменям достоинство туза на 1 для кикеров малого стрита (большого стрита нет, мы это проверили)
            straight_cards[i] = (straight_cards[i][0], 1)
            straight_indexes.append(i)
    
#     print()
#     print('straight_cards', straight_cards, '\n')
#     print('delta_ones_indexes =', delta_ones_indexes, ', count_ones =', count_ones, 'straight_indexes =', straight_indexes)
#     print('suits_indexes =', suits_indexes, ', ranks =', ranks)
    
# Straight_Flush
    flush = max(suits_indexes, key=len)
    diff = set(flush) & set(straight_indexes)
#     print()
#     print('Straight_Flush')
#     print('flush =', flush)
#     print('straight_indexes =', straight_indexes)
#     print('diff =', diff)
#     print()
    if len(diff) > 4:
        return make_res_combination(8, sorted([straight_cards[j][1] for j in diff], reverse=True)[:5])
    
    ranks_sorted = np.array(sorted(ranks.items(), key=lambda x: (x[1], x[0]), reverse=True))
    
# Four_of_a_Kind, Full_House
    first_ranks = ranks_sorted[0, 1] + ranks_sorted[1, 1]
    if first_ranks > 4:
        score = ranks_sorted[0, 1] + 3
        if score == 7:
            # Four_of_a_Kind
            return make_res_combination(score, ([ranks_sorted[0,0]] + sorted(ranks_sorted[1:,0], reverse=True))[:2])
        else:
            # Full_House
            return make_res_combination(score, ranks_sorted[:2,0])
# Flush
    if len(flush) > 4:
        return make_res_combination(5, [cards[j][1] for j in flush[:5]])
    
# Straight
    if straight_indexes:
        max_straight_value = cards[straight_indexes[0]][1]
        return make_res_combination(4, list(range(max_straight_value, max_straight_value-5, -1)))
    
# Three_of_a_Kind, Two_Pair, Pair
    if first_ranks > 2:
        score = ranks_sorted[0, 1] * 2 + ranks_sorted[1, 1] - 4
        return make_res_combination(score, (list(ranks_sorted[:2,0]) + sorted(ranks_sorted[2:,0], reverse=True))[:7-first_ranks])
    
# High_Card
    return make_res_combination(0, list(ranks)[:5])




@cards_to_tuple
def get_best_combination(cards:list):
    return quick_get_best_combination(cards)
    
    


# Функция вероятности получения коминации для разного количества дополнительно вынутых карт
# рекурсивная функция подсчета событий
def count_combination(cards, *, deck=None, combinations=None, n_cards=1):
#     print('START_COUNT')
    if deck==None:
        deck = remove_cards(make_deck_tuple(), cards)
    if n_cards < 1:
        return 1, int(quick_get_best_combination(cards)[0] in combinations)
    
    count = 0
    target_count = 0
    deck_in = deck.copy()
    for _ in range(len(deck)):
#         card = deck_in.pop(0) # ВСЕ КОМБИНАЦИИ с повторами и перестановками
        card = deck_in.pop() # только уникальные сочетания
        comb = cards + [card]
        if n_cards < 2:
            count += 1
            if quick_get_best_combination(comb)[0] in combinations:
                target_count += 1
        else:
            res = count_combination(comb, deck=deck_in, combinations=combinations, n_cards=n_cards-1)
            count += res[0]
            target_count += res[1]
#         deck_in.append(card) # ВСЕ КОМБИНАЦИИ с повторами и перестановками

#     print('END_COUNT')
    return count, target_count





@cards_to_tuple
def probability_combination(cards:list, combinations, n_cards = 1):
    deck_test = remove_cards(make_deck_tuple(), cards)
    res = count_combination(cards, deck=deck_test, combinations=combinations, n_cards=n_cards)
    return res





def prob_victory_river_1opp(hand, table):
    # примем, что стол из 5 карт, значит мой полный набор известен
    if not len(table) == 5:
        print('Неподходящий стол')
        return 1, 0
    
    my_comb = table + hand
    my_best_comb = quick_get_best_combination(my_comb)
    
    deck_test = remove_cards(make_deck_tuple(), my_comb)
    
    count = 0
    target_count = 0
    n_cards = len(deck_test)
    for i in range(n_cards):
        for j in range(i+1, n_cards):
            count += 1
            opp_best_comb = quick_get_best_combination(table + [deck_test[i]] + [deck_test[j]])
            if my_best_comb[1] > opp_best_comb[1]: # В случае ничьей - считаем как поражение
                target_count += 1

    return count, target_count




def prob_victory_1opp(hand, table, *, deck=None, n_cards=1):
    my_comb = table + hand
    my_best_comb = quick_get_best_combination(my_comb)
    
    count = 0
    target_count = 0
    deck_in = deck.copy()
    for _ in range(len(deck)):
        card = deck_in.pop()
        comb = table + [card]
        if n_cards < 2:
            res = prob_victory_river_1opp(hand, comb)    
        else:
            res = prob_victory_1opp(hand, comb, deck=deck_in, n_cards=n_cards-1)
        
        count += res[0]
        target_count += res[1]

    return count, target_count




@cards_to_tuple
def prob_victory_n(hand:list, table:list):
    count_table = len(table)
    if count_table > 5:
        print('Неподходящий стол')
        return 1, 0
    n_cards = 5 - count_table
    if n_cards < 1:
        return prob_victory_river_1opp(hand, table)
    deck_test = remove_cards(make_deck_tuple(), hand+table)
    return prob_victory_1opp(hand, table, deck=deck_test , n_cards=n_cards)




def show_prob_victory(hand:list, table:list):
    print('Комбинация на руках:\n', get_best_combination(hand + table), sep='', end='\n\n')
    res = prob_victory_n(hand, table)
    print('Общее кол-во итераций:', res[0])
    print('Кол-во целевых событий:', res[1])
    print(f'Вероятность выигрыша: {text.BOLD}{text.BG_SILVER} {(res[1] / res[0]):.3%} {text.END}', end='\n\n')
