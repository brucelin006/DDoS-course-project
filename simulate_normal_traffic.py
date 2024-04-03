import requests
import random
import string
import time


def read_user_agents(file_path):
    """Read user agents from a file and return them as a list."""
    with open(file_path, "r") as file:
        user_agents = file.read().splitlines()
    return user_agents


def generate_random_string(length=10):
    """Generate a random string of fixed length."""
    letters = string.ascii_letters
    return "".join(random.choice(letters) for _ in range(length))


def make_request(url, user_agents):
    """Simulate a random request (GET or POST) with a random user agent."""
    user_agent = random.choice(user_agents)
    headers = {"User-Agent": user_agent}

    # Randomly choose between making a GET or POST request
    if random.choice([True, False]):
        response = requests.get(url, headers=headers)
        print(f"GET /: {response.status_code}")
    else:
        item_name = generate_random_string()  # Generate a random item name
        response = requests.post(
            f"{url}/items/", json={"name": item_name}, headers=headers
        )
        print(f"POST /items/: {response.status_code} - Item: {item_name}")


def simulate_random_traffic(url, iterations, user_agents):
    """Simulate random traffic with random user agents."""
    for i in range(iterations):
        make_request(url, user_agents)
        print(f"current request: {i}")
        time.sleep(random.uniform(0.1, 3))  # Random delay between requests


if __name__ == "__main__":
    user_agents_file_path = "user-agents.txt"
    user_agents = read_user_agents(user_agents_file_path)

    base_url = "http://192.168.70.128:8000"
    number_of_iterations = 100  # Number of random actions to perform

    simulate_random_traffic(base_url, number_of_iterations, user_agents)
