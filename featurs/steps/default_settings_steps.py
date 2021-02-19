from behave import given, when, then


@given('Proceed with default settings')
def tap_done_button(context):
    context.app.launch_page.tap_done()


@when('Open main screen')
def main_screen_is_opened(context):
    context.app.main_page.tap_cancel()


@then('All default settings are active')
def verify_temperature(context):
    context.app.main_page.verify_temperature()
