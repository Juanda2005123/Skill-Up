Feature: Notification Register

  Scenario: Notification register client
    Given the user is on the login page
    When the client user logs in with a valid username and password
    And the client user navigates to "Notifications" page
    Then the client register notification is show

  Scenario: Notification register client
    Given the user is on the login page
    When the freelancer user logs with a valid username and password
    And the freelancer user navigates to "Notifications" page
    Then the freelancer register notification is show