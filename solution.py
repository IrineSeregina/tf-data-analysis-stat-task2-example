import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 432056961 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = x.mean()
    betta = p
    
    return min((loc - 0.092)/(1-alpha) + 0.092, (loc - 0.092)/(betta) + 0.092), max((loc - 0.092)/(1-alpha) + 0.092, (loc - 0.092)/(betta) + 0.092)
