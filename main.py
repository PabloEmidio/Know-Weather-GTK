import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from datetime import datetime
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
        self.city_text = builder.get_object('city_text')
        self.main_temp = builder.get_object('main_temp')
        
        self.which_temp_simbol_is = 'Celsius'

        self.weekday_name = builder.get_object('weekday_name')
        self.weekday_name_today = builder.get_object('weekday_name_today')
        
        self.temp_today_max = builder.get_object('today_max')
        self.temp_today_min = builder.get_object('today_min')
        
        self.hour_1_now = builder.get_object('hour_1_now')
        self.hour_1_chance_of_rain = builder.get_object('hour_1_chance_of_rain')
        self.hour_1_icon = builder.get_object('hour_1_icon')
        self.hour_1_temp = builder.get_object('hour_1_temp')

        self.hour_2_clock = builder.get_object('hour_2_clock')
        self.hour_2_chance_of_rain = builder.get_object('hour_2_chance_of_rain')
        self.hour_2_icon = builder.get_object('hour_2_icon')
        self.hour_2_temp = builder.get_object('hour_2_temp')

        self.hour_3_clock = builder.get_object('hour_3_clock')
        self.hour_3_chance_of_rain = builder.get_object('hour_3_chance_of_rain')
        self.hour_3_icon = builder.get_object('hour_3_icon')
        self.hour_3_temp = builder.get_object('hour_3_temp')

        self.hour_4_clock = builder.get_object('hour_4_clock')
        self.hour_4_chance_of_rain = builder.get_object('hour_4_chance_of_rain')
        self.hour_4_icon = builder.get_object('hour_4_icon')
        self.hour_4_temp = builder.get_object('hour_4_temp')

        self.hour_5_clock = builder.get_object('hour_5_clock')
        self.hour_5_chance_of_rain = builder.get_object('hour_5_chance_of_rain')
        self.hour_5_icon = builder.get_object('hour_5_icon')
        self.hour_5_temp = builder.get_object('hour_5_temp')
        
        self.day_1_name = builder.get_object('day_1_name')
        self.day_1_icon = builder.get_object('day_1_icon')
        self.day_1_temp_max = builder.get_object('day_1_temp_max')
        self.day_1_temp_min = builder.get_object('day_1_temp_min')
        
        self.day_2_name = builder.get_object('day_2_name')
        self.day_2_icon = builder.get_object('day_2_icon')
        self.day_2_temp_max = builder.get_object('day_2_temp_max')
        self.day_2_temp_min = builder.get_object('day_2_temp_min')

        
    def onDestroy(self, *args):
        Gtk.main_quit()
        
        
    def on_button_search_clicked(self, widget):
        # now.strftime('%A') to know how weekday is
        import re, unicodedata
        word = unicodedata.normalize('NFD', self.entry.get_text())
        word = re.sub('[\u0300-\u036f]', '', word)
        try:
            now = datetime.now()
            current_hour = int(now.strftime('%H'))
            current_search  = self.weather_instance.get_weather_info(word, current_hour=current_hour)
            
            self.city_name.set_text(current_search['location']['name'] + '/' + current_search['location']['region'])
            self.city_text.set_text(current_search['current']['condition']['text'])
            self.main_temp.set_text(str(int(current_search['current']['temp_c'])) + '°')
            weekday = now.strftime('%A')
            self.weekday_name.set_text(weekday)
            self.weekday_name_today.set_text('Today')
            
            today_max_temp = str(int(current_search['forecast']['forecastday'][0]['day']['maxtemp_c']))
            today_min_temp = str(int(current_search['forecast']['forecastday'][0]['day']['mintemp_c']))
            self.temp_today_max.set_text(today_max_temp)
            self.temp_today_min.set_text(today_min_temp)
            
            ### Hours informations ######################################################
            def is_available(increase: int) -> bool:
                return not (current_hour + increase > 23)
            
            if is_available(0):
                self.hour_1_now.set_text('Now')
                if int(chance_of_rain := current_search['forecast']['forecastday'][0]['hour'][current_hour]['chance_of_rain'])>0:
                    self.hour_1_chance_of_rain.set_text(str(chance_of_rain) + '%')
                self.hour_1_temp.set_text(str(int(current_search['forecast']['forecastday'][0]['hour'][current_hour]['temp_c'])))
            else:
                self.hour_1_now.set_text('unavailable')
                self.hour_1_temp.set_text('tomorrow')
            self.hour_1_icon.set_from_file('./images/hour_icon/1.png')
                
            if is_available(1):
                self.hour_2_clock.set_text(str(int(now.strftime('%I'))+1) + now.strftime('%p'))
                if int(chance_of_rain := current_search['forecast']['forecastday'][0]['hour'][current_hour+1]['chance_of_rain'])>0:
                    self.hour_1_chance_of_rain.set_text(str(chance_of_rain) + '%')
                self.hour_2_temp.set_text(str(int(current_search['forecast']['forecastday'][0]['hour'][current_hour+1]['temp_c'])))
            else:
                self.hour_2_clock.set_text('unavailable')
                self.hour_2_temp.set_text('tomorrow')
            self.hour_2_icon.set_from_file('./images/hour_icon/2.png')
                
            if is_available(2):
                self.hour_3_clock.set_text(str(int(now.strftime('%I'))+2) + now.strftime('%p'))
                if int(chance_of_rain := current_search['forecast']['forecastday'][0]['hour'][current_hour+2]['chance_of_rain'])>0:
                    self.hour_3_chance_of_rain.set_text(str(chance_of_rain) + '%')
                self.hour_3_temp.set_text(str(int(current_search['forecast']['forecastday'][0]['hour'][current_hour+2]['temp_c'])))
            else:
                self.hour_3_clock.set_text('unavailable')
                self.hour_3_temp.set_text('tomorrow')
            self.hour_3_icon.set_from_file('./images/hour_icon/3.png')
            
            if is_available(3):
                self.hour_4_clock.set_text(str(int(now.strftime('%I'))+3) + now.strftime('%p'))
                if int(chance_of_rain := current_search['forecast']['forecastday'][0]['hour'][current_hour+3]['chance_of_rain'])>0:
                    self.hour_4_chance_of_rain.set_text(str(chance_of_rain) + '%')
                self.hour_4_temp.set_text(str(int(current_search['forecast']['forecastday'][0]['hour'][current_hour+3]['temp_c'])))
            else:
                self.hour_4_clock.set_text('unavailable')
                self.hour_4_temp.set_text('tomorrow')
            self.hour_4_icon.set_from_file('./images/hour_icon/4.png')
                
            if is_available(4):
                self.hour_5_clock.set_text(str(int(now.strftime('%I'))+4) + now.strftime('%p'))
                if int(chance_of_rain := current_search['forecast']['forecastday'][0]['hour'][current_hour+3]['chance_of_rain'])>0:
                    self.hour_5_chance_of_rain.set_text(str(chance_of_rain) + '%')
                self.hour_5_temp.set_text(str(int(current_search['forecast']['forecastday'][0]['hour'][current_hour+4]['temp_c'])))
            else:
                self.hour_5_clock.set_text('unavailable')
                self.hour_5_temp.set_text('tomorrow')
            self.hour_5_icon.set_from_file('./images/hour_icon/5.png')
            
                        
            ### days informations ######################################################
            self.day_1_name.set_text(datetime.fromisoformat(current_search['forecast']['forecastday'][1]['date']).strftime('%A'))
            self.day_1_icon.set_from_file('./images/days_icon/1.png')
            self.day_1_temp_max.set_text(str(int(current_search['forecast']['forecastday'][1]['day']['maxtemp_c'])))
            self.day_1_temp_min.set_text(str(int(current_search['forecast']['forecastday'][1]['day']['mintemp_c'])))

            self.day_2_name.set_text(datetime.fromisoformat(current_search['forecast']['forecastday'][2]['date']).strftime('%A'))
            self.day_2_icon.set_from_file('./images/days_icon/2.png')
            self.day_2_temp_max.set_text(str(int(current_search['forecast']['forecastday'][2]['day']['maxtemp_c'])))
            self.day_2_temp_min.set_text(str(int(current_search['forecast']['forecastday'][2]['day']['mintemp_c'])))
        except Exception as error:
            print(f'error {error}')
        

builder.connect_signals(Handler())
window = builder.get_object('window')
window.show_all()
Gtk.main()