@test123
Feature: login

Background:
  Given user should be on login page

  @valid @smoke @regression
Scenario: valid login
When user enter the valid credentials
Then user should navigated to home page

@invalid @sanity
Scenario: Invalid login
When user enter the invalid credentials
Then user can see the error message

@datadriven  @abc
Scenario Outline: Invalid login data driven
When user enter the invalid credentials username as <userid> and password as <password>
Then user can see the error message
Examples:
  |userid | password|
  |admin1 | pwd1    |
  |admin2 | pwd2    |
  |admin3 | pwd3    |
