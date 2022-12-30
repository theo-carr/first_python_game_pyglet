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
        self.startStateBatch = pyglet.graphics.Batch()
        self.state = 'start'
        self.startlabel = pyglet.text.Label("WELCOME TO ECON TOWER",
                                       font_name = 'Times New Roman',
                                       font_size = 36,
                                       x = self.width//2, y = self.width//2,
                                       anchor_x = 'center', anchor_y = 'center',
                                       batch = self.startStateBatch)
        self.usernameEntry = ''
        self.usernameWidget = TextWidget(self.usernameEntry,
                                          x = self.width//2, y = self.height//2 - 100,
                                          batch = self.startStateBatch,
                                          width = self.width//5)
        self.text_cursor = self.get_system_mouse_cursor('text')

        self.focus = None
        self.set_focus(self.usernameWidget)

    """
    event handling
    with pyglet, we can just def event methods in the class and it will do the heavy lifting

    """
    def on_draw(self):
        if self.state == 'start':
            self.clear()
            self.startlabel.draw()
            #create user entry text box              
            self.startStateBatch.draw()
           # self.usernameLabel.updateText(updateStr = self.usernameEntry)
    def set_focus(self, focus):
        if focus is self.focus:
            return

        if self.focus:
            self.focus.caret.visible = False
            self.focus.caret.mark = self.focus.caret.position = 0

        self.focus = focus
        if self.focus:
            self.focus.caret.visible = True

            

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

class TextWidget:
    def __init__(self, text, x, y, width, batch):
        self.document = pyglet.text.document.UnformattedDocument(text)
        self.document.set_style(0, len(self.document.text), dict(color=(0, 0, 0, 255)))
        font = self.document.get_font()
        height = font.ascent - font.descent

        self.layout = pyglet.text.layout.IncrementalTextLayout(self.document, width, height, batch=batch)
        self.layout.position = x, y, 0
        self.caret = pyglet.text.caret.Caret(self.layout)
        # Rectangular outline
        pad = 2
        self.rectangle = pyglet.shapes.Rectangle(x - pad, y - pad, width + pad, height + pad, (200, 200, 220), batch)

    def hit_test(self, x, y):
        return (0 < x - self.layout.x < self.layout.width and
                0 < y - self.layout.y < self.layout.height)



    



def main():
    window = MainWindow()
    pyglet.app.run()

if __name__ == "__main__":
    main()
         