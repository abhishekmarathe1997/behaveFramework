Feature: leads

  Background:
    Given user should be on login page
    When user enter the valid credentials
    Then user should navigated to home page

  Scenario: create lead
    When user click on new Lead
    When user fills the mandatory fields and click save
    Then lead should be created successfully

   @smoke
    Scenario: create lead
    When user click on new Lead
    When user fills the mandatory fields and click save
    Then lead should be created successfully

  @ss
    Scenario: create multiple leads
#    Given user should on home page
    When user create multiple leads and verified
    | firstname | lastname |
    |modi | bjp |
    |modi1|bjp1 |
    |modi2|bjp2 |
    Then user can logout