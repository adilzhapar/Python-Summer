import arcade
Width = 700
Height = 500
Title = "Welcome to Arcade"
Radius = 100

arcade.open_window(Width, Height, Title)

arcade.set_background_color(arcade.color.BLUEBERRY)

arcade.start_render()
arcade.draw_circle_filled(
    Width/2, Height/2, Radius, arcade.color.PINE_GREEN
)
arcade.finish_render()
arcade.run()