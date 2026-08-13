import httpx
import json
import os
from dotenv import load_dotenv

profiles = []

load_dotenv()
token = os.getenv("GITHUB_TOKEN")
while True:
    username = input("Enter GitHub username (or type 'exit' to quit): ")
    
    if username.lower() == "exit":
        break
        
    try:
        response = httpx.get(f"https://api.github.com/users/{username}", headers={"Authorization": f"Bearer {token}"})
        
        if response.status_code == 404:
            print("User not found.")
        else:
            data = response.json()
            profile_info = {
                "name": data.get("name"),
                "bio": data.get("bio"),
                "public_repos": data.get("public_repos")
            }
            profiles.append(profile_info)
            print("Name:", profile_info["name"])
            print("Bio:", profile_info["bio"])
            print("Public Repos:", profile_info["public_repos"])

    except Exception as e:
        print("An error occurred:", e)

with open("profiles.json", "w") as f:
    json.dump(profiles, f, indent=4)

print("Profiles saved to profiles.json. Exiting.")