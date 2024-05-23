import json

with open('database\\admin\\user.json', 'r') as ua:
    adminUser = json.load(ua)
    
with open('database\\client\\user.json', 'r') as uc:
    clientUser = json.load(uc)
    
with open('database\\client\\profil.json', 'r') as dc:
    dataClient = json.load(dc)
    
with open('static\\json\\daftar_buku.json', 'r') as lb:
    listBook = json.load(lb)
    
with open('static\\json\\buku.json', 'r') as lbg:
    listGambarBuku = json.load(lbg)
    