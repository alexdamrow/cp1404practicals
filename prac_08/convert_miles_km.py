"""
CP1404 Practical 8
Miles to Kilometers Converter
Estimated time: 40 minutes
Actual time:
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

FACTOR_MILES_TO_KM = 1.60934


class ConvertMilesKmApp(App):
    """App for converting miles to kilometers"""
    output_km = StringProperty()

    def build(self):
        """Construct the app."""
        self.title = "Miles and Km converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculations(self, text):
        """Handle the calculations."""
        miles = self.check_valid(text)
        self.output_km = str(miles * FACTOR_MILES_TO_KM)

    def handle_increment(self, text, change):
        """Handle the up and down button and update the input."""
        miles = self.check_valid(text) + change
        self.root.ids.input_number.text = str(miles)

    def check_valid(self, text):
        """Check if an input is valid"""
        try:
            return float(text)
        except ValueError:
            return 0.0


ConvertMilesKmApp().run()
