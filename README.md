# QA Fundamental Project 1

## Contents
* [Introduction](#introduction)
* [Architecture](#architecture)
    * [Evolution of Project Design](#evolution-of-project-design)
    * [Kanban Board](#kanban-board)
    * [Risk Assessment](#risk-assessment)
* [Developement and Deployment](#developement-and-deployment)
    * [Test Reports](#test-report)
    * [Continuous Integration](#continuous-integration)

## Introduction

The project objective was as follows:
> To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.

It was also mentioned that there should be a relational database containing a minimum of two tables with a relationship between them. 

For this project I decided to create a webapp that stores and displays a users' personal records for a number of exercises that one performs in the gym.

## Architecture

### Evolution of Project Design 
The scope of the project was reviewed and narrowed several times over the projects' duration. 

My original design for the entity relation diagram (ERD) for my database:

![OG_ERD](./images/OG_ERD.png)

Originally I had intended the app to feature the option for a user to add exercises to the database. I decided against this due to the time constraints involved in implementing such a feature and so added the exercises into the exercise table as static data.

Another feature I originally wanted to incorporate was a users table which let multiple users store, view, update and delete their gym records. This idea was axed for similar reasons, namely time concerns. 

The new ERD for my project ended up looking like this:

![new_ERD](./images/new_ERD.png)

### Kanban Board

I chose [Trello](https://trello.com) to create my Kanban board and hence to plan my project due to it being free and that I was already familiar with the app.

A screenshot of my Trello board:

![trello_board](./images/trello_board.png)

My full Trello board can be accessed [here](https://trello.com/b/7kMzASNH/qaproject-1).

### Risk Assessment 

Screenshot of my risk assessment:

![risk_asmnt](./images/risk_amnt.png)

Full risk assessment available [here](https://onedrive.live.com/edit.aspx?resid=2999F3BD7781D9A6!127&ithint=file%2cxlsx&wdOrigin=OFFICECOM-WEB.START.MRU).

## Developement and Deployment

### Test Report

A test report for my application can be found below:

![testreport](./images/test_report.png)

It can be seen that I achieved a total of 84% test coverage. The only area found to be lacking was the routes.py file which only had 71% coverage. Further analyis yielded that the lines that needed testing were:
- 16 
- 29-32 
- 44-46
- 58-61

These lines were omitted due to time constraints and my relative inexperience writing unit tests for such code.

A total of 10 tests were carried out using unit and integration testing. An overall coverage of 84% was deeemed acceptable. 

### Continuous Integration

The app was deployed through Jenkins with a GitHub webhook and the following shell commands:
> python3 -m venv venv  
>. ./venv/bin/activate  
>export URI_project_db  
>export S_key  
>pip3 install -r requirements.txt  
>python3 app.py

Where the URI_project_db and S_key are the secret database credentials stored on Jenkins. 