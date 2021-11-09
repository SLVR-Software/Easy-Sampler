import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Easy Sampler', width=600, height=300)

def samplePlaylist_callback(sender, app_data, user_data):
    print(sender)
    with dpg.window(label="Playlist Sampler"):
        dpg.add_button(label="okay")



with dpg.window(label="Example Window"):
    dpg.add_text("Simply Sample")
    dpg.add_button(label="Sample Youtube Video")
    dpg.add_button(label="Sample Youtube Playlist",callback=samplePlaylist_callback)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()