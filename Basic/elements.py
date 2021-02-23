#Launch page
temperature_setting = 'com.graph.weather.forecast.channel:id/tgTemperature_setting'
time_format_setting = 'com.graph.weather.forecast.channel:id/tg_format_time_setting'
wind_speed_setting = 'com.graph.weather.forecast.channel:id/rl_wind_speed_format'
lock_screen_setting = 'com.graph.weather.forecast.channel:id/tgLock_settings'
notification_setting = 'com.graph.weather.forecast.channel:id/tgNotifi_settings'
status_bar_setting = 'com.graph.weather.forecast.channel:id/tg_notifi_second_settings'

wind_speed_recyclew = 'com.graph.weather.forecast.channel:id/md_contentRecyclerView'
wind_speed_units = '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.graph.weather.forecast.channel:id/md_contentRecyclerView"/android.widget.LinearLayout]' #mph, km/h, m/s, knots, ft/s (index 0-4)
wind_speed_popup_cancel = 'com.graph.weather.forecast.channel:id/md_buttonDefaultNegative'


#Main page
burger_menu_btn = {
    'class': 'android.widget.ImageButton',
    'xpath': '//android.view.ViewGroup[@resource-id="com.graph.weather.forecast.channel:id/toolbar"/android.widget.ImageButton]'
}
location_in_title = {
    'id': 'com.graph.weather.forecast.channel:id/tvTitle',
    'index': 0,
}
location_btn = {
    'id': 'com.graph.weather.forecast.channel:id/tvTitle',
    'index': 1
}
lock_screen_icon = {
    'id': 'com.graph.weather.forecast.channel:id/iv_lock_home',
    'index': 0,
    'class': 'android.widget.TextView',
}
lock_screen_text = {
    'id': 'com.graph.weather.forecast.channel:id/tv_lock_home',
    'text': 'Lock screen',
}
date = 'com.graph.weather.forecast.channel:id/tvDate'
time = 'com.graph.weather.forecast.channel:id/tvHour'
hour_item = 'com.graph.weather.forecast.channel:id/tvHourItem'
wind_speed = {
    'id': 'com.graph.weather.forecast.channel:id/tv_rain_probability',
    'index': 4,
}
more_details = 'com.graph.weather.forecast.channel:id/llMoreHour'

days_of_the_week_recycle = 'com.graph.weather.forecast.channel:id/rvDay'
each_day_wrapper_class = 'android.widget.LinearLayout' #indexes 0-6
clickable_item_day_of_the_week = 'com.graph.weather.forecast.channel:id/rl_day_of_week'

#Main Menu
home_btn_bm = 'com.graph.weather.forecast.channel:id/llHome'
manage_location_bm = 'com.graph.weather.forecast.channel:id/llLocation'
temperature_bm = 'com.graph.weather.forecast.channel:id/tgTemperature'
lock_screen_bm = 'com.graph.weather.forecast.channel:id/tg_lock_screen'
notification_bm = 'com.graph.weather.forecast.channel:id/tg_alarm'
status_bar_bm = 'com.graph.weather.forecast.channel:id/tg_notifi_ongoing'
remove_bg_bm = 'com.graph.weather.forecast.channel:id/tg_hide_bg'
weather_radar_bm = 'com.graph.weather.forecast.channel:id/llWeatherRadar'
weather_widgets_bm = 'com.graph.weather.forecast.channel:id/ll_weather_widgets'
remove_ads_bm = 'com.graph.weather.forecast.channel:id/ll_get_full_version'
unit_settings_bm = 'com.graph.weather.forecast.channel:id/ll_unit_settings'
version_bm = 'com.graph.weather.forecast.channel:id/tv_version'

#Add Location page
add_location_click = 'com.graph.weather.forecast.channel:id/ll_click_location'
add_location_btn = 'com.graph.weather.forecast.channel:id/ll_add_location'
search_location_texfield = 'com.graph.weather.forecast.channel:id/et_search_location'
item_search_top = 'com.graph.weather.forecast.channel:id/ll_item_search'
delete_location_btn = 'com.graph.weather.forecast.channel:id/ivDelete'
delete_btn_on_popup = 'android:id/button1'
back_btn_edit_location_screen = '//android.view.ViewGroup[@resource-id="com.graph.weather.forecast.channel:id/toolbar_edit"/android.widget.ImageButton]'

#Day of the week page
hourly_weather_text = 'com.graph.weather.forecast.channel:id/tv_hourly_time'





