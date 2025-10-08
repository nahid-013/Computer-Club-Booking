import uuid
def uidCount():
    u = uuid.uuid4()
    number = (u.int % 100000000)  # большое число (128 бит)
    return number