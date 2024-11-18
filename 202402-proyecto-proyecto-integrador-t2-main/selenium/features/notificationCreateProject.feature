Feature: Notification Create project

  Scenario: Notification create project
    Given the user is on the login page
    When the client user logs in with a valid username and password
    And the client user navigates to "Notifications" page
    Then the create project notification is show