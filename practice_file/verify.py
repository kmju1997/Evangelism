import cognitive_face as CF

# Replace the subscription_key string value with your valid subscription key.
KEY = '3e67dad170bd4ea9b14d65af37183eb9'
CF.Key.set(KEY)

# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# a free trial subscription key, you should not need to change this region.
uri_base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
CF.BaseUrl.set(uri_base)

# The URL of a JPEG image to analyze.
img_url1 = 'https://i.pinimg.com/736x/ba/a9/46/baa9460f4408bf3505bb8dc25bc48568--emma-watson-hair-bob-emma-watson-hair-styles.jpg'
img_url2 = 'https://static.independent.co.uk/s3fs-public/thumbnails/image/2015/03/08/09/emmawatson.jpg'

# Face Detect
detect1 = CF.face.detect(img_url1)
detect2 = CF.face.detect(img_url2)

faceId1 = detect1[0]['faceId']
faceId2 = detect2[0]['faceId']

# Face Verify
result = CF.face.verify(faceId1, faceId2)

print(result)