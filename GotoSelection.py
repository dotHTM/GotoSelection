import sublime
import sublime_plugin

class GotoSelectionCommand(sublime_plugin.WindowCommand):
    def run(self):
        search = self.window.active_view().substr(self.window.active_view().sel()[0])
        self.window.run_command("show_overlay", {"overlay": "goto", "text": search})