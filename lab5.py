class TV():
    def __init__(self, name, total_channels, active_channel, max_vol, active_vol):
        self.tv_name = name
        self.total_channels = total_channels
        self.active_channel = active_channel
        self.max_vol = max_vol
        self.active_vol = 0

    def increase_volume(self):
        if self.active_vol >= self.max_vol:
            return False
        else:
            self.active_vol += 1
            return True
    def change_channel(self, num):
        if num > self.total_channels or num <= 0:
            return False
        else:
            self.active_channel = num
            return True

    def decrease_volume(self):
        if self.active_vol <= 0:
            return False
        else:
            self.active_vol -= 1
            return True
    def str_to_file(self):
        one_string = ( self.tv_name + "," +
                str(self.total_channels) + "," + 
                str(self.active_channel) + "," + 
                str(self.max_vol) + "," + 
                str(self.active_vol))
        return one_string

    def get_name(self):
        return self.tv_name

    def __str__(self):
        return self.tv_name + ", channel:" + str(self.active_channel) + ", volume:" + str(self.active_vol)

def read_file(name):
    fp = open(name, "r")
    if fp == None:
        return None
    tv_objects = []

    while True:
        line = fp.readline()

        if not line: 
            break
        else:
            line = line.replace("\n", "")
            line = line.split(",")
            t = TV(line[0], int(line[1]), int(line[2]), int(line[3]), int(line[4]))
            print(t)
            tv_objects.append(t)
            
    fp.close()

    return tv_objects        
    

def write_file(name, tv_objects):
    tmp = []
    fp = open(name,"w")

    for i in tv_objects:
        tmp.append(i.str_to_file())
    output = "\n".join(tmp)
    fp.write(output)
    fp.close()

def select_TV_menu(tv_objects):
    rval = 0
    while True:
        print("*** Welcome to this TV simulator *** press '0' to quit")
        for i in range(0, len(tv_objects)):
            print(i+1, ") ", tv_objects[i].get_name())
        try:
            rval = int(input("Choose: "))
            if rval == 0:
                return None
            if rval > len(tv_objects) or rval < 1:
                print("Wrong input try again\n\n\n")
                continue
        except:
            print("Wrong input try again\n\n\n")
            continue
        return tv_objects[rval-1]

def adjust_TV_menu():
    str1 = ["1. Change channel",
            "2. Increaste volume",
            "3. Decreaes volume",
            "4. Main menu\n"
            "Choose number: "]
    combo = "\n".join(str1)
    try:
        rval = int(input(combo))
    except:
        return None

    return rval

def main():
    tv_objects = read_file("allaTv.txt")

    while True:
        selected_tv = select_TV_menu(tv_objects)
        if selected_tv == None:
            break

        while True:
            print(selected_tv)
            action = adjust_TV_menu()
            if action == 1:
                number = int(input("Choose channel number: "))
                selected_tv.change_channel(number)
            elif action == 2:
                selected_tv.increase_volume()
            elif action == 3:
                selected_tv.decrease_volume()
            elif action == 4:
                break
            else:
                continue
    
    write_file("allaTv.txt", tv_objects)

main()

