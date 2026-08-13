import httpx

username = input("Enter GitHub username: ")

try:
    response = httpx.get(f"https://api.github.com/users/{username}")
    
    if response.status_code == 404:
        print("User not found.")
    else:
        data = response.json()
        print("Name:", data.get("name"))
        print("Bio:", data.get("bio"))
        print("Public Repos:", data.get("public_repos"))

except Exception as e:
    print("An error occurred:", e)