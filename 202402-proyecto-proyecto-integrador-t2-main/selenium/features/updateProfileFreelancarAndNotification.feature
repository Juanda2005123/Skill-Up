Feature: Update Notification Freelancer Profile

  Scenario: Update profile Freelancer
    Given the user is on the login page
    When the freelancer user logs with a valid username and password
    And the freelancer user navigates to "Customize profile" page
    And the freelancer fills some profile fields with valid data
    Then the freelancer profile is changed

  Scenario: Notification Update Profile Freelancer
    Given the user is on the login page
    When the freelancer user logs with a valid username and password
    And the freelancer user navigates to "Notifications" page
    Then the create freelancer profile notification is show