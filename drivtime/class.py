from datetime import time
from typing import List

def overview(daily: int, weekly: int, fortnightly: int) -> List:
    """[summary]

    Args:
        daily (int): Daily driving used
        weekly (int): Weekly driving used
        fortnightly (int): Fortnightly driving used time

    Returns:
        List: [description]
    """
    
    # Driving period limit
    daily_lim = time(9)
    weekly_lim = time(56)
    fortnightly_lim = time(90)
