import json

with open('D:\\produktif bu Tya\\manajemen_perpustakaan\\static\\json\\database.json', 'r') as db:
    dbFile = json.load(db)    
    
with open('D:\\produktif bu Tya\\manajemen_perpustakaan\\static\\json\\userValid.json', 'r') as user_valid:
    userValid = json.load(user_valid)
    
with open('D:\\produktif bu Tya\\manajemen_perpustakaan\\static\\json\\admin\\user.json', 'r') as user_admin:
    dataAdmin = json.load(user_admin)
    
with open('D:\\produktif bu Tya\\manajemen_perpustakaan\\static\\json\\user\\user.json', 'r') as user_file:
    dataUser = json.load(user_file)

with open('D:\\produktif bu Tya\\manajemen_perpustakaan\\static\\json\\user\\input_user.json', 'r') as inpt_user:
    inputUser = json.load(inpt_user)
    
with open('D:\\produktif bu Tya\\manajemen_perpustakaan\\static\\json\\list-book\\name-book.json', 'r') as listBook:
    book = json.load(listBook)