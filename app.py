import time
import matplotlib.pyplot as plt

from monitor import get_cpu_usage
from scheduler import classify_host
from vm_manager import migrate_vms, shutdown_host, start_host, get_migration_count
from energy_model import update_energy

print("=== Energy-Aware Cloud Management System ===")

energy_history = []
time_steps = []
t = 0

# Run fixed iterations
for i in range(10):

    cpu = get_cpu_usage()
    state = classify_host(cpu)

    print(f"\nCPU Usage: {cpu}% → State: {state}")

    if state == "UNDERLOADED":
        migrate_vms()
        shutdown_host()

    elif state == "OVERLOADED":
        migrate_vms()
        start_host()

    else:
        print("✅ NORMAL state")

    servers, energy = update_energy(state)

    print(f"Active Servers: {servers}")
    print(f"Energy Consumption: {energy} Watts")
    print(f"Total VM Migrations: {get_migration_count()}")

    # store data
    energy_history.append(energy)
    time_steps.append(t)
    t += 1

    time.sleep(1)

# 📊 PLOT GRAPH
plt.plot(time_steps, energy_history)
plt.title("Energy Consumption Over Time")
plt.xlabel("Time")
plt.ylabel("Energy (Watts)")
plt.grid()

# 👇 IMPORTANT (for Docker + local both)
plt.savefig("energy_graph.png")

# 👇 Only shows graph locally (safe)
try:
    plt.show()
except:
    print("Graph display not supported (Docker mode)")

print("📊 Graph saved as energy_graph.png")