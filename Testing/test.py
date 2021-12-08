import random

print("Welcome to the game, 'Killers Who Practice Cardio!' Here is a brief introduction to this game:")
print('You are a mage who is the target of a pair of assassins.\n'
'assassin 1 is fast but can only kill you when once they are right next to you\n'
'assassin 2 is slower but can shoot and kill you within the range of 5 miles\n')

print('To survive, read carefully: \n'
'1. you must outrun the assassins on your horse, Roach, and get to the magic forest at the edge of the kingdom.'
'2. There, you will be safe. There are 150 miles in the kingdom. Get to the forest without being killed. \n'
'3. If it rains, you will not go as quickly.\n'
'4. If Roach dies, you can run on foot. You are slower than Roach. \n'
'5. The assassins move at different speeds, and have different ways of killing you. \n'
'6. You will get hungry, and if you starve, you will obviously die. So be careful. \n'
'7. Since I, the creator of the game, understand the cruel nature of my audience, you can attack people \n'
'8. If you kill too many people (12 or more), your wizard clan will banish you. Have morals.\n'
'Good luck.\n ')

milesTraveled = 0
hunger = 0
food = 3
roachExhaustion = 0
assassin1Distance = 20
assassin2Distance = 20
assassin3Distance = 20
weather = 0
chest = 0
spells = 3
speedBump = 0
killCount = 0


def assassin_distance():
    import arcade

    arcade.open_window(600, 600, "Drawing Example")

    arcade.set_background_color(arcade.csscolor.SKY_BLUE)

    arcade.start_render()

    arcade.draw_rectangle_filled(200, 100, 400, 200, arcade.csscolor.GREY)
    arcade.draw_rectangle_filled(500, 100, 400, 200, arcade.csscolor.GREY)
    arcade.draw_rectangle_filled(200, 100, 300, 500, arcade.csscolor.GREY)
    arcade.draw_rectangle_filled(50, 50, 50, 50, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(50, 150, 50, 50, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(250, 50, 50, 50, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(350, 50, 50, 50, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(450, 50, 50, 50, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(550, 50, 50, 50, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(100, 250, 50, 50, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(200, 250, 50, 50, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(100, 325, 50, 50, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(200, 325, 50, 50, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(300, 325, 50, 50, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(300, 250, 50, 50, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(250, 150, 50, 50, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(350, 150, 50, 50, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(450, 150, 50, 50, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(550, 150, 50, 50, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(150, 50, 100, 250, arcade.csscolor.WHITE)
    arcade.draw_circle_outline(175, 75, 15, arcade.csscolor.BLACK)

    arcade.finish_render()
    arcade.run()