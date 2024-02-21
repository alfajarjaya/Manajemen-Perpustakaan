from assets import data_json as db_json
# Database user
db_file = db_json.dbFile
user_file =db_json.dataUser

def validateNama(userName):
    valid = db_json.userValid
    
    for key, value in valid.items():
        return userName in value
def database(user):

    if validateNama(user):
        if user == user_file['fajar']['nama']:
            return db_file['fajar']
        elif user == user_file['bagas']['nama']:
            return db_file['bagas']
        elif user == user_file['sandi']['nama']:
            return db_file['sandi']
        elif user == user_file['angel']['nama']:
            return db_file['angel']
        elif user == user_file['joko']['nama']:
            return db_file['joko']
    else:
        return None