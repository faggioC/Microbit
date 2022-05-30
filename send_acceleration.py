from microbit import *
while True:
    a = accelerometer.get_values()
    if button_a.is_pressed():
        btn = 0
        display.show(Image.HAPPY)
    else:
        btn = 1
        display.show(Image.SAD)
    print(a,btn)
    sleep(100)