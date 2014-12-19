#!/usr/bin/env python

import gtk, sys, os, re

SSH = [
        "user@netsnail.cn -p7622",
]

RDESKTOP = [
        "192.168.1.246 -utiger -ptiger -g70%",
]

class ConnectTray():
	def __init__(self):
		self.blinking = False
		self.tray = gtk.StatusIcon()
                self.tray.set_from_stock(gtk.STOCK_CONNECT)
		self.tray.connect('popup-menu', self.popup)

	def do_ssh(self, widget):
                cmd = widget.get_name()
                os.system('gnome-terminal --title "'+cmd+'" --command "ssh -C '+cmd+'" &')

	def do_rdesktop(self, widget):
                cmd = widget.get_name()
                os.system('rdesktop -ken-us -a16 -f -z -N -P -K -xb -xl -r clientname=TIGER -r disk:tmp=/tmp -rclipboard:PRIMARYCLIPBOARD -rdisk:desktop=/home/tiger/Desktop -r sound:remote '+cmd+' &')

	def popup(self, statusicon, button, activate_time):
		pop_menu = gtk.Menu()
                
                for i in SSH:
                        _item = gtk.ImageMenuItem(gtk.STOCK_CONNECT)
                        _item.set_name(i)
                        _item.set_label(i)
                        _item.connect("activate", self.do_ssh)
                        pop_menu.append(_item)
                
                for i in RDESKTOP:
                        _item = gtk.ImageMenuItem(gtk.STOCK_NETWORK)
                        _item.set_name(i)
                        _item.set_label(re.sub(r'-p[^ ]+', '-p***', i))
                        _item.connect("activate", self.do_rdesktop)
                        pop_menu.append(_item)

                pop_menu.append(gtk.SeparatorMenuItem())

                _item = gtk.ImageMenuItem(gtk.STOCK_EDIT)
                _item.set_label('Edit')
                _item.connect("activate", self.edit_self)
                pop_menu.append(_item)

                _item = gtk.ImageMenuItem(gtk.STOCK_REFRESH)
                _item.set_label('Restart')
                _item.connect("activate", self.restart)
                pop_menu.append(_item)

                _item = gtk.ImageMenuItem(gtk.STOCK_QUIT)
                _item.set_label('Quit')
		_item.connect("activate", gtk.main_quit)
		pop_menu.append(_item)
		
		pop_menu.show_all()
		pop_menu.popup(None, None, None, 0, gtk.get_current_event_time())
        def restart(self, widget):
                python = sys.executable
                os.execl(python, python, *sys.argv)
        
        def edit_self(self, widget):
                os.system('emacs '+os.path.realpath(__file__)+' &')

if __name__ == '__main__':
        ConnectTray()
        gtk.main()
