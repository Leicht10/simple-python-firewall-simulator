import random


def generate_random_ip():
    return f"192.168.1.{random.randint(0, 20)}"


def check_firewall_rules(ip, rules):
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return "ALLOWED"


def main():
    firewall_rules = {
        "192.168.1.5": "BLOCKED",
        "192.168.1.6": "BLOCKED",
        "192.168.1.8": "BLOCKED",
        "192.168.1.12": "BLOCKED",
        "192.168.1.14": "BLOCKED",
        "192.168.1.17": "BLOCKED",
        "192.168.1.18": "BLOCKED",
    }

    for _ in range(12):
        ip_address = generate_random_ip()
        action = check_firewall_rules(ip_address, firewall_rules)
        random_number = random.randint(100, 9999)
        if action == "BLOCKED":
            print(
                f" \033[91m\n[Firewall] Incoming connection from {ip_address:<13} → BLOCKED (Port: {random_number:<1})\033]0m")
        else:
            print(
                f" \033[92m\n[Firewall] Incoming connection from {ip_address:<13} → ALLOWED (Port: {random_number:<1})\033]0m")


if __name__ == "__main__":
    main()
