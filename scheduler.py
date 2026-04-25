LOW_THRESHOLD = 30
HIGH_THRESHOLD = 70

def classify_host(cpu):
    if cpu < LOW_THRESHOLD:
        return "UNDERLOADED"
    elif cpu > HIGH_THRESHOLD:
        return "OVERLOADED"
    else:
        return "NORMAL"