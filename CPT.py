import arcade
import random
import math

WIDTH = 640
HEIGHT = 480

# data map

player_x = WIDTH/2
player_y = HEIGHT/2

rain_x_pos = [100, 200, 300, 400, 350]
rain_y_pos = [480, 480, 480, 480, 480]
rain_radius = [25]

ship_w = [125]
ship_l = [100]

ship_img = arcade.load_texture('images/officialrocket.png')
asteroid_img = arcade.load_texture('images/asteroid.png')


player_health = 100
player_max_health = 100

up_pressed = False
down_pressed = False
left_pressed = False
right_pressed = False

BTN_2_X = 0
BTN_2_Y = 1
BTN_2_WIDTH = 2
BTN_2_HEIGHT = 3
BTN_2_IS_CLICKED = 4
BTN_2_COLOR = 5
BTN_2_COLOR_CLICKED = 6

BTN_3_X = 0
BTN_3_Y = 1
BTN_3_WIDTH = 2
BTN_3_HEIGHT = 3
BTN_3_IS_CLICKED = 4
BTN_3_COLOR = 5
BTN_3_COLOR_CLICKED = 6

current_screen = "menu"

button2 = [WIDTH / 2, 250, 125, 40, False, arcade.color.PURPLE, arcade.color.ELECTRIC_CRIMSON]

button3 = [WIDTH / 2, 325, 125, 40, False, arcade.color.BABY_BLUE_EYES, arcade.color.JADE]


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.schedule(update, 1 / 60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press
    window.on_mouse_release = on_mouse_release

    arcade.run()


def update(delta_time):
    global player_health
    global current_screen
    global player_y
    global up_pressed
    global down_pressed
    global left_pressed
    global right_pressed
    if up_pressed == True:
        player_y += 10
    if down_pressed == True:
        player_y -= 10
    global player_x
    if left_pressed == True:
        player_x -= 10
    if right_pressed == True:
        player_x += 10
    for index in range(len(rain_y_pos)):
        rain_y_pos[index] -= 6

        if rain_y_pos[index] < 0:
            rain_y_pos[index] = random.randrange(HEIGHT, HEIGHT + 50)
            rain_x_pos[index] = random.randrange(0, WIDTH)

    a = rain_radius[0] - ship_w[0]
    b = rain_radius[0] - ship_l[0]
    dist = math.sqrt(a ** 2 + b ** 2)

    if dist < rain_radius[0] + ship_w[0]:
        current_screen == "End"

    if ship_w == rain_x_pos and ship_l == rain_y_pos:
        player_health -= 25

    if player_health == 0:
        current_screen = "End"

    if player_y >= 480:
        up_pressed = False

    if player_y <=0:
        down_pressed = False

    if player_x <=0:
        left_pressed = False

    if player_x >= 635:
        right_pressed = False




def on_draw():
    arcade.start_render()
    global current_screen
    global player_x, player_y
    arcade.start_render()
    # Draw in here...

    x = 180
    y = 325

    if current_screen == "menu":
        if button2[BTN_2_IS_CLICKED]:
            color = button2[BTN_2_COLOR_CLICKED]
        else:
            color = button2[BTN_2_COLOR]

        if button3[BTN_3_IS_CLICKED]:
            color = button3[BTN_3_COLOR_CLICKED]
        else:
            color = button3[BTN_3_COLOR]

        arcade.draw_rectangle_filled(button2[BTN_2_X],
                                     button2[BTN_2_Y],
                                     button2[BTN_2_WIDTH],
                                     button2[BTN_2_HEIGHT],
                                     button2[BTN_2_COLOR])
        arcade.draw_rectangle_filled(button3[BTN_3_X],
                                     button3[BTN_3_Y],
                                     button3[BTN_3_WIDTH],
                                     button3[BTN_3_HEIGHT],
                                     button3[BTN_3_COLOR])
        arcade.draw_text("INSTRUCTIONS", 260, 245, arcade.color.BLACK, 13, 10, "center", 'Calibri', True, False)
        arcade.draw_text("START", 275, 315, arcade.color.BLACK, 20, 15, "center", 'Calibri', True, False)
        arcade.draw_text("READY, SET, LIFTOFF!", 95, 400, arcade.color.WHITE, 35)


    elif current_screen == "instructions":
        arcade.set_background_color(arcade.color.BLACK)
        arcade.draw_text("INSTRUCTIONS", 40, 375, arcade.color.WHITE, 50, 200, "left", "Calibri", True, False)
        arcade.draw_line(40, 360, 600, 360, arcade.color.WHITE, 10)
        arcade.draw_text("IN this game, you will be using the keys W to move up, S to move down, A to move left and D to move Right",  60, 320, arcade.color.WHITE, 15, 250, "left", "arial", False, False)

    elif current_screen == "End":
        arcade.set_background_color(arcade.color.BLACK)
        arcade.draw_text("GAME OVER", x, y, arcade.color.WHITE, 50, 10, "center", "Veneer", True, False)



    elif current_screen == "game":

        arcade.draw_texture_rectangle(player_x, player_y, ship_w[0], ship_l[0], ship_img)
        for x, y in zip(rain_x_pos, rain_y_pos):
            arcade.draw_circle_filled(x, y, rain_radius[0], asteroid_img)
        max_bar_width = 170
        bar_height = 40
        arcade.draw_xywh_rectangle_filled(WIDTH - max_bar_width,
                                          HEIGHT - bar_height,
                                          max_bar_width,
                                          bar_height,
                                          arcade.color.BLACK)

        health_width = player_health / player_max_health * max_bar_width
        arcade.draw_xywh_rectangle_filled(WIDTH - max_bar_width,
                                          HEIGHT - bar_height,
                                          health_width,
                                          bar_height,
                                          arcade.color.APPLE_GREEN)

        arcade.draw_text(f"{player_health}/{player_max_health}",
                         WIDTH - max_bar_width,
                         HEIGHT - bar_height,
                         arcade.color.WHITE,
                         font_size=25)


def on_key_press(key, modifiers):
    global current_screen

    if current_screen == "game":
        global up_pressed
        if key == arcade.key.W:
            up_pressed = True
        global down_pressed
        if key == arcade.key.S:
            down_pressed = True
        global left_pressed
        if key == arcade.key.A:
            left_pressed = True
        global right_pressed
        if key == arcade.key.D:
            right_pressed = True


def on_key_release(key, modifiers):
    global current_screen
    if current_screen == "game":
        global up_pressed
        if key == arcade.key.W:
            up_pressed = False
        global down_pressed
        if key == arcade.key.S:
            down_pressed = False
        global left_pressed
        if key == arcade.key.A:
            left_pressed = False
        global right_pressed
        if key == arcade.key.D:
            right_pressed = False


def on_mouse_press(x, y, button, modifiers):
    global current_screen

    if current_screen == "menu":
        if x > 257 and x < 383 and y > 305 and y < 345:
            current_screen = "game"
        if x > 257 and x < 383 and y > 230 and y < 270:
            current_screen = "instructions"



def on_mouse_release(x, y, button, modifiers):
    global current_screen
    button2[BTN_2_IS_CLICKED] = False
    button3[BTN_3_IS_CLICKED] = False


if __name__ == '__main__':
    setup()
