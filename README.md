Testing Framework : Lean_Tech

Github link with the source code :

Documentation explaining the test suite setup and execution process :

    1) Task : You are tasked with developing an automated test suite for Sauce labs demo website.
     Your automation test suite should cover the customer flow of selecting 3 random items and completing the checkout flow.

    2) Test items : https://www.saucedemo.com

    3) Tools and tech used :
        Language         : Python
        Framework        : Pytest
        Library          : Selenium Library
        Reporting        : Pytest html
        Approach / Model : POM (Page object Model)

    4) Framwork Structure :
        base package      -> base_driver.py -> Contains common modules/libraries
        pages package     -> It contains elements and data of all the 5 pages involved during automation
                           All pages inherit base package
                           methods of these pages are then utilised in test case
        reports           -> Reports in html format
        testcases package -> Actual testcase flow is written in this.
                           test_complete_flow.py contains testcase of the flow
                           conftst.py file contains fixtures where setup and teardown is defined on class level
        Testdata          -> Currently test data is empty, but it will have testing data against which test cases needs to be validated
        Readme file       -> Details of framework are mentioned

    5) How to execute : run below command from CLI , report will be generated and stored in reports folder.
                        pytest -s --capture=sys --html=reports/report.html --self-contained-html

Any additional resources or dependencies required to run the tests :
    Below installations are needed :
    1) Python -> SeleniumLibrary, pytest, pytest-html


