import file_handler, datetime
file = file_handler("log.json")

def log(user, message):
    log_data = file.load_data()
    log_data[str(datetime.datetime.now())] = {"user" : user, "data" : message}
    file.save_data(log_data)