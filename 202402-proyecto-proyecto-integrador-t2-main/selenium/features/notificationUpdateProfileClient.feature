Feature: Notification Update Profile Client

  Scenario: Notification update profile client
    Given the user is on the login page
    When the second client user logs in with a valid username and password
    And the client user navigates to "View Profile" page
    And the second client fills the company description with valid data
    And the client goes to the "notifications" page
    Then the client profile notification is show