import time
print('Mimdal: Hy my name is Mimdal. Who are you?')
cont = 10

name = input(str('My name is : '))
age = input("I'm : ")

if int(age) <= 17:
    print("Mimdal: wldi bra.")
    if name.lower()== ("said") or name.lower() == ("tofah"):
        print("You: Noooo, my name is ", name,"!")
    time.sleep(2)
    if name.lower()!= ("said") or name.lower() != ("tofah"):
        print("You: No plzzz.")
    time.sleep(2)
    if name.lower() == "said" or name.lower() == "tofa7":
        print("Mimdal: Soooooo ur name is ", name," my brother, right? ok sf sir lhiiiiiiiiiiiiiiiiiiiih!")
    else:
        print("Mimdal: so I have one question for, u have Bra Bra?(Y/N).")
        a = input("Y/N: ")
        if a.lower() != "y":
            print("Nah, I don't have it")
            time.sleep(2)
            print("Mimdal: Maxi")
        else:
            print("Y..Yes,yes! I have it.")
            time.sleep(2)
            print("Mimdal: Ta ana 3andi hhhh.")
            time.sleep(2)
            print("Mimdal: ila dhakti nzidk 5 points.")
            f = input("Laugh(Y/N): ")
            if f.lower() == "y":
                print("Mimdal: Mzyan.")
            else:
                print("Mimdal: Haya bahija radi dhak.")
                time.sleep(2)
                print("Bahija: hhhhh.")
else:
    print("Mimdal: Mzyan.")
while True:
    cmd = input("press Enter to exit:  ")
    if cmd == "":
        break
    
