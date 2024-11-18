Feature: Update Profile Client

  Scenario: Update profile client
    Given the user is on the login page
    When the client user logs in with a valid username and password
    And the client user navigates to "View Profile" page
    And the client fills the company description with valid data
    Then the client company description is changed