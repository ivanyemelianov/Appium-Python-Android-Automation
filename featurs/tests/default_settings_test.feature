
Feature: Testing default settings

  Scenario: User can set the temperature unit to celsius
    Given Proceed with default settings
    When Open main screen
    Then Temperature is set to celsius

  Scenario: User can set the 12 hour time format
    Given Proceed with default settings
    When Open main screen
    Then Time elements have am or pm

  Scenario: User can set wind speed to km/h
    Given Proceed with default settings
    When Open main screen
    Then Wind speed element has km/h