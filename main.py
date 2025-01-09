import app

_app = app.App()
_app.after(1000, _app.music_loop)
_app.mainloop()