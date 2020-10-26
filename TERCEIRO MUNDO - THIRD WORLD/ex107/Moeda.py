def increase(price,rate):
    response = price + (price*rate/100)
    return response


def decrease(price,rate):
    response = price - (price*rate/100)
    return response


def double(price):
    response = price * 2
    return response


def half(price):
    response = price / 2
    return response