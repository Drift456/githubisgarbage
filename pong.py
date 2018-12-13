from sense_hat import SenseHat
sense = SenseHat()

blue = (0, 0, 255)

bat_y = 4

def draw_bat():
    sense.set_pixel(0, bat_y, blue)
    sense.set_pixel(0, bat_y + 1, blue)
    sense.set_pixel(0, bat_y - 1, blue)
    
#main Function----------------
draw_bat()

move_up
