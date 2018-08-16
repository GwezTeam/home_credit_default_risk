import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn


file_name_list = ['application_train', 'application_test', 'bureau', 'bureau_balance', 'credit_card_balance',
                  'installments_payments', 'POS_CASH_balance', 'previous_application']
print('importing data ...')
data = {}
try:
    data = {name: pd.read_csv('../all/' + name + '.csv', chunksize=100) for name in file_name_list}
    print('data imported successfully')
except(Exception):
    print('data import failed')
