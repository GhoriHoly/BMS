import requests
import time

BASE_URL = 'http://127.0.0.1:5000'

CHARGING_LIMITS = {
    '3-phase 16A': 11,
    '1-phase 16A': 3.6,
    '1-phase 32A': 7.3,
    '3-phase 10A': 6.9
}


MAX_LOAD = CHARGING_LIMITS['3-phase 16A']


def get_station_info():
    response = requests.get(f"{BASE_URL}/info")
    return response.json()


def get_base_load():
    response = requests.get(f"{BASE_URL}/baseload")
    return response.json()


def get_price_per_hour():
    response = requests.get(f"{BASE_URL}/priceperhour")
    return response.json()


def start_charging():
    requests.post(f"{BASE_URL}/charge", json={"charging": "on"})


def stop_charging():
    requests.post(f"{BASE_URL}/charge", json={"charging": "off"})


def reset_battery():
    requests.post(f"{BASE_URL}/discharge", json={"discharging": "on"})


def main():
    print("Resetting battery to initial state...")
    reset_battery()
    time.sleep(1)

    prices = get_price_per_hour()
    base_load = get_base_load()

    print("Starting automated charging controller...")
    while True:
        info = get_station_info()
        hour = info['sim_time_hour']
        current_load = info['base_current_load']
        battery_pct = info['battery_capacity_kWh'] / 46.3 * 100

     
        if battery_pct >= 80:
            print(f"[{hour}:00] Battery reached 80%. Stopping charge.")
            stop_charging()
            break

        # Check lowest price hour
        lowest_price_hour = prices.index(min(prices))
        if hour == lowest_price_hour and current_load < MAX_LOAD:
            print(f"[{hour}:00] Lowest price hour & load ({current_load} kW) under {MAX_LOAD} kW. Charging...")
            print(f"Charge: {battery_pct} %")
            start_charging()
        else:
            print(f"[{hour}:00] Not optimal to charge (Load: {current_load} kW, Price hour: {prices[hour]} Öre). Stopping...")
            stop_charging()

        time.sleep(4) 

    print("Charging session completed.")


if __name__ == "__main__":
    main()
