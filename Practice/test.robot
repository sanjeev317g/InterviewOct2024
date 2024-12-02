*** Settings ***
Library    customLibrary.py
Library    RPA.Robocorp.Storage


*** Variables ***

*** Test Cases ***
Calling CustomLibrary
    ${v}=    TestRobot     10
    Should Be Equal As Numbers    10    ${v}