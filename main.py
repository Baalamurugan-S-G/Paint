from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse,Color,Line
from kivy.core.window import Window
import random

Window.clearcolor = (1,1,1,1)

class PaintWindow(Widget):
    def on_touch_down(self, touch):
        r=random.randint(0,255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.canvas.add(Color(rgb = (r/255.0,g/255.0,b/255.0)))
        d=30
        #self.canvas.add(Ellipse(pos=(touch.x-d/2,touch.y-d/2),size=(d,d)))
        touch.ud['line']=Line(points=(touch.x,touch.y))
        self.canvas.add(touch.ud['line'])
    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x,touch.y]


class PaintApp(App):
    def build(self):

        rootWindow=Widget()
        self.painter= PaintWindow()
        clearBtn= Button(text='Clear')
        clearBtn.bind(on_release=self.clear_canvas)
        rootWindow.add_widget(self.painter)
        rootWindow.add_widget(clearBtn)
        return rootWindow
    def clear_canvas(self,obj):
        self.painter.canvas.clear()

PaintApp().run()