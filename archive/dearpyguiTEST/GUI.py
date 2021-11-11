import dearpygui.dearpygui as dpg
import helper

dpg.create_context()
dpg.create_viewport(title='Easy Sampler', width=300, height=300)

def inputUrl_callback(sender, app_data, user_data):
    print(sender)
    url = helper.promptUserForDirectory()
    app_data["OUTPUT_PATH"] = url

def youtubeSampler_callback(sender, app_data, user_data):
    print(sender)
    print(app_data)
    print(user_data)
    with dpg.window(label="Youtube Sampler", width=300, height=300):
        dpg.add_input_text(label="URL")
        dpg.add_button(label="Choose Output Folder",callback=inputUrl_callback)
        print(type(app_data["OUTPUT_PATH"]))
        if (type(app_data["OUTPUT_PATH"]) == str):
            dpg.add_text(app_data["OUTPUT_PATH"])
        else:
            dpg.add_text(app_data["OUTPUT_PATH"])
        dpg.add_radio_button(items=["Playlist","Video"])
        dpg.add_button(label="Start Sampling")

        
    

with dpg.viewport_menu_bar():
    with dpg.menu(label="File"):
        dpg.add_menu_item(label="Save")
        dpg.add_menu_item(label="Save As")

        with dpg.menu(label="Settings"):
            dpg.add_menu_item(label="Setting 1")
            dpg.add_menu_item(label="Setting 2")

    with dpg.menu(label="Open"):
        dpg.add_menu_item(label="Youtube Sampler", callback=youtubeSampler_callback)

    dpg.add_menu_item(label="Help")

    


    with dpg.menu(label="Widget Items"):
        dpg.add_checkbox(label="Pick Me")
        dpg.add_button(label="Press Me")
        dpg.add_color_picker(label="Color Me")



dpg.set_viewport_small_icon("./img/record.ico")
dpg.set_viewport_large_icon("./img/record.ico")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.show_documentation()
dpg.start_dearpygui()
dpg.destroy_context()