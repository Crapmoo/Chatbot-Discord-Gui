import json
import eel

def properties_write(engine,token,key,chanel):
    try:
        with open("settings.json", "w") as file:
            settings = {"engine":engine,"token":token,"key":key,"chanel":chanel}
            json.dump(settings, file)
    except Exception as e:
        print(e)

@eel.expose
def properties_read():
    try:
        with open("settings.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return None


        