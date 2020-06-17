# importing the requests library
import requests
url = "http://sc17re.pythonanywhere.com"

x = ""
username = ""
password = ""
while x != "quit":
    x = input("Choose your option: ")

    if(x == "register"):
        newUsername = input("Enter username: ")
        newEmail = input("Enter email: ")
        newPassword = input("Enter password: ")
        #request = "http://127.0.0.1:8000/api/register/" + username + "/" + email + "/" + password + "/"
        data = {'username':newUsername,
                'userPassword':newPassword,
                'userEmail':newEmail}
        api = url+ "/api/register/"
        content = requests.post(api,data)
        print(content.text)

    if(x.startswith("login ")):
        username = input("Enter username: ")
        password = input("Enter password: ")
        data = {'username':username,
                'password':password}
        url = x[5:(len(x))]
        api = url + "/api/login/"
        content = requests.get(api,data)
        if not ((content.text.startswith("User: "))):
            username = ""
            password = ""
        print(content.text)

    if(x == "logout"):
        username = ""
        password = ""

    if(x == "list"):
        api = url + "/api/list/"
        content = requests.get(api)
        print(content.text)

    if(x.startswith("average")):
        spaceCount = 0
        professorID = ""
        moduleCode = ""
        for i in x:
            if(i == " "):
                spaceCount+=1
            else:
                if(spaceCount == 1):
                    professorID+=i
                if(spaceCount == 2):
                    moduleCode += i

        api = url+"/api/average/"
        data = {"professorID":professorID,
                "moduleID":moduleCode}
        content = requests.get(api,data)
        print(content.text)

    if(x.startswith("rate ")):
        professorID = ""
        moduleCode = ""
        year = ""
        semester = ""
        rating = ""
        spaceCount = 0
        for i in x:
            if(i == " "):
                spaceCount+=1
            else:
                if(spaceCount == 1):
                    professorID+=i
                if(spaceCount == 2):
                    moduleCode += i
                if(spaceCount == 3):
                    year += i
                if(spaceCount == 4):
                    semester += i
                if(spaceCount == 5):
                    rating += i
        api = url+"/api/rate/"
        print(username)
        data = {"userName":username,
                "professorID":professorID,
                "moduleID":moduleCode,
                "year":year,
                "semester":semester,
                "rating":rating}
        print(api)
        content = requests.post(api,data)
        print(content.text)

    if(x == "view"):
        api = url+"/api/view/"
        content = requests.get(api)
        print(content.text)
