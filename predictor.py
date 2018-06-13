import settings as S
import random


def validate_attrs(user_attr):
    if user_attr.get('sex') is None or user_attr.get('time') is None or user_attr.get('province') is None:
        return False
    return True


def calc_user_index(user_attr):
    # TODO: Replace this random logic
    index_list = list(S.prob_dict.keys())
    return random.choice(index_list)


def predict(user_attr):
    user_index = calc_user_index(user_attr)
    return S.prize_dict.get(user_index), S.prob_dict.get(user_index)


