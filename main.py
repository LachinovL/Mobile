from kivymd.app import MDApp
from kivymd.uix.picker import MDTimePicker
from datetime import datetime
from playsound import playsound
import collections
import math
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.graphics import Color, Line


Position = collections.namedtuple('Position', 'x y')


class MyClockWidget(FloatLayout):
    def on_parent(self, myclock, parent):
        for i in range(1, 13):
            number = Label(
                text=str(i),
                pos_hint={
                    "center_x": 0.5 + 0.45*math.sin(2 * math.pi * i/12),
                    "center_y": 0.5 + 0.45*math.cos(2 * math.pi * i/12),
                }
            )
            self.ids["face"].add_widget(number)

    def position_on_clock(self, fraction, length):
        center_x = self.size[0]/2*8
        center_y = self.size[1]/2*6
        return Position(
            center_x + length * math.sin(2 * math.pi * fraction),
            center_y + length * math.cos(2 * math.pi * fraction),
        )

    def update_clock(self, *args):
        time = datetime.now()
        hands = self.ids["hands"]
        seconds_hand = self.position_on_clock(time.second/60, length=0.45*hands.size[0])
        minutes_hand = self.position_on_clock(time.minute/60+time.second/3600, length=0.40*hands.size[0])
        hours_hand = self.position_on_clock(time.hour/12 + time.minute/720, length=0.35*hands.size[0])

        hands.canvas.clear()
        with hands.canvas:
            Color(0.2, 0.5, 0.2)
            Line(points=[hands.center_x, hands.center_y, seconds_hand.x, seconds_hand.y], width=1, cap="round")
            Color(0.3, 0.6, 0.3)
            Line(points=[hands.center_x, hands.center_y, minutes_hand.x, minutes_hand.y], width=2, cap="round")
            Color(0.4, 0.7, 0.4)
            Line(points=[hands.center_x, hands.center_y, hours_hand.x, hours_hand.y], width=3, cap="round")


class MyClock(MDApp):
    title = "Часы"
    started = False
    seconds = 0
    event = Clock

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_time, 0)
        #Clock.schedule_interval(self.update_timer, 0)

    def build(self):
        clock_widget = MyClockWidget()
        Clock.schedule_once(clock_widget.update_clock, 0)
        Clock.schedule_interval(clock_widget.update_clock, 1)
        self.root.ids.clock.add_widget(clock_widget)



    #Секундомер
    def update_time(self, obj):
        if self.started:
            self.seconds += obj
        if self.started:
            self.root.ids.start_stop.text_color = 0.88, 0.02, 0.02
            self.root.ids.start_stop.line_color = 0.88, 0.02, 0.02
        else:
            self.root.ids.start_stop.text_color = 0.06, 0.76, 0
            self.root.ids.start_stop.line_color = 0.06, 0.76, 0
        minutes, seconds = divmod(self.seconds, 60)
        part_second = seconds * 100 % 100
        self.root.ids.stopwatch.text = f'[size=45]{int(minutes):02}[/size][size=30]:[/size][size=60]{int(seconds):02}[/size][size=30].[/size][size=30]{int(part_second):02}[/size]'


    def start_stop(self):
        self.root.ids.start_stop.text = 'START' if self.started else 'STOP'
        self.started = not self.started
        self.root.ids.reset.disabled = True if self.started else False

    def reset(self):
        if self.started:
            self.started = False
        self.seconds = 0

    #Будильник
    def get_time(self, instance, time):
        pass


    def on_cancel(self, instance, time):
        pass

    def on_save(self, instance, time):
        self.root.ids.time_label.text = str(time)
        alarm_time = self.root.ids.time_label.text
        self.alarm_start(alarm_time)

    def on_stop(self):
        if self.event == Clock:
            pass
        else:
            self.event.cancel()
            self.root.ids.time_label.text = 'Добавьте будильник'



    def show_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_cancel=self.on_cancel, time=self.get_time, on_save=self.on_save)
        time_dialog.open()

    def alarm_start(self, alarm_time):
        print(f"Будильник установлен на время {alarm_time}...")
        self.update_alarm_time(0)
        self.event = Clock.schedule_interval(self.update_alarm_time, 0)


    def update_alarm_time(self, obj):
        alarm_time = self.root.ids.time_label.text
        alarm_hour = int(alarm_time[0:2])
        alarm_min = int(alarm_time[3:5])
        alarm_sec = int(alarm_time[6:8])
        now = datetime.now()

        current_hour = now.hour
        current_min = now.minute
        current_sec = now.second
        if alarm_hour == current_hour:
            if alarm_min == current_min:
                if alarm_sec == current_sec:
                    print("Подъем!")
                    playsound('data/bd.mp3')
                    self.on_stop()

if __name__ == "__main__":
    MyClock().run()












