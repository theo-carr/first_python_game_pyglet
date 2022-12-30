import pyglet
from pyglet.text import layout, caret
from pyglet.window import key
"""
The main game window which is a subclass of the pyglet window
"""

class MainWindow(pyglet.window.Window):
    def __init__(self) -> None:
        #inherent the pyglet window class and pass resizable = true to it
        super().__init__(resizable = True)
        #set the state of the game to start, meaning we are on the start menue
        #where we will ask a player if they want to start a new game and get their name 
        #self.resizeable = True
        self.state = 'start'
        self.startlabel = pyglet.text.Label("WELCOME TO ECON TOWER",
                                       font_name = 'Times New Roman',
                                       font_size = 36,
                                       x = self.width//2, y = self.width//2,
                                       anchor_x = 'center', anchor_y = 'center',)
        self.usernameEntry = ''
        self.usernameLabel = TextEntryLabel(text=self.usernameEntry,
                                            font_name = 'Times New Roman',
                                            font_size = 26,
                                            bold =True,
                                            x = self.width//2, y = self.height//2 - 50,
                                            anchor_x = 'center', anchor_y = 'center')

    """
    event handling
    with pyglet, we can just def event methods in the class and it will do the heavy lifting

    """
    def on_draw(self):
        if self.state == 'start':
            self.clear()
            self.startlabel.draw()
            #create user entry text box              
            self.usernameLabel.draw()
            self.usernameLabel.updateText(updateStr = self.usernameEntry)
            # keys = key.KeyStateHandler()
            # self.push_handlers(keys)
            print(self.usernameEntry)
            

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
        if self.state == 'start':
            self.usernameEntry += text

"""
CLASS FOR TEXT ENTRY BOXES
"""

class TextEntryLabel(pyglet.text.Label):
    def __init__(self, text='', font_name=None, font_size=None, bold=False, italic=False, stretch=False, color=..., x=0, y=0, z=0, width=None, height=None, anchor_x='left', anchor_y='baseline', align='left', multiline=False, dpi=None, batch=None, group=None, rotation=0):
        super().__init__(text, font_name, font_size, bold, italic, stretch, color, x, y, z, width, height, anchor_x, anchor_y, align, multiline, dpi, batch, group, rotation)
    def updateText(self, updateStr):
        self.text = updateStr



    



def main():
    window = MainWindow()
    pyglet.app.run()

if __name__ == "__main__":
    main()
         