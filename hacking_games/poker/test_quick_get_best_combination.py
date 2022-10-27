from func_poker import make_res_combination
from func_poker import cards_to_tuple
from func_poker import get_best_combination


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
        res_1 = get_best_combination(test_1)
        test_2 = ['B7', 'B8', 'C9', 'D10', 'A13', 'D14']
        res_2 = get_best_combination(test_2)
        assert res_1 == ('High_Card', 1211100504)
        assert res_2 == ('High_Card', 1413100908)
    
    # 2
    def test_pair(self):
        test_1 = ['A10', 'B3', 'C4', 'D10', 'B11', 'A2', 'C12',]
        res_1 = get_best_combination(test_1)
        test_2 = ['A14', 'A10', 'B8', 'C9', 'D7', 'A3', 'B10',]
        res_2 = get_best_combination(test_2)        
        assert res_1 == ('Pair', 101012110400)
        assert res_2 == ('Pair', 101014090800)
    
    # 3
    def test_two_pair(self):
        test_1 = ['A10', 'B3', 'C4', 'D10', 'B4', 'A2', 'C12',]
        res_1 = get_best_combination(test_1)
        test_2 = ['A10', 'B7', 'C4', 'D10', 'B4', 'A7', 'C12',]
        res_2 = get_best_combination(test_2)
        assert res_1 == ('Two_Pair', 201004120000)
        assert res_2 == ('Two_Pair', 201007120000)
    
    # 4
    def test_three(self):
        test_1 = ['A5', 'B5', 'C5', 'D3', 'B9', 'A2', 'C12',]
        res_1 = get_best_combination(test_1)
        assert res_1 == ('Three_of_a_Kind', 300512090000)
    
    # 5
    def test_straight(self):
        test_1 = ['A14', 'B13', 'A12', 'A11', 'A10', 'C2', 'B4',]
        res_1 = get_best_combination(test_1)
        test_2 = ['A14', 'A2', 'B3', 'C4', 'D5', 'A4', 'B10',]
        res_2 = get_best_combination(test_2)
        test_3 = ['A14', 'A10', 'B8', 'C9', 'D7', 'A6', 'B10',]
        res_3 = get_best_combination(test_3)
        assert res_1 == ('Straight', 401413121110)
        assert res_2 == ('Straight', 400504030201)
        assert res_3 == ('Straight', 401009080706)
    
    # 6
    def test_flush(self):
        test_1 = ['A10', 'B9', 'A8', 'A7', 'A6', 'C12', 'A3',]
        res_1 = get_best_combination(test_1)
        test_2 = ['A10', 'A3', 'A4', 'A5', 'B11', 'A2', 'C14',]
        res_2 = get_best_combination(test_2)
        test_3 = ['A14', 'A3', 'A4', 'A9', 'B4', 'A2', 'C14',]
        res_3 = get_best_combination(test_3)
        assert res_1 == ('Flush', 501008070603)
        assert res_2 == ('Flush', 501005040302)
        assert res_3 == ('Flush', 501409040302)
    
    # 7
    def test_full_house(self):
        test_1 = ['A5', 'B5', 'C5', 'A9', 'B9', 'C3', 'A10',]
        res_1 = get_best_combination(test_1)
        test_2 = ['A5', 'B5', 'C5', 'A9', 'B9', 'C9', 'A10',]
        res_2 = get_best_combination(test_2)
        test_3 = ['A5', 'B5', 'C5', 'A3', 'B3', 'C9', 'A9',]
        res_3 = get_best_combination(test_3)
        assert res_1 == ('Full_House', 600509000000)
        assert res_2 == ('Full_House', 600905000000)
        assert res_3 == ('Full_House', 600509000000)
    
    # 8
    def test_four(self):
        test_1 = ['A7', 'B7', 'C7', 'D7', 'A3', 'B9', 'C4',]
        res_1 = get_best_combination(test_1)
        test_2 = ['A7', 'B7', 'C7', 'D7', 'B4', 'B9', 'C4',]
        res_2 = get_best_combination(test_2)
        assert res_1 == ('Four_of_a_Kind', 700709000000)
        assert res_2 == ('Four_of_a_Kind', 700709000000)
    
    # 9
    def test_straight_flush(self):
        test_1 = ['A10', 'A9', 'A8', 'A7', 'A6', 'B9', 'C9',]
        res_1 = get_best_combination(test_1)
        test_2 = ['A14', 'A2', 'A3', 'A4', 'A5', 'B3', 'C4',]
        res_2 = get_best_combination(test_2)
        test_3 = ['A14', 'A13', 'A12', 'A11', 'A10', 'B7', 'C4',]
        res_3 = get_best_combination(test_3)
        test_4 = ['A14', 'A2', 'B6', 'C4', 'A5', 'A4', 'A3',]
        res_4 = get_best_combination(test_4)
        assert res_1 == ('Straight_Flush', 801009080706)
        assert res_2 == ('Straight_Flush', 800504030201)
        assert res_3 == ('Straight_Flush', 801413121110)
        assert res_4 == ('Straight_Flush', 800504030201)
    
    # 10
    # def test_royal_flush(self):
        # test_1 = ['A14', 'A13', 'A12', 'A11', 'A10', 'A9', 'A8',]
        # res_1 = get_best_combination(test_1)
        # test_2 = ['A14', 'A13', 'A12', 'A11', 'A10', 'B7', 'C4',]
        # res_2 = get_best_combination(test_2)
        # assert res_1 == ('Royal Straight Flush', 900000000000)
        # assert res_2 == ('Royal Straight Flush', 900000000000)