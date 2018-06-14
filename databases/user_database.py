import pickle

def save_user(user_type, user_info):
    users = open("users.pkl", "ab")
    user_info["user_type"] = user_type
    pickle.dump(user_info, users)
    users.close()

def get_user(username):
    with open('users.pkl') as f:
        users_info = pickle.load(f)
    for i in range(len(users_info.items())):
        if users_info["first_name"] == username:
            return users_info
        else:
            return "User Does Not Exist In The Database"