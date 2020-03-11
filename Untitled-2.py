import httplib

conn = httplib.HTTPConnection("owletcare,myshopify,com")

headers = {
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "1dd2ae3b-1efa-4693-8a00-c3ea64b65a6e,83397a81-7a60-4772-af78-fee278776492",
    'Host': "owletcare.myshopify.com:443",
    'cookie': "_secure_admin_session_id=47aebdb42449db4e797d7ff911297f55; shopify_web_return_to=%2Fadmin%2Fapi%2F2019-04%2Fcustomers%2Fsearch.json%3Fquery%3Dphone%3A17193579627; __cfduid=d4f4ecb70b7f5621ff8749b809bb81af01561672196",
    'accept-encoding': "gzip, deflate",
    'authorization': "Basic OTZiMWM2MTMxMTY2OGIwYmQ5MDEyMGFkZDFiZmY2MWQ6NzNlMDBlZmQ0ZDE0ZTZmZWE4Y2JkZDdmMWFmNjNhMmU=",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

conn.request("GET", "admin,api,2019-04,customers,search.json", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))