import file_handler
user_file = file_handler.FileHandler("user_data.json")

def make_user(user):
    user_data = user_file.load_data()
    user_data[user] = {"lvl" : 1, "exp" : 0, "exp_max" : 100, "bal" : 100, "data" : {}}
    user_file.save_data(user_data)

def get_user_data(user):
    user_data = user_file.load_data()
    try:
        return user_data[user]
    except:
        make_user(user)
        return user_file.load_data()[user]

def save_user(user, data):
    user_data = user_file.load_data()
    user_data[user] = data
    user_file.save_data(user_data)

def add_exp(user, exp):
    level_up = False
    user_data = get_user_data(user)
    user_data["exp"] += int(exp)
    if user_data["exp"] >= user_data["exp_max"]:
        user_data["lvl"] += 1
        user_data["exp"] -= 100
        user_data["bal"] += 100
        user_data["exp_max"] += user_data["exp_max"]
        level_up = True
    save_user(user, user_data)
    return level_up

def add_bal(user, bal):
    user_data = get_user_data(user)
    user_data["bal"] += bal
    save_user(user, user_data)

def get_bal(user):
    user_data = get_user_data(user)
    return user_data["bal"] 

def get_lvl(user):
    user_data = get_user_data(user)
    return user_data["lvl"]

def get_data(user):
    user_data = get_user_data(user)
    return user_data["data"]

def write_data(user, data):
    user_data = get_user_data(user)
    user_data["data"] = data
    save_user(user, user_data)

def set_bal(user, bal):
    user_data = get_user_data(user)
    user_data["bal"] = bal
    save_user(user, user_data)