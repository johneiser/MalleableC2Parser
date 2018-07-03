import malleable

try:
    p = malleable.Profile()
    p.ingest("amazon.profile")
    if p.validate():
        request = p.get.construct_client("mydomain.sample", "mydata")
        print request.url, request.headers, request.body
except MalleableError as e:
    print str(e)
