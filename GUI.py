import dearpygui.dearpygui as dpg
import helper

dpg.create_context()
dpg.create_viewport(title='Easy Sampler', width=600, height=200)

def inputUrl_callback(sender, app_data, user_data):
    print(sender)
    url = helper.promptUserForDirectory()
    print(url)
    return url

def samplePlaylist_callback(sender, app_data, user_data):
    print(sender)
    with dpg.window(label="Playlist Sampler"):
        dpg.add_button(label="Pick Output Folder",callback=inputUrl_callback)
    

    

with dpg.viewport_menu_bar():
    with dpg.menu(label="File"):
        dpg.add_menu_item(label="Save")
        dpg.add_menu_item(label="Save As")

        with dpg.menu(label="Settings"):
            dpg.add_menu_item(label="Setting 1")
            dpg.add_menu_item(label="Setting 2")

    dpg.add_menu_item(label="Help")

    with dpg.menu(label="Widget Items"):
        dpg.add_checkbox(label="Pick Me")
        dpg.add_button(label="Press Me")
        dpg.add_color_picker(label="Color Me")

with dpg.window(label="Youtube Sampler", width=300, height=300):
    dpg.add_text("Simply Sample")
    dpg.add_button(label="Sample Youtube Video")
    dpg.add_button(label="Sample Youtube Playlist",callback=samplePlaylist_callback)

dpg.set_viewport_small_icon("./img/record.ico")
dpg.set_viewport_large_icon("./img/record.ico")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()