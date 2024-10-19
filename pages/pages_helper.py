import random



def random_date():
    day = random.randint(1, 28)
    month = random.randint(1, 12)
    year = random.randint(1990, 2006)
    return f"{year}{month:02d}{day:02d}"