import web
import urllib
import urllib2
import json
import os

urls = (
    '/', 'MainHandler',
    '/login', 'LoginHandler'
)
app = web.application(urls, globals())

applify_api_key = "AFMO8PX80XLH"
applify_secret = "2981P50HHL4F07H"
applify_host_name = "localhost:8081"
home = os.path.expanduser("~")



def read_config():
    try:
        f = open(home + "/.agileconfig","r")
        contents = f.read()
        if contents:
            contents = json.loads(contents)
        else:
            contents = {}
        f.close()
    except:
        contents = {}
    return contents


def add_to_config(key, value):
    contents = read_config()
    f = open(home + "/.agileconfig","w")
    contents[key] = value
    f.write(json.dumps(contents))
    f.close()
    return contents


class MainHandler:
    def GET(self):
        url = "http://www.teampura.com/dialog/oauth?"
        url += "api_key=" + applify_api_key
        url += "&redirect_uri=" + str(urllib.quote("http://" + applify_host_name + "/login",''))
        url += "&scope=user,project,items"

        web.redirect(url)

class LoginHandler:
    def GET(self):
        data = web.input(code=None)

        code = data.code.replace(" ", "+")

        url = "http://www.teampura.com/accesstoken?"
        url += "api_key=" + applify_api_key + "&"
        url += "secret_key=" + applify_secret + "&"
        url += "code=" + code

        response = urllib2.urlopen(url)
        api_response = json.loads(response.read())

        print api_response

        add_to_config("teams", api_response["user"]["teams"])
        add_to_config("token", api_response["token"])


        return "<h1> Woooohoooo!.. </h1> <p>Successfully Login!, You can use AGILE CONSOLE.. (^_^)v <p>"



if __name__ == "__main__":
    app.run()