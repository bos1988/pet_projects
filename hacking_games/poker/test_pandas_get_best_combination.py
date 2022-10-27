import pandas as pd
import numpy as np

# Работает Через DataFrame:
#     - карты хранит в DF
#     - поиск нужной комбинайии присходит через DF
# Возвращает наименование комбинации и SCORE с учетом кикеров: чем выше SCORE, тем лучше комбинация
def get_best_combination(cards, show_info=False):
    # High Card (Старшая карта)
    # Pair (Пара)
    # Two Pair (Две пары)
    # Three of a Kind (Сет или Тройка)
    # Straight (Стрит)
    # Flush (Флеш)
    # Full House (Фул Хауз)
    # Four of a Kind (Каре)
    # Straight Flush (Стрит Флеш)
    # Royal Straight Flush (Стрит Флеш Роял)
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

    cards = pd.DataFrame({
        'suit': np.array(cards)[:, 0],
        'rank': np.array(cards)[:, 1]
    })
    kickers = [0] * 3

    if show_info:
        display(cards)

    def n_duplicates(check_cards):
        return check_cards['rank'].value_counts().max()

    def is_twopair(check_cards):
        value_counts = check_cards['rank'].value_counts().values
        return value_counts[0] > 1 and value_counts[1] > 1

    def flush_set(check_cards):
        most_frequent = check_cards['suit'].value_counts().idxmax()
        return check_cards[check_cards['suit'] == most_frequent]['rank']

    def straight_set(ranks):
        if 14 in ranks.values:
            ranks = pd.concat([ranks, pd.Series([1]*sum(ranks == 14))])
        ranks_list = sorted(ranks.unique())
        seq = [{ranks_list[0]}]
        i = 0
        for j in range(len(ranks_list)-1):
            if ranks_list[j+1] - ranks_list[j] == 1:
                seq[i].add(ranks_list[j])
                seq[i].add(ranks_list[j+1])
            else:
                i += 1
                seq.append({ranks_list[j+1]})
        max_seq = max(seq, key=lambda x: (len(x), max(x)))
        return pd.Series(sorted(max_seq), name='rank')

    def get_simple_kickers(ranks, twin_comb=1):
        super_set = ranks.value_counts().reset_index().sort_values(['rank', 'index'], ascending=False).reset_index(drop=True)
        if show_info:
            print('Super_set:')
            display(super_set)
        if twin_comb > 1:
            return super_set['index'][:twin_comb-1].to_list() + [super_set['index'][twin_comb-1]]
        else:
            return super_set['index'][:5].to_list()

    straight_flush = straight_set(flush_set(cards))
    if len(straight_flush) >= 5:
        if straight_flush.max() == 14: # Royal Straight Flush (Стрит Флеш Роял)
            score = 9
        else: # Straight Flush (Стрит Флеш)
            score = 8
            kickers = get_simple_kickers(straight_flush)
    elif n_duplicates(cards) == 4: # Four of a Kind (Каре)
        score = 7
        kickers = get_simple_kickers(cards['rank'], twin_comb=2)
    elif n_duplicates(cards) == 3 and is_twopair(cards): # Full House (Фул Хауз)
        score = 6
        kickers = get_simple_kickers(cards['rank'], twin_comb=2)
    elif len(flush_set(cards)) >= 5: # Flush (Флеш)
        score = 5
        kickers = get_simple_kickers(flush_set(cards))
    elif len(straight_set(cards['rank'])) >= 5: # Straight (Стрит)
        score = 4
        kickers = get_simple_kickers(straight_set(cards['rank']))
    elif n_duplicates(cards) == 3: # Three of a Kind (Сет или Тройка)
        score = 3
        kickers = get_simple_kickers(cards['rank'], twin_comb=3)
    elif is_twopair(cards): # Two Pair (Две пары)
        score = 2
        kickers = get_simple_kickers(cards['rank'], twin_comb=3)
    elif n_duplicates(cards) == 2: # Pair (Пара)
        score = 1
        kickers = get_simple_kickers(cards['rank'], twin_comb=4)
    else: # High Card (Старшая карта)
        score = 0
        kickers = get_simple_kickers(cards['rank'])

    return c[score], score * (100**5*10) + sum([kickers[i] * 100**(4-i)  for i in range(len(kickers))])

def get_df_cards(cards:list):
    res = {'suit': [], 'rank': []}
    for i in cards:
        res['suit'].append(i[0])
        res['rank'].append(int(i[1:]))
    return pd.DataFrame(res)



class TestBestVombinations():
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
    # 1
    def test_hight_card(self):
        # test_1 = ['', '', '', '', '', '', '',]
        test_1 = ['A10', 'B3', 'C4', 'D5', 'B11', 'A2', 'C12',]
        test_1 = get_df_cards(test_1)
        res_1 = get_best_combination(test_1)
        test_2 = ['B7', 'B8', 'C9', 'D10', 'A13', 'D14']
        test_2 = get_df_cards(test_2)
        res_2 = get_best_combination(test_2)
        assert res_1 == ('High_Card', 1211100504)
        assert res_2 == ('High_Card', 1413100908)
    
    # 2
    def test_pair(self):
        test_1 = ['A10', 'B3', 'C4', 'D10', 'B11', 'A2', 'C12',]
        test_1 = get_df_cards(test_1)
        res_1 = get_best_combination(test_1)
        test_2 = ['A14', 'A10', 'B8', 'C9', 'D7', 'A3', 'B10',]
        test_2 = get_df_cards(test_2)
        res_2 = get_best_combination(test_2)        
        assert res_1 == ('Pair', 101012110400)
        assert res_2 == ('Pair', 101014090800)
    
    # 3
    def test_two_pair(self):
        test_1 = ['A10', 'B3', 'C4', 'D10', 'B4', 'A2', 'C12',]
        test_1 = get_df_cards(test_1)
        res_1 = get_best_combination(test_1)
        test_2 = ['A10', 'B7', 'C4', 'D10', 'B4', 'A7', 'C12',]
        test_2 = get_df_cards(test_2)
        res_2 = get_best_combination(test_2)
        assert res_1 == ('Two_Pair', 201004120000)
        assert res_2 == ('Two_Pair', 201007120000) # не проходит
    
    # 4
    def test_three(self):
        test_1 = ['A5', 'B5', 'C5', 'D3', 'B9', 'A2', 'C12',]
        test_1 = get_df_cards(test_1)
        res_1 = get_best_combination(test_1)
        assert res_1 == ('Three_of_a_Kind', 300512090000)
    
    # 5
    def test_straight(self):
        test_1 = ['A14', 'B13', 'A12', 'A11', 'A10', 'C2', 'B4',]
        test_1 = get_df_cards(test_1)
        res_1 = get_best_combination(test_1)
        test_2 = ['A14', 'A2', 'B3', 'C4', 'D5', 'A4', 'B10',]
        test_2 = get_df_cards(test_2)
        res_2 = get_best_combination(test_2)
        test_3 = ['A14', 'A10', 'B8', 'C9', 'D7', 'A6', 'B10',]
        test_3 = get_df_cards(test_3)
        res_3 = get_best_combination(test_3)
        assert res_1 == ('Straight', 401413121110)
        assert res_2 == ('Straight', 400504030201)
        assert res_3 == ('Straight', 401009080706)
    
    # 6
    def test_flush(self):
        test_1 = ['A10', 'B9', 'A8', 'A7', 'A6', 'C12', 'A3',]
        test_1 = get_df_cards(test_1)
        res_1 = get_best_combination(test_1)
        test_2 = ['A10', 'A3', 'A4', 'A5', 'B11', 'A2', 'C14',]
        test_2 = get_df_cards(test_2)
        res_2 = get_best_combination(test_2)
        test_3 = ['A14', 'A3', 'A4', 'A9', 'B4', 'A2', 'C14',]
        test_3 = get_df_cards(test_3)
        res_3 = get_best_combination(test_3)
        assert res_1 == ('Flush', 501008070603)
        assert res_2 == ('Flush', 501005040302)
        assert res_3 == ('Flush', 501409040302)
    
    # 7
    def test_full_house(self):
        test_1 = ['A5', 'B5', 'C5', 'A9', 'B9', 'C3', 'A10',]
        test_1 = get_df_cards(test_1)
        res_1 = get_best_combination(test_1)
        test_2 = ['A5', 'B5', 'C5', 'A9', 'B9', 'C9', 'A10',]
        test_2 = get_df_cards(test_2)
        res_2 = get_best_combination(test_2)
        test_3 = ['A5', 'B5', 'C5', 'A3', 'B3', 'C9', 'A9',]
        test_3 = get_df_cards(test_3)
        res_3 = get_best_combination(test_3)
        assert res_1 == ('Full_House', 600509000000)
        assert res_2 == ('Full_House', 600905000000)
        assert res_3 == ('Full_House', 600509000000)
    
    # 8
    def test_four(self):
        test_1 = ['A7', 'B7', 'C7', 'D7', 'A3', 'B9', 'C4',]
        test_1 = get_df_cards(test_1)
        res_1 = get_best_combination(test_1)
        test_2 = ['A7', 'B7', 'C7', 'D7', 'B4', 'B9', 'C4',]
        test_2 = get_df_cards(test_2)
        res_2 = get_best_combination(test_2)
        assert res_1 == ('Four_of_a_Kind', 700709000000)
        assert res_2 == ('Four_of_a_Kind', 700709000000) # не проходит
    
    # 9
    def test_straight_flush(self):
        test_1 = ['A10', 'A9', 'A8', 'A7', 'A6', 'B9', 'C9',]
        test_1 = get_df_cards(test_1)
        res_1 = get_best_combination(test_1)
        test_2 = ['A14', 'A2', 'A3', 'A4', 'A5', 'B3', 'C4',]
        test_2 = get_df_cards(test_2)
        res_2 = get_best_combination(test_2)
        test_3 = ['A14', 'A2', 'B6', 'C4', 'A5', 'A4', 'A3',]
        test_3 = get_df_cards(test_3)
        res_3 = get_best_combination(test_3)
        assert res_1 == ('Straight_Flush', 801009080706)
        assert res_2 == ('Straight_Flush', 800504030201)
        assert res_3 == ('Straight_Flush', 800504030201)
    
    # 10
    def test_royal_flush(self):
        test_1 = ['A14', 'A13', 'A12', 'A11', 'A10', 'A9', 'A8',]
        test_1 = get_df_cards(test_1)
        res_1 = get_best_combination(test_1)
        test_2 = ['A14', 'A13', 'A12', 'A11', 'A10', 'B7', 'C4',]
        test_2 = get_df_cards(test_2)
        res_2 = get_best_combination(test_2)
        assert res_1 == ('Royal_Straight_Flush', 900000000000)
        assert res_2 == ('Royal_Straight_Flush', 900000000000)