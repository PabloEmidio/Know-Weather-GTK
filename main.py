import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from api_request import Weather

builder = Gtk.Builder()
builder.add_from_file('./glade/main.glade')

class Handler:
    
    def __init__(self, *args, **kwargs):
        super(Handler, self).__init__(*args, **kwargs)
        
        self.weather_instance = Weather()
        
        self.entry = builder.get_object('entry')
        self.btn_search = builder.get_object('btn_search')
        self.city_name = builder.get_object('city_name')
        self.weather_icon = builder.get_object('weather_icon')
        self.temp = builder.get_object('temp')
        self.temp_simbol = builder.get_object('temp_simbol')
        self.which_temp_simbol_is = 'ºC'
        
        self.max_bar = builder.get_object('max_bar')
        self.min_bar = builder.get_object('min_bar')
        self.avg_bar = builder.get_object('avg_bar')
        
        self.max_temp = builder.get_object('max_temp')
        self.min_temp = builder.get_object('min_temp')
        self.avg_temp = builder.get_object('avg_temp')

        
    def onDestroy(self, *args):
        Gtk.main_quit()
        
    def on_button_search_clicked(self, widget):
        import re, unicodedata
        word = unicodedata.normalize('NFD', self.entry.get_text())
        word = re.sub('[\u0300-\u036f]', '', word)
        try:
            current_search  = self.weather_instance.get_weather_info(word)
            self.city_name.set_text(current_search['location']['name'] + '/' + current_search['location']['region'])
            self.weather_icon.set_from_file('./images/weather_icon.png')
            self.temp.set_text(str(current_search['current']['temp_c']))
            self.temp_simbol.set_text(self.which_temp_simbol_is)
            
            max_temp = current_search['forecast']['forecastday'][0]['day']['maxtemp_c']
            min_temp = current_search['forecast']['forecastday'][0]['day']['mintemp_c']
            avg_temp = current_search['forecast']['forecastday'][0]['day']['avgtemp_c']

            self.max_bar.set_max_value(max_temp + 10)
            self.min_bar.set_max_value(max_temp + 10)
            self.avg_bar.set_max_value(max_temp + 10)
            
            self.max_bar.set_value(max_temp)
            self.min_bar.set_value(min_temp)
            self.avg_bar.set_value(avg_temp)
            
            self.max_temp.set_text(str(max_temp) + ' / ' + str(max_temp +10) + 'ºC ')
            self.min_temp.set_text(str(min_temp) + ' / ' + str(max_temp+10) + 'ºC ')
            self.avg_temp.set_text(str(avg_temp) + ' / ' + str(max_temp +10) + 'ºC ')
           
        except Exception as error:
            print(f'error {error}')


builder.connect_signals(Handler())
window = builder.get_object('window')
window.show_all()
Gtk.main()