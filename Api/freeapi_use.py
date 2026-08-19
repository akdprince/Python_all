#We are going to requests freeapi's api to call some data

import requests

def get_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random" 
    response = requests.get(url)
    data = response.json()
    # print(data["statusCode"])
    if data["statusCode"] and "data" in data:
        user_data = data["data"]
        user_name = user_data["login"]["username"]
        country= user_data["location"]["country"]
        return user_name, country
    else:
        raise Exception("Failed to get User Data from freeapi.app")

def main():
    try:
        user_name, country = get_random_user()
        print(f"User Name: {user_name} \n Country: {country}")
    except Exception as e:
        print(str(e))
if __name__ == "__main__":
    main()


 
