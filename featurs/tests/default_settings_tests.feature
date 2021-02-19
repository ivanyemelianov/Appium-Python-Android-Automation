
Feature: Testing default settings

  Scenario: User can proceed with default settings and the default settings are active
    Given Proceed with default settings
    When Open main screen
    Then All default settings are active
