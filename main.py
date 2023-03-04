def on_button_pressed_a():
    radio.send_number(0)
    basic.show_icon(IconNames.HAPPY)
    basic.pause(500)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_number(1)
    basic.show_icon(IconNames.SAD)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)
