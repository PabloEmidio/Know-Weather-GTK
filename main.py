import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import datetime
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
        
        # self.temp_simbol = builder.get_object('temp_simbol')
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

        
    def onDestroy(self, *args):
        Gtk.main_quit()
        
    def on_button_search_clicked(self, widget):
        # now.strftime('%A') to know how weekday is
        
        import re, unicodedata
        word = unicodedata.normalize('NFD', self.entry.get_text())
        word = re.sub('[\u0300-\u036f]', '', word)
        try:
            now = datetime.datetime.now()
            current_hour = int(now.strftime('%H'))
            current_search  = self.weather_instance.get_weather_info(word, current_hour=current_hour)
            
            self.city_name.set_text(current_search['location']['name'] + '/' + current_search['location']['region'])
            # self.weather_icon.set_from_file('./images/weather_icon.png')
            self.city_text.set_text(current_search['current']['condition']['text'])
            self.main_temp.set_text(str(int(current_search['current']['temp_c'])) + '°')
            # self.temp_simbol.set_text(self.which_temp_simbol_is)
            weekday = datetime.date.fromisoformat(current_search['forecast']['forecastday'][0]['date']).strftime('%A')
            self.weekday_name.set_text(weekday)
            self.weekday_name_today.set_text('Today')
            
            today_max_temp = str(int(current_search['forecast']['forecastday'][0]['day']['maxtemp_c']))
            today_min_temp = str(int(current_search['forecast']['forecastday'][0]['day']['mintemp_c']))
            self.temp_today_max.set_text(today_max_temp)
            self.temp_today_min.set_text(today_min_temp)
            
            self.hour_1_now.set_text('Now')
            if int(chance_of_rain := current_search['forecast']['forecastday'][0]['hour'][current_hour]['chance_of_rain'])>0:
                self.hour_1_chance_of_rain.set_text(str(chance_of_rain) + '%')
            self.hour_1_icon.set_from_file('./images/hour_icon/1.png')
            self.hour_1_temp.set_text(str(int(current_search['forecast']['forecastday'][0]['hour'][current_hour]['temp_c'])))
            
            self.hour_2_clock.set_text(str(int(now.strftime('%I'))+1) + now.strftime('%p'))
            if int(chance_of_rain := current_search['forecast']['forecastday'][0]['hour'][current_hour+1]['chance_of_rain'])>0:
                self.hour_1_chance_of_rain.set_text(str(chance_of_rain) + '%')
            self.hour_2_icon.set_from_file('./images/hour_icon/2.png')
            self.hour_2_temp.set_text(str(int(current_search['forecast']['forecastday'][0]['hour'][current_hour+1]['temp_c'])))
            
            self.hour_3_clock.set_text(str(int(now.strftime('%I'))+2) + now.strftime('%p'))
            if int(chance_of_rain := current_search['forecast']['forecastday'][0]['hour'][current_hour+2]['chance_of_rain'])>0:
                self.hour_3_chance_of_rain.set_text(str(chance_of_rain) + '%')
            self.hour_3_icon.set_from_file('./images/hour_icon/3.png')
            self.hour_3_temp.set_text(str(int(current_search['forecast']['forecastday'][0]['hour'][current_hour+2]['temp_c'])))
            
            self.hour_4_clock.set_text(str(int(now.strftime('%I'))+3) + now.strftime('%p'))
            if int(chance_of_rain := current_search['forecast']['forecastday'][0]['hour'][current_hour+3]['chance_of_rain'])>0:
                self.hour_4_chance_of_rain.set_text(str(chance_of_rain) + '%')
            self.hour_4_icon.set_from_file('./images/hour_icon/4.png')
            self.hour_4_temp.set_text(str(int(current_search['forecast']['forecastday'][0]['hour'][current_hour+3]['temp_c'])))
            
            self.hour_5_clock.set_text(str(int(now.strftime('%I'))+4) + now.strftime('%p'))
            if int(chance_of_rain := current_search['forecast']['forecastday'][0]['hour'][current_hour+3]['chance_of_rain'])>0:
                self.hour_5_chance_of_rain.set_text(str(chance_of_rain) + '%')
            self.hour_5_icon.set_from_file('./images/hour_icon/5.png')
            self.hour_5_temp.set_text(str(int(current_search['forecast']['forecastday'][0]['hour'][current_hour+4]['temp_c'])))
                        
                                    
            
            
            # avg_temp = current_search['forecast']['forecastday'][0]['day']['avgtemp_c']

            # self.max_bar.set_max_value(max_temp + 10)
            # self.min_bar.set_max_value(max_temp + 10)
            # self.avg_bar.set_max_value(max_temp + 10)
            
            # self.max_bar.set_value(max_temp)
            # self.min_bar.set_value(min_temp)
            # self.avg_bar.set_value(avg_temp)
            
            # self.max_temp.set_text(str(max_temp) + ' / ' + str(max_temp +10) + 'ºC ')
            # self.min_temp.set_text(str(min_temp) + ' / ' + str(max_temp+10) + 'ºC ')
            # self.avg_temp.set_text(str(avg_temp) + ' / ' + str(max_temp +10) + 'ºC ')
           
        except Exception as error:
            print(f'error {error}')


builder.connect_signals(Handler())
window = builder.get_object('window')
window.show_all()
Gtk.main()