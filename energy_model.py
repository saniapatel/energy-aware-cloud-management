active_servers = 5  # initial servers

def update_energy(state):
    global active_servers

    if state == "UNDERLOADED" and active_servers > 1:
        active_servers -= 1

    elif state == "OVERLOADED":
        active_servers += 1

    # energy model: each server = 100W
    energy = active_servers * 100
    return active_servers, energy