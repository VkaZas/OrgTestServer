import os

project_path = os.path.split(os.path.abspath(__file__))[0]

PRIZE_TABLE_PATH = os.path.join(project_path, 'model/prize_table.csv')
PROB_TABLE_PATH = os.path.join(project_path, 'model/prob_table.csv')

prize_dict = []
prob_dict = []
