from InstagramAPI import InstagramAPI
user,pwd = 'justgirls.me', '500reaispracada' #your credentials
InstagramAPI = InstagramAPI(user,pwd)       
InstagramAPI.login()                        # login
mediaId='1563293881806422756'    #a media_id
recipients = ["263317393", "2033750601"]                             #array of user_ids. They can be strings or ints
InstagramAPI.direct_share(mediaId, recipients,text='Teste direct bot')