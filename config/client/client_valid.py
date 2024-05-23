import config.import_json as json

data_client = json.dataClient
user_client = json.clientUser

def databaseProfil(user):
    for key, value in user_client.items():
        if user == value['13062193872']['user']:
            return data_client['3062193872']
        if user == value['20073072979']['user']:
            return data_client['0073072979']
        if user == value['30095071044']['user']:
            return data_client['0095071044']
        if user == value['40065211738']['user']:
            return data_client['0065211738']
        if user == value['50078020225']['user']:
            return data_client['0078020225']
        if user == value['60061948654']['user']:
            return data_client['0061948654']
        if user == value['70075420919']['user']:
            return data_client['0075420919']
        if user == value['80063331972']['user']:
            return data_client['0063331972']
        if user == value['90068791885']['user']:
            return data_client['0068791885']
        if user == value['100065298464']['user']:
            return data_client['0065298464']
        if user == value['110077666331']['user']:
            return data_client['0077666331']
        if user == value['120066882938']['user']:
            return data_client['0066882938']
        if user == value['130064748354']['user']:
            return data_client['0064748354']
        if user == value['140074670648']['user']:
            return data_client['0074670648']
        if user == value['150063450509']['user']:
            return data_client['0063450509']
        if user == value['160074214171']['user']:
            return data_client['0074214171']
        if user == value['170072601683']['user']:
            return data_client['0072601683']
        if user == value['180068540266']['user']:
            return data_client['0068540266']
        if user == value['190069270434']['user']:
            return data_client['0069270434']
        if user == value['200072070493']['user']:
            return data_client['0072070493']
        if user == value['210066954705']['user']:
            return data_client['0066954705']
        if user == value['220077079282']['user']:
            return data_client['0077079282']
        if user == value['230068910949']['user']:
            return data_client['0068910949']
        if user == value['240076810171']['user']:
            return data_client['0076810171']
        if user == value['250067626570']['user']:
            return data_client['0067626570']
        if user == value['260072966532']['user']:
            return data_client['0072966532']
        if user == value['270056964972']['user']:
            return data_client['0056964972']
        if user == value['283063566196']['user']:
            return data_client['3063566196']
        if user == value['290077815617']['user']:
            return data_client['0077815617']
        if user == value['300065074721']['user']:
            return data_client['0065074721']
        if user == value['310062582176']['user']:
            return data_client['0062582176']
        if user == value['320079243170']['user']:
            return data_client['0079243170']
        if user == value['330062293664']['user']:
            return data_client['0062293664']
        if user == value['340074754002']['user']:
            return data_client['0074754002']
        if user == value['350061989492']['user']:
            return data_client['0061989492']
        
    return 'Username not found'

def name_and_pw_client(user,pw):
    
    for key,value in user_client.items():
        if user == value['13062193872']['user'] and pw == value['13062193872']['password']:
            return True
        if user == value['20073072979']['user'] and pw == value['20073072979']['password']:
            return True
        if user == value['30095071044']['user'] and pw == value['30095071044']['password']:
            return True
        if user == value['40065211738']['user'] and pw == value['40065211738']['password']:
            return True
        if user == value['50078020225']['user'] and pw == value['50078020225']['password']:
            return True
        if user == value['60061948654']['user'] and pw == value['60061948654']['password']:
            return True
        if user == value['70075420919']['user'] and pw == value['70075420919']['password']:
            return True
        if user == value['80063331972']['user'] and pw == value['80063331972']['password']:
            return True
        if user == value['90068791885']['user'] and pw == value['90068791885']['password']:
            return True
        if user == value['100065298464']['user'] and pw == value['100065298464']['password']:
            return True
        if user == value['110077666331']['user'] and pw == value['110077666331']['password']:
            return True
        if user == value['120066882938']['user'] and pw == value['120066882938']['password']:
            return True
        if user == value['130064748354']['user'] and pw == value['130064748354']['password']:
            return True
        if user == value['140074670648']['user'] and pw == value['140074670648']['password']:
            return True
        if user == value['150063450509']['user'] and pw == value['150063450509']['password']:
            return True
        if user == value['160074214171']['user'] and pw == value['160074214171']['password']:
            return True
        if user == value['170072601683']['user'] and pw == value['170072601683']['password']:
            return True
        if user == value['180068540266']['user'] and pw == value['180068540266']['password']:
            return True
        if user == value['190069270434']['user'] and pw == value['190069270434']['password']:
            return True
        if user == value['200072070493']['user'] and pw == value['200072070493']['password']:
            return True
        if user == value['210066954705']['user'] and pw == value['210066954705']['password']:
            return True
        if user == value['220077079282']['user'] and pw == value['220077079282']['password']:
            return True
        if user == value['230068910949']['user'] and pw == value['230068910949']['password']:
            return True
        if user == value['240076810171']['user'] and pw == value['240076810171']['password']:
            return True
        if user == value['250067626570']['user'] and pw == value['250067626570']['password']:
            return True
        if user == value['260072966532']['user'] and pw == value['260072966532']['password']:
            return True
        if user == value['270056964972']['user'] and pw == value['270056964972']['password']:
            return True
        if user == value['283063566196']['user'] and pw == value['283063566196']['password']:
            return True
        if user == value['290077815617']['user'] and pw == value['290077815617']['password']:
            return True
        if user == value['300065074721']['user'] and pw == value['300065074721']['password']:
            return True
        if user == value['310062582176']['user'] and pw == value['310062582176']['password']:
            return True
        if user == value['320079243170']['user'] and pw == value['320079243170']['password']:
            return True
        if user == value['330062293664']['user'] and pw == value['330062293664']['password']:
            return True
        if user == value['340074754002']['user'] and pw == value['340074754002']['password']:
            return True
        if user == value['350061989492']['user'] and pw == value['350061989492']['password']:
            return True
        
    return False
        
def user_client_valid(user):
    for key, value in user_client.items():
        if user == value['13062193872']['user']:
            return True
        if user == value['20073072979']['user']:
            return True
        if user == value['30095071044']['user']:
            return True
        if user == value['40065211738']['user']:
            return True
        if user == value['50078020225']['user']:
            return True
        if user == value['60061948654']['user']:
            return True
        if user == value['70075420919']['user']:
            return True
        if user == value['80063331972']['user']:
            return True
        if user == value['90068791885']['user']:
            return True
        if user == value['100065298464']['user']:
            return True
        if user == value['110077666331']['user']:
            return True
        if user == value['120066882938']['user']:
            return True
        if user == value['130064748354']['user']:
            return True
        if user == value['140074670648']['user']:
            return True
        if user == value['150063450509']['user']:
            return True
        if user == value['160074214171']['user']:
            return True
        if user == value['170072601683']['user']:
            return True
        if user == value['180068540266']['user']:
            return True
        if user == value['190069270434']['user']:
            return True
        if user == value['200072070493']['user']:
            return True
        if user == value['210066954705']['user']:
            return True
        if user == value['220077079282']['user']:
            return True
        if user == value['230068910949']['user']:
            return True
        if user == value['240076810171']['user']:
            return True
        if user == value['250067626570']['user']:
            return True
        if user == value['260072966532']['user']:
            return True
        if user == value['270056964972']['user']:
            return True
        if user == value['283063566196']['user']:
            return True
        if user == value['290077815617']['user']:
            return True
        if user == value['300065074721']['user']:
            return True
        if user == value['310062582176']['user']:
            return True
        if user == value['320079243170']['user']:
            return True
        if user == value['330062293664']['user']:
            return True
        if user == value['340074754002']['user']:
            return True
        if user == value['350061989492']['user']:
            return True

    return False