def input_error (func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TypeError as e:
            return "Unknown operation"

    return wrapper

def hello (dictt, *args, **kwargs):
    result = "How can I help you?"
    return result

def all_number(dictt, *args, **kwargs):
    resalt = dictt
    return resalt


def adds(dictt, name, phone):
    if name not in dictt.keys():
        dictt[name] = phone
        resalt = f"New contact: {name} - {phone}"
    return resalt


def phone(dictt, name, *args, **kwargs):
    resalt = dictt[name]
    return resalt


def change(dictt, name, phone, *args, **kwargshell):
    dictt[name] = phone
    resalt = f"New phone for {name} is: {phone}"
    return resalt

def finish (dictt, *args, **kwargshell):
    resalt = "Good bye!"
    return resalt

dictt = {
    "ivan": "0-000-00-00",
    "john": "0-123-45-67"
}

def parsing (user_input):
    xy = user_input.split(" ")
    try:
        if xy[1] != "all" and xy[1] != "bye":
            global name
            name = xy[1]
            try:
                if xy[2] != "":
                    global num
                    num = xy [2]
            except:
                num = ""
    except:
        pass
    return name, num

name, num = "", ""

@input_error
def handler(operation):
    parsing (operation)
    command = {
        "hello": hello,                            
        f"phone {name}": phone,                         
        f"add {name} {num}": adds,                            
        "show all": all_number,                   
        f"change {name} {num}": change,                        
        "good bye": finish,                       
        "close": finish,                          
        "exit": finish
    }
    resalt = command.get(operation)
    return resalt

def main():
    print("User help bot v 0.0.1")
    while 2 > 1:
        h = input("Enter your command: ")
        
        hh = handler(h.lower())
        hhh = handler (dictt, name, num)
        print(hhh)
        if h == "good bye" or h == "close" or h == "exit":
            break



if __name__ == '__main__':
    main()
