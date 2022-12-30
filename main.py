import pyglet
from pyglet.text import layout, caret
"""
The main game window which is a subclass of the pyglet window
"""

class MainWindow(pyglet.window.Window):
    def __init__(self) -> None:
        super().__init__()
        #set the state of the game to start, meaning we are on the start menue
        #where we will ask a player if they want to start a new game and get their name 
        self.state = 'start'
        self.startlabel = pyglet.text.Label("WELCOME TO ECON TOWER",
                                       font_name = 'Times New Roman',
                                       font_size = 36,
                                       x = self.width//2, y = self.width//2,
                                       anchor_x = 'center', anchor_y = 'center',)
        # self.document = pyglet.text.document.UnformattedDocument()
        # self.carrot_layout = layout.IncrementalTextLayout(self.document,width=100, height=100)
        # self.carrot = caret.Caret(self.carrot_layout)
        # self.push_handlers(self.carrot)
    """
    event handling
    with pyglet, we can just def event methods in the class and it will do the heavy lifting

    """
    def on_draw(self):
        if self.state == 'start':
            self.clear()
            self.startlabel.draw()
            self.carrot.draw()

    def on_key_press(self, symbol, modifiers):
        print(f"{symbol} was pressed")
        
        #detect the shift key like so
        if modifiers == 1:  
            print('shift is held down')
    
    def on_key_release(self, symbol, modifiers):
        print('key released')

    def on_mouse_press(self, x,y,button, modifiers):
        print(f"Mouse was pressed at point {(x, y)}")
    
    def on_text(self, text):
        print(text)


    



def main():
    window = MainWindow()
    pyglet.app.run()

if __name__ == "__main__":
    main()
         