import settings as S
import csv


def load_model():
    prize_dict = {}
    with open(S.PRIZE_TABLE_PATH, encoding='utf8') as prize_file:
        prize_table = csv.reader(prize_file)
        for item in prize_table:
            prize_dict[item[0]] = item[1:]

    prob_dict = {}
    with open(S.PROB_TABLE_PATH) as prob_file:
        probe_table = csv.reader(prob_file)
        for item in probe_table:
            prob_dict[item[0]] = item[1:]

    S.prize_dict = prize_dict
    S.prob_dict = prob_dict


if __name__ == '__main__':
    load_model()

