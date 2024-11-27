from pywinauto import Application

# Launch or attach to the application
app = Application().connect(title="Minecraft server")  # Replace with the window's title

print(app)
# Access the main window
main_window = app.window(title="Minecraft server")  # Replace with the window's title

textbox = main_window.child_window(control_type="Edit")  # 'Edit' usually corresponds to textboxes
textbox.set_edit_text("say Hello, world!")  # Example command for Minecraft console
