from interface import GptWindow
from openaiRequest import request_gpt
from filemanager import searchKey



key = searchKey()


# Creats an instance of the main window
root = GptWindow(color1="#7657e3",
                 color2="#ffa247",
                 key=key,
                 aFunction=request_gpt
)

root.mainloop()
