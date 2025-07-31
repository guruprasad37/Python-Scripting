import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes")

complete_detail = response.json()  # Automatically converts json to dictionary

# Print all key-value pairs in the dictionary
for key, value in complete_detail.items():
    print(f"{key}: {value}")