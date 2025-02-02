import app
from styles_loader import load_json_style

print(load_json_style(json_path="assets/styles/default/style.json"))

_app = app.App()
_app.after(1000, _app.music_loop)
_app.mainloop()