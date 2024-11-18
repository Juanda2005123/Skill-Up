Feature: Browse Project Feature

  Scenario: Browse first project
    Given the user is on the login page
    When the freelancer user logs with a valid username and password
    And the user navigates to "Browse Projects" page
    And the user clicks the first project
    And the project information is show
    Then the freelancer clicks the apply project button

  Scenario: Browse two projects
    Given the user is on the login page
    When the freelancer user logs with a valid username and password
    And the user navigates to "Browse Projects" page
    And the user clicks the first project
    And the first project information is show
    And the user goes back to "Browse Projects" page
    And the user clicks the second project
    Then the second project information is show