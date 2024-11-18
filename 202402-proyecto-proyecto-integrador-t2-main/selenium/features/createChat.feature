Feature: Create Chat Feature

  Scenario: Client Create Chat Freelancer List
    Given the user is on the login page
    When the second client user logs in with a valid username and password
    And the client user navigates to "Notifications" page
    And the user client clicks the notification
    And the client chats with the freelancer
    Then the chat with the freelancer is created

  Scenario: Freelancer Create Chat Freelancer Request
    Given the user is on the login page
    When the freelancer user logs with a valid username and password
    And the user navigates to "Browse Projects" page
    And the user clicks the second project
    And the user clicks the create chat button
    Then the chat with the client is created