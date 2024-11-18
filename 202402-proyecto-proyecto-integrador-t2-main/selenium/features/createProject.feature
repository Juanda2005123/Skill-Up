Feature: Project Creation Feature

  Scenario: Successful project creation with valid data
    Given the user is on the login page
    When the client user logs in with a valid username and password
    And the user navigates to "My Projects" page
    And the user clicks the "Create Project" button
    And the user fills in the project creation form with valid data
    Then the new project should be displayed in the "My Projects" page

  Scenario: Unsuccessful project creation with invalid data
    Given the user is on the login page
    When the client user logs in with a valid username and password
    And the user navigates to "My Projects" page
    And the user clicks the "Create Project" button
    And the user fills in the project creation form with invalid data
    Then an error should appear

  Scenario: Unsuccessful project creation with empty data
    Given the user is on the login page
    When the client user logs in with a valid username and password
    And the user navigates to "My Projects" page
    And the user clicks the "Create Project" button
    And the user fills in the project creation form with empty data
    Then the project cant be created
  
