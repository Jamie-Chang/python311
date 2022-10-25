city1 = {
    "name": "London",
    "country": "UK",
}

city2 = {
    "name": "New York",
}

def ticket():
    print(f"{city1['name']}, {city1['country']} -> {city2['name']}, {city2['country']}")


if __name__ == "__main__":
    ticket()
