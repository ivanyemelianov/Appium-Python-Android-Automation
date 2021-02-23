from behave import given, when, then


@given('Proceed with default settings')
def tap_done_button(context):
    context.app.launch_page.tap_done()


@when('Open main screen')
def main_screen_is_opened(context):
    context.app.main_page.tap_cancel()


@then('Temperature is set to celsius')
def verify_temperature_celsius(context):
    context.app.main_page.verify_temperature_celsius()


@then('Time elements have am or pm')
def verify_12h_timeformat(context):
    context.app.main_page.verify_12h_timeformat()


@then('Wind speed element has km/h')
def verify_kmh_wind_speed(context):
    context.app.main_page.verify_kmh_wind_speed()
