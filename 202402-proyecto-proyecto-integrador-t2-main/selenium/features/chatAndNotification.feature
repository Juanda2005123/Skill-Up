Feature: Chat And Notification

  Scenario: Chat freelancer 
    Given the user is on the login page
    When the freelancer user logs with a valid username and password
    And the freelancer navigates to "messages" page
    And the user clicks the first message chat
    And the freelancer sends a valid message
    And the message is show
    And the freelancer user logs out from messages
    And the user clicks the login button on the landpage
    And the second client user logs in with a valid username and password
    And the client user navigates to "Notifications" page
    And the user client clicks the notification
    Then the freelancer message is show
    
  Scenario: Chat client
    Given the user is on the login page
    When the second client user logs in with a valid username and password
    And the client navigates to "messages" page
    And the user clicks the first message chat
    And the client sends a valid message
    And the client message is show
    And the client user logs out from messages
    And the user clicks the login button on the landpage
    And the freelancer user logs with a valid username and password
    And the freelancer user navigates to "Notifications" page
    And the user freelancer clicks the notification
    Then the client message is show

  Scenario: Empty Message Chat freelancer 
    Given the user is on the login page
    When the freelancer user logs with a valid username and password
    And the freelancer navigates to "messages" page
    And the user clicks the first message chat
    And the freelancer sends an invalid message
    Then the message is not show
    
  
