import app
from styles_loader import load_json_style

_app = app.App()
_app.after(1000, _app.music_loop)
_app.mainloop()