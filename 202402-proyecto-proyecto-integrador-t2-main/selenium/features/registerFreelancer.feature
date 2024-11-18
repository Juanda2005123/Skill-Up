Feature: Register Client Feature

  Scenario: Successful Register with valid credentials 
    Given the user is on the landpage
    When the user clicks the register button on the landpage
    And the user clicks the register freelancer button on the landpage
    And the user register a freelancer with valid credentials
    Then the user must be redirected to the login page

  Scenario: Successful Register with valid credentials but already created user and login 
    Given the user is on the landpage
    When the user clicks the register button on the landpage
    And the user clicks the register freelancer button on the landpage
    And the user register a freelancer with valid credentials
    And the user should see an error message
    And the user freelancer go backs to the landpage
    And the user clicks the login button on the landpage
    And the freelancer user logs with a valid username and password
    Then the freelancer user should be redirected to the dashboard page
  


  Scenario: Register with invalid phone number format
    Given the user is on the landpage
    When the user clicks the register button on the landpage
    And the user clicks the register freelancer button on the landpage
    And the user attempts to register a freelancer with an invalid phone number format
    Then the user should see an error message

  Scenario: Register with invalid identification format
    Given the user is on the landpage
    When the user clicks the register button on the landpage
    And the user clicks the register freelancer button on the landpage
    And the user attempts to register a freelancer with an invalid identification format
    Then the user should see an error message

  Scenario: Register with non-matching passwords
    Given the user is on the landpage
    When the user clicks the register button on the landpage
    And the user clicks the register freelancer button on the landpage
    And the user attempts to register a freelancer with passwords that do not match
    Then the user should see an error message

  Scenario: Register with empty fields
    Given the user is on the landpage
    When the user clicks the register button on the landpage
    And the user clicks the register freelancer button on the landpage
    And the user attempts to register a freelancer with some fields empty
    Then the user should see an error message with the empty field

  Scenario: Successful Register with valid credentials but email is invalid
    Given the user is on the landpage
    When the user clicks the register button on the landpage
    And the user clicks the register freelancer button on the landpage
    And the user tries to register a freelancer with invalid email format
    Then the user should see an error message
