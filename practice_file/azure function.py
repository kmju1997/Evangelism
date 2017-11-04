import cognitive_face as CF
import requests 


CFKEY = '2da2fd40df54473181a4ebc6368b2ae8'
AFKEY = 'https://evancognitive.azurewebsites.net/api/HttpTriggerJS1?code=rX5USICbFkFanoJpZ5Gz30Zm2LMraaOMfK/cfaZ0aszfqMGude7CDA=='

CF.Key.set(CFKEY)

# 1 = obama 2,3 = emma watson 
img_url1 = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Poster-sized_portrait_of_Barack_Obama.jpg/180px-Poster-sized_portrait_of_Barack_Obama.jpg'
img_url2 = 'https://static.independent.co.uk/s3fs-public/thumbnails/image/2015/03/08/09/emmawatson.jpg'
img_url3 = 'https://media4.s-nbcnews.com/j/newscms/2017_07/1195895/emma-watson-2008-03_1e18a472209f2c73c3032efbc33f9a1a.today-ss-slide-desktop.jpg'

# Image should be the format of 'jpg' or 'png'

detect1 = CF.face.detect(img_url1)
detect2 = CF.face.detect(img_url2)

faceId1 = detect1[0]['faceId']
faceId2 = detect2[0]['faceId']

result = CF.face.verify(faceId1, faceId2)

response = requests.request('POST',AFKEY,json=result)

print(response.text)