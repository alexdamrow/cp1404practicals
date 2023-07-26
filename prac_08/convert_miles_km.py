"""
CP1404 Practical 8
Miles to Kilometers Converter
Estimated time: 40 minutes
Actual time:
"""
from kivy.app import App
from kivy.lang import Builder


class ConvertMilesKmApp(App):

    def build(self):
        self.title = "Miles and Km converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root




ConvertMilesKmApp().run()