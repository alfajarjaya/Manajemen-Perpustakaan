def validateNama(userName):
    name = ['Alfajjar','Bagas','Sandi']
    
    return userName in name

def database(user):
    
    fajar = {
        'user':'Alfajjar',
        'nama': 'Alfajjar Syachputra',
        'nomor_induk': '123',
        'kelas': 'XI TKJ 2'
    }
    
    bagas = {
        'user':'Bagas',
        'nama': 'Bagas Firmansyah',
        'nomor_induk': '456',
        'kelas': 'XI TKJ 1'
    }
    
    sandi = {
        'user':'Sandi',
        'nama': 'Kurnia Sandi',
        'nomor_induk': '789',
        'kelas': 'XI TKJ 3'
    }
    
    if validateNama(user):
        if user == fajar['user']:
            return fajar
        elif user == bagas['user']:
            return bagas
        elif user == sandi['user']:
            return sandi
    else:
        return None    