Feature: Apply Project And Notification

  Scenario: The freelancer apply to a project and the client receives the notification
    Given the user is on the login page
    When the freelancer user logs with a valid username and password
    And the user navigates to "Browse Projects" page
    And the user clicks the second project
    And the freelancer clicks the apply project button
    And the freelancer logs out
    And the user clicks the login button on the landpage
    And the client user logs in with a valid username and password
    And the client user navigates to "Notifications" page
    Then the freelancer apply project appears in the client page

  Scenario: The client rejects the apply to a project of the freelancer and the freelancer receives the notification
    Given the user is on the login page
    When the second client user logs in with a valid username and password
    And the client user navigates to "Notifications" page
    And the user client goes to readed notifications
    And the user client clicks the notification
    And the client rejects the freelancer
    And the client user in notifications logs out
    And the user clicks the login button on the landpage
    And the freelancer user logs with a valid username and password
    And the freelancer user navigates to "Notifications" page
    Then the client rejects apply project notification is show

  Scenario: The client accepts the apply to a project of the freelancer and the freelancer receives the notification
    Given the user is on the login page
    When the client user logs in with a valid username and password
    And the client user navigates to "Notifications" page
    And the user client clicks the notification
    And the client approves the freelancer
    And the client user in notifications logs out
    And the user clicks the login button on the landpage
    And the freelancer user logs with a valid username and password
    And the freelancer user navigates to "Notifications" page
    Then the client accepts apply project notification is show

  



  Scenario: The freelancer sends a proposal with the deliverables and the client receives the notification
    Given the user is on the login page
    When the freelancer user logs with a valid username and password
    And the freelancer user navigates to "Notifications" page
    And the user freelancer clicks the notification
    And the user freelancer fills the milestones
    And the freelancer logs out
    And the user clicks the login button on the landpage
    And the client user logs in with a valid username and password
    And the client user navigates to "Notifications" page
    Then the freelancer proposal with the deliverables is show

  Scenario: The client rejects the proposal with the deliverables and the freelancer receives the notification
    Given the user is on the login page
    When the client user logs in with a valid username and password
    And the client user navigates to "Notifications" page
    And the user client clicks the notification
    And the client rejects the deliverables of the freelancer
    And the client user in notifications logs out
    And the user clicks the login button on the landpage
    And the freelancer user logs with a valid username and password
    And the freelancer user navigates to "Notifications" page
    Then the client rejects the proposal is show

  Scenario: The freelancer resends the proposal with the deliverables and the client receives the notification
    Given the user is on the login page
    When the freelancer user logs with a valid username and password
    And the freelancer user navigates to "Notifications" page
    And the user freelancer clicks the notification
    And the freelancer fills another milestone
    And the freelancer logs out
    And the user clicks the login button on the landpage
    And the client user logs in with a valid username and password
    And the client user navigates to "Notifications" page
    Then the freelancer proposal with the deliverables is show

  Scenario: The client approves the proposal with the deliverables and the freelancer receives the notification
    Given the user is on the login page
    When the client user logs in with a valid username and password
    And the client user navigates to "Notifications" page
    And the user client clicks the notification
    And the client approves the deliverables of the freelancer
    And the client user in notifications logs out
    And the user clicks the login button on the landpage
    And the freelancer user logs with a valid username and password
    And the freelancer user navigates to "Notifications" page
    Then the client approves the proposal is show
    And the project is show in deliver work
  