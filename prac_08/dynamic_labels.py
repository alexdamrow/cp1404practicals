"""
CP1404 prac 8 - Dynamic  labels
Estimated time: 30 minutes
Actual time: 40 minutes
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main program - kivy app where labels are created from list."""
    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Greg", "Mark", "Jacob"]

    def build(self):
        """Build the kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root


    def create_labels(self):
        """Create label from list and add to GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)







DynamicLabelsApp().run()
