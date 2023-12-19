*** Settings ***
Documentation     Test cases for project module
...               Run using "python web2py.py --no-banner -M -S eden  -R applications/eden/tests/edentest_runner.py -A project_project"

Resource          ../../resources/main.robot

*** Variables ***
${PROJECT URL}      ${BASEURL}/project/project

*** Test Cases ***

Test Project List
    Login To Eden If Not Logged In  ${VALID USER}  ${VALID PASSWORD}
    Go To    ${PROJECT URL}
    Table Should Contain    datatable   Water and Sanitation

Updating Project Should Be Successful

    Login To Eden If Not Logged In  ${VALID USER}  ${VALID PASSWORD}
    Go To  ${PROJECT URL}

    # Open a record
    Click Element  xpath=//*[@id="datatable"]/tbody/tr[1]/td[1]/a[1]
    Wait Until Page Contains Element  project_project_name

    # Change the project's name
    Input Text  project_project_comments  Test Comment
    Click Element  xpath=//input[@type="submit" and @value="Save"]

    #Assertion
    Should Show Confirmation
