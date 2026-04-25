migration_count = 0

def migrate_vms():
    global migration_count
    migration_count += 1
    print("🔄 Migrating VMs to other servers...")

def shutdown_host():
    print("⚡ Underloaded → shutting down server")

def start_host():
    print("🚀 Overloaded → starting new server")

def get_migration_count():
    return migration_count