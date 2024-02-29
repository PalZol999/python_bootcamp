


def make_song(num, drink):
    num=0
    drink=""
    while True:
        if num == 0:
            yield f"No more {drink}"
        elif num ==1:
            yield f"Only 1 bottle of {drink} left!"
        else:
            yield f"{num} bottles of {drink} on the wall."
        num -= 1


def make_song(num=99, drink="soda"):
    while num > 0:
        if num == 1:
            yield f"Only 1 bottle of {drink} left!"
    
        else:
            yield f"{num} bottles of {drink} on the wall."
        num -= 1
    yield f"No more {drink}!"