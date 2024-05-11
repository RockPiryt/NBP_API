from random import randrange
from datetime import timedelta

def random_date(start, end):
    """This function will return a random datetime between two datetime 
    objects."""

    delta = end - start #róznica w dniach
    # zamieniam dzień na sekundy i dodaje różnice sekund
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta) #losuje losową ilość sekund
    return start + timedelta(seconds=random_second)

# The precision is seconds. You can increase precision up to microseconds, 
# or decrease to, say, half-hours, if you want. For that just change the last line's calculation.

from datetime import datetime

d1 = datetime.strptime('1/1/2010 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('1/1/2023 4:50 AM', '%m/%d/%Y %I:%M %p')


created_date = random_date(d1, d2).strftime("%Y-%m-%d")
# print(created_date)