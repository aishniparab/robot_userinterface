import kivy
import time
from kivy.app import App
from dialoguefunc import *
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.base import runTouchApp
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.scatter import Scatter
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

# Screen classes for each screen

# Welcome Screen
class WelcomeScreen(Screen):
    pass

# Screen that calls functions from dialoguefunc.py
class DialogueFuncScreen(Screen):
    pass

# Manages the two screens
class MyScreenManager(ScreenManager):
    pass

root_widget = Builder.load_string('''
#:import SlideTransition kivy.uix.screenmanager.SlideTransition
MyScreenManager:
    WelcomeScreen:
    DialogueFuncScreen:

<WelcomeScreen>:
    canvas.before:
        Color:
            rgb: 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    name: 'welcome'
    FloatLayout:
        Label:
            text: 'Welcome.'
            font_size: 30
            color: 0, 0, 0, 1
            font_name: 'kivy/kivy/data/fonts/helvetica.ttf'

        Button:
            text: '>  '
            font_size: 50
            font_name: 'kivy/kivy/data/fonts/helvetica.ttf'
            color: 0, 0, 0, 1
            halign: 'center'
            height: self.texture_size[1]
            background_color: 1, 1, 1, 0
            size_hint: 0.1, 0.05
            pos_hint: {'x': .47, 'y': .4}
            on_release:
                root.manager.transition.direction = 'left'
                app.root.current = 'second'



<DialogueFuncScreen>:
    canvas.before:
        Color:
            rgb: 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    name: 'second'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Click on a button to play the script. '
            size_hint_max_x: None
            size_hint_y: 0.08
            font_size: 20
            color: 0, 0, 0, 1
            font_name: 'kivy/kivy/data/fonts/helvetica.ttf'
            valign: 'middle'
            haligh: 'center'

        StackLayout:
            orientation: 'tb-lr'
            Button:
                size_hint: None, 0.15
                text: 'Hello..'
                font_size: 11
                color: 1, 1, 1, 1
                background_color: 0, 0, 0, 1
                font_name: 'kivy/kivy/data/fonts/helvetica.ttf'
                size_hint: 0.2, 0.2
                text_size: self.width, None
                halign: 'center'
                height: self.texture_size[1]
                on_press:
                    app.call_func(1)

            Button:
                size_hint: None, 0.15
                text: 'Nice to meet you..'
                font_size: 11
                color: 1, 1, 1, 1
                background_color: 0, 0, 0, 1
                font_name: 'kivy/kivy/data/fonts/helvetica.ttf'
                size_hint: 0.2, 0.2
                text_size: self.width, None
                halign: 'center'
                height: self.texture_size[1]
                valign: 'middle'
                on_press: app.call_func(2)

            Button:
                size_hint: None, 0.15
                text: 'What time do you sleep?..'
                font_size: 11
                color: 1, 1, 1, 1
                background_color: 0, 0, 0, 1
                font_name: 'kivy/kivy/data/fonts/helvetica.ttf'
                size_hint: 0.2, 0.2
                text_size: self.width, None
                halign: 'center'
                height: self.texture_size[1]
                on_press: app.call_func(3)
            Button:
                size_hint: None, 0.15
                text: 'What time do you wake?..'
                font_size: 11
                color: 1, 1, 1, 1
                background_color: 0, 0, 0, 1
                font_name: 'kivy/kivy/data/fonts/helvetica.ttf'
                size_hint: 0.2, 0.2
                text_size: self.width, None
                halign: 'center'
                height: self.texture_size[1]
                on_press: app.call_func(4)
            Button:
                size_hint: None, 0.15
                text: 'How often trouble sleeping?..'
                font_size: 11
                color: 1, 1, 1, 1
                background_color: 0, 0, 0, 1
                font_name: 'kivy/kivy/data/fonts/helvetica.ttf'
                size_hint: 0.2, 0.2
                text_size: self.width, None
                halign: 'center'
                height: self.texture_size[1]
                on_press: app.call_func(5)
            Button:
                size_hint: None, 0.15
                text: 'Feel well-rested when you wake?..'
                font_size: 11
                color: 1, 1, 1, 1
                background_color: 0, 0, 0, 1
                font_name: 'kivy/kivy/data/fonts/helvetica.ttf'
                size_hint: 0.2, 0.2
                text_size: self.width, None
                halign: 'center'
                height: self.texture_size[1]
                on_press: app.call_func(6)
            Button:
                size_hint: None, 0.15
                text: 'Normal to wake up at night?..'
                font_size: 11
                color: 1, 1, 1, 1
                background_color: 0, 0, 0, 1
                font_name: 'kivy/kivy/data/fonts/helvetica.ttf'
                size_hint: 0.2, 0.2
                text_size: self.width, None
                halign: 'center'
                height: self.texture_size[1]
                on_press: app.call_func(7)
            Button:
                size_hint: None, 0.15
                text: 'Sleepy during the day?..'
                font_size: 11
                color: 1, 1, 1, 1
                background_color: 0, 0, 0, 1
                font_name: 'kivy/kivy/data/fonts/helvetica.ttf'
                size_hint: 0.2, 0.2
                text_size: self.width, None
                halign: 'center'
                height: self.texture_size[1]
                on_press: app.call_func(8)
            Button:
                size_hint: None, 0.15
                text: 'How often do you nap?..'
                font_size: 11
                color: 1, 1, 1, 1
                background_color: 0, 0, 0, 1
                font_name: 'kivy/kivy/data/fonts/helvetica.ttf'
                size_hint: 0.2, 0.2
                text_size: self.width, None
                halign: 'center'
                height: self.texture_size[1]
                on_press: app.call_func(9)
            Button:
                size_hint: None, 0.15
                text: 'Fall asleep during task?..'
                font_size: 11
                color: 1, 1, 1, 1
                background_color: 0, 0, 0, 1
                font_name: 'kivy/kivy/data/fonts/helvetica.ttf'
                size_hint: 0.2, 0.2
                text_size: self.width, None
                halign: 'center'
                height: self.texture_size[1]
                on_press: app.call_func(10)

            Button:
                size_hint: None, 0.15
                text: 'Here are some tips for you..'
                font_size: 11
                color: 1, 1, 1, 1
                background_color: 0, 0, 0, 1
                font_name: 'kivy/kivy/data/fonts/helvetica.ttf'
                size_hint: 0.2, 0.2
                text_size: self.width, None
                halign: 'center'
                height: self.texture_size[1]
                on_press: app.call_func(11)
            Button:
                size_hint: None, 0.15
                text: 'Introduce Mindful Breathing Exercise..'
                font_size: 11
                color: 1, 1, 1, 1
                background_color: 0, 0, 0, 1
                font_name: 'kivy/kivy/data/fonts/helvetica.ttf'
                size_hint: 0.2, 0.2
                text_size: self.width, None
                halign: 'center'
                height: self.texture_size[1]
                on_press: app.call_func(12)
            Button:
                size_hint: None, 0.15
                text: 'Mindful Breathing Exercise continued..'
                font_size: 11
                color: 1, 1, 1, 1
                background_color: 0, 0, 0, 1
                font_name: 'kivy/kivy/data/fonts/helvetica.ttf'
                size_hint: 0.2, 0.2
                text_size: self.width, None
                halign: 'center'
                height: self.texture_size[1]
                on_press: app.call_func(13)
            Button:
                size_hint: None, 0.15
                text: 'Abdominal Breathing Exercise..'
                font_size: 11
                color: 1, 1, 1, 1
                background_color: 0, 0, 0, 1
                font_name: 'kivy/kivy/data/fonts/helvetica.ttf'
                size_hint: 0.2, 0.2
                text_size: self.width, None
                halign: 'center'
                height: self.texture_size[1]
                on_press: app.call_func(14)
            Button:
                size_hint: None, 0.15
                text: 'Timed Breathing Exercise..'
                font_size: 11
                color: 1, 1, 1, 1
                background_color: 0, 0, 0, 1
                font_name: 'kivy/kivy/data/fonts/helvetica.ttf'
                size_hint: 0.2, 0.2
                text_size: self.width, None
                halign: 'center'
                height: self.texture_size[1]
                on_press: app.call_func(15)
            Button:
                size_hint: None, 0.15
                text: 'Counting Breathing Exercise..'
                font_size: 11
                color: 1, 1, 1, 1
                background_color: 0, 0, 0, 1
                font_name: 'kivy/kivy/data/fonts/helvetica.ttf'
                size_hint: 0.2, 0.2
                text_size: self.width, None
                halign: 'center'
                height: self.texture_size[1]
                on_press: app.call_func(16)

            Button:
                size_hint: None, 0.15
                text: 'Thank participant..'
                font_size: 11
                color: 1, 1, 1, 1
                background_color: 0, 0, 0, 1
                font_name: 'kivy/kivy/data/fonts/helvetica.ttf'
                size_hint: 0.2, 0.2
                text_size: self.width, None
                halign: 'center'
                height: self.texture_size[1]
                on_press: app.call_func(17)
            Button:
                size_hint: None, 0.15
                text: 'Introduce Colouring Task..'
                font_size: 11
                color: 1, 1, 1, 1
                background_color: 0, 0, 0, 1
                font_name: 'kivy/kivy/data/fonts/helvetica.ttf'
                size_hint: 0.2, 0.2
                text_size: self.width, None
                halign: 'center'
                height: self.texture_size[1]
                on_press: app.call_func(18)
            Button:
                size_hint: None, 0.15
                text: 'Give colouring directions..'
                font_size: 11
                color: 1, 1, 1, 1
                background_color: 0, 0, 0, 1
                font_name: 'kivy/kivy/data/fonts/helvetica.ttf'
                size_hint: 0.2, 0.2
                text_size: self.width, None
                halign: 'center'
                height: self.texture_size[1]
                on_press: app.call_func(19)
            Button:
                size_hint: None, 0.15
                text: 'Cue to begin colouring..'
                font_size: 11
                color: 1, 1, 1, 1
                background_color: 0, 0, 0, 1
                font_name: 'kivy/kivy/data/fonts/helvetica.ttf'
                size_hint: 0.2, 0.2
                text_size: self.width, None
                halign: 'center'
                height: self.texture_size[1]
                on_press: app.call_func(20)
            Button:
                size_hint: None, 0.15
                text: 'Cue to stop colouring..'
                font_size: 11
                color: 1, 1, 1, 1
                background_color: 0, 0, 0, 1
                font_name: 'kivy/kivy/data/fonts/helvetica.ttf'
                size_hint: 0.2, 0.2
                text_size: self.width, None
                halign: 'center'
                height: self.texture_size[1]
                on_press: app.call_func(21)

            Button:
                size_hint: None, 0.15
                text: 'Give Tip: Listen to music..'
                font_size: 11
                color: 1, 1, 1, 1
                background_color: 0, 0, 0, 1
                font_name: 'kivy/kivy/data/fonts/helvetica.ttf'
                size_hint: 0.2, 0.2
                text_size: self.width, None
                halign: 'center'
                height: self.texture_size[1]
                on_press: app.call_func(22)
            Button:
                size_hint: None, 0.15
                text: 'Give Tip: Read vs. Phone..'
                font_size: 11
                color: 1, 1, 1, 1
                background_color: 0, 0, 0, 1
                font_name: 'kivy/kivy/data/fonts/helvetica.ttf'
                size_hint: 0.2, 0.2
                text_size: self.width, None
                halign: 'center'
                height: self.texture_size[1]
                on_press: app.call_func(23)
            Button:
                text: '<'
                font_size: 25
                font_name: 'kivy/kivy/data/fonts/helvetica.ttf'
                color: 0, 0, 0, 1
                halign: 'center'
                height: self.texture_size[1]
                background_color: 1, 1, 1, 0
                size_hint: 0.2, 0.2
                on_release:
                    root.manager.transition.direction = 'right'
                    app.root.current = 'welcome'
            Button:
                text: 'x'
                font_size: 25
                font_name: 'kivy/kivy/data/fonts/helvetica.ttf'
                color: 0, 0, 0, 1
                halign: 'center'
                height: self.texture_size[1]
                background_color: 1, 1, 1, 0
                size_hint: 0.2, 0.2
                on_release:
                    app.stop()
    ''')

# Defining our app
class ScreenManagerApp(App):

    title = 'ReEmbodied Cognition Lab Wizard'

    def build(self):
        return root_widget

    # Calls a function for the corresponding button pressed.
    # Functions are called in the order of the script.
    def call_func(self, int):
        if (int == 1):
            Introduction.hello()
        if (int ==2):
            Introduction.nice2meet()
        if (int == 3):
            SleepDiscussion.whatSleepTime()
        if (int == 4):
            SleepDiscussion.whatWakeTime()
        if (int == 5):
            SleepDiscussion.howOftenSleepTrouble()
        if (int == 6):
            SleepDiscussion.isRestedFeeling()
        if (int == 7):
            SleepDiscussion.normal2wakeNight()
        if (int == 8):
            SleepDiscussion.daySleepy()
        if (int == 9):
            SleepDiscussion.howOftenNap()
        if (int == 10):
            SleepDiscussion.sleepDuringTask()
        if (int == 11):
            SleepDiscussion.feedbackTips()
        if (int == 12):
            SleepExercises.mindfulBreathing()
        if (int == 13):
            SleepExercises.submindfulBreathing()
        if (int == 14):
            SleepExercises.abdominalBreathing()
        if (int == 15):
            SleepExercises.timedBreathing()
        if (int == 16):
            SleepExercises.countBreathing()
        if (int == 17):
            SleepExercises.thankParticipant()
        if (int == 18):
            SleepExercises.colouringTask()
        if (int == 19):
            SleepExercises.colouringDirections()
        if (int == 20):
            SleepExercises.beginColouringCue()
        if (int == 21):
            SleepExercises.stopColouringCue()
        if (int == 22):
            SleepExercises.listenMusicTip()
        if (int == 23):
            SleepExercises.readingVsPhoneTip()

# Run the app.
ScreenManagerApp().run()
