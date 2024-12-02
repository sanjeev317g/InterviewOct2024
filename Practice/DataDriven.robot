*** Settings ***
*** Variables ***
*** Test Cases ***
Testing DataDriven in TestRobot    
    [Template]    keywordDD
    10    20
    30    40   
    50    60

*** Keywords ***
keywordDD
    [Arguments]    ${a}    ${b}
    Log     ${a} 
    Log    ${b}
    