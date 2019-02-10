#!/usr/bin/python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GObject, Gtk

from os import path
from utils import uri_to_path

class CreateWindow(GObject.GObject):
    __gsignals__ = {
        'refresh': (GObject.SIGNAL_RUN_FIRST, None, ())
    }

    def __init__(self, window, file, uri):
        GObject.GObject.__init__(self)

        self._builder = Gtk.Builder()
        self._builder.add_from_resource('/com/nautilus/create-desktop-entry/ui/create.ui')
        self._builder.connect_signals(self)

        self._window = self._builder.get_object("window")
        self._window.set_transient_for(window)
        self._build_window(file, uri)
        self._window.show_all()


    def _build_window(self, file, uri):

        filename = file.get_name()

        if filename.startswith("."):
            filename = filename[1:]

        self._name = self._builder.get_object("name")
        self._name.set_text(filename.split(".")[0])

        self._description = self._builder.get_object("description")

        self._command = self._builder.get_object("command")
        self._command.set_text(uri)

        self._named_icon = self._builder.get_object("named-icon")
        self._custom_icon = self._builder.get_object("custom-icon")
        self._named_icon_entry = self._builder.get_object("named-icon-entry")
        self._file_chooser = self._builder.get_object("file-chooser")
        self._create_button = self._builder.get_object("create-button")

    def on_required_changed(self, args):
        if not self._name.get_text().strip() or not self._command.get_text().strip():
            self._create_button.set_sensitive(False)
        else:
            self._create_button.set_sensitive(True)

    def on_change_icon_type(self, args):
        if self._named_icon.get_active():
            self._named_icon_entry.set_sensitive(True)
            self._file_chooser.set_sensitive(False)
        else:
            self._named_icon_entry.set_sensitive(False)
            self._file_chooser.set_sensitive(True)

    def on_create(self, args):
        name = self._name.get_text().strip()
        f = open(path.expanduser("~/.local/share/applications/" + name + ".desktop"), "w")

        f.write("[Desktop Entry]\n")
        f.write("Name=" + name + "\n")
        f.write("Comment=" + self._description.get_text().strip()+ "\n")
        f.write("Exec=" + self._command.get_text().strip()+ "\n")
        f.write("Type=Application\n")

        if self._named_icon.get_active():
            icon = self._named_icon_entry.get_text()
        else:
            icon = uri_to_path(self._file_chooser.get_uri())

        f.write("Icon=" + icon.strip())

        self._window.destroy()

    def on_destroy(self, args):
        self._window.destroy()
