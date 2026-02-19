import random
import config
from utils.logger import log_info

def calculate_customer_score():
    log_info("Calculating customer score")

    # Simulated business logic
    score = random.randint(300, 850)

    return score
