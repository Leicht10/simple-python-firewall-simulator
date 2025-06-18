# 🔥 Simple Python Firewall Simulator

This is a basic firewall simulation tool written in Python as part of my learning process. It randomly generates IP addresses and checks them against a static list of firewall rules to decide whether to allow or block traffic.

---

## 💡 What It Does

- Randomly generates IPs in the `192.168.1.0/24` range
- Checks if each IP is in the "blocked" list
- Outputs a simulated action (`block` or `allow`) along with a random event number

---

## 📄 Example Output

<img width="363" alt="Screenshot 2025-06-18 at 18 51 00" src="https://github.com/user-attachments/assets/737dfabb-145a-4cd9-bf7e-4dc7cb6a201a" />


---

## 🧠 Why I Built This

I followed a YouTube tutorial to understand how basic firewall logic can be simulated using Python. I now understand how condition-based filtering works with IPs, and how to use dictionaries and functions in Python.

---

## 🚀 Run the Script

```bash
python3 firewall_sim.py
