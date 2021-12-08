import arcade
i =0
x = 50
y = 50
arcade.open_window(600, 600, "Drawing Example")

arcade.set_background_color(arcade.csscolor.SKY_BLUE)

arcade.start_render()

arcade.draw_rectangle_filled(200, 100, 400, 200, arcade.csscolor.GREY)
arcade.draw_rectangle_filled(500, 100, 400, 200, arcade.csscolor.GREY)
arcade.draw_rectangle_filled(200, 100, 300, 500, arcade.csscolor.GREY)

for i in range(550):
    arcade.draw_rectangle_filled(x, y, 50, 50, arcade.csscolor.BLACK)
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