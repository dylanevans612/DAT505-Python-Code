import twitter, datetime, sqlite3, urllib2, time

#console = sqlite3.connect()

while True:

    console = sqlite3.connect("C:\\Users\\dylan_000\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History")
    cursor = console.cursor()

    cursor.execute("SELECT urls.title FROM urls")
    data = cursor.fetchall()

    hist = []

    for row in data: 
        hist.append(row)

    new = str(hist[-1])
    short = new[3:-3]
    console.close

    file = open("TwitterCredentials.txt")
    creds = file.read().split('\n')
    api = twitter.Api(creds[0],creds[1],creds[2],creds[3])
    timestamp = datetime.datetime.utcnow()
    response = api.PostUpdate("Loving life looking at " + str(short))
    print("Status updated to: " + response.text)
    
    time.sleep(3600)

    #console.close()
    #hist = "C\Users\dylan001\AppData\Local\Google\Chrome\UserData\Default"
    #print (hist).read()