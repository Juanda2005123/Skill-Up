Feature: Project Update Feature

  Scenario: Successful project creation with valid data and update
    Given the user is on the login page
    When the second client user logs in with a valid username and password
    And the user navigates to "My Projects" page
    And the user clicks the "Create Project" button
    And the user fills in the project creation form with data
    And the new project should be displayed and the edit button is pressed
    And the project information is filled with valid data
    Then the edit project should be displayed in the "My Projects" page

  Scenario: Unsuccessful project update with invalid data
    Given the user is on the login page
    When the second client user logs in with a valid username and password
    And the user navigates to "My Projects" page
    And the project should be displayed and the edit button is pressed
    And the project information is filled with invalid data
    Then an error should appear of the edit project
