from behave import given, when, then
from selenium import webdriver
from pages.loginPage import LoginPage
from pages.landpagePage import LandpagePage
from pages.dashboardClientPage import DashboardClientPage
from pages.clientProjectPage import ClientProjectPage
from pages.updateProjectPage import UpdateProjectPage
from pages.createProjectPage import CreateProjectPage




@when('the user fills in the project creation form with data')
def stepUserLogsValidUsernameAndPassword(context):
    context.createProjectPage = CreateProjectPage(context.driver)
    context.createProjectPage.createProject(
        "R", 
        "S", 
        "W", 
        4, 
        3)
    
@when('the new project should be displayed and the edit button is pressed')
def stepUserLogsValidUsernameAndPassword(context):
    context.clientProjectPage = ClientProjectPage(context.driver)
    context.clientProjectPage.updateProject("R")

@when('the project should be displayed and the edit button is pressed')
def stepUserLogsValidUsernameAndPassword(context):
    context.clientProjectPage = ClientProjectPage(context.driver)
    context.clientProjectPage.updateProject("Real-Time Chat Application")

@when('the project information is filled with valid data')
def stepUserLogsValidUsernameAndPassword(context):
    context.updateProjectPage = UpdateProjectPage(context.driver)
    context.updateProjectPage.updateProject(
        "eal-Time Chat Application", 
        "oftware Engineer - Full Stack", 
        "e need a skilled full-stack developer to build a real-time chat application for our internal team communication. The application should support group chats, file sharing, and real-time notifications. Experience with WebSocket technology, a modern frontend framework, and a scalable backend solution is essential.", 
        405, 
        3
    )
    
@when('the project information is filled with invalid data')
def stepUserLogsValidUsernameAndPassword(context):
    context.updateProjectPage = UpdateProjectPage(context.driver)
    context.updateProjectPage.updateProject(
        "Real-Time Chat Application", 
        "Software Engineer - Full Stack", 
        "We need a skilled full-stack developer to build a real-time chat application for our internal team communication. The application should support group chats, file sharing, and real-time notifications. Experience with WebSocket technology, a modern frontend framework, and a scalable backend solution is essential.", 
        -4000, 
        30
    )

@when('the project information is filled with empty data')
def stepUserLogsValidUsernameAndPassword(context):
    context.updateProjectPage = UpdateProjectPage(context.driver)
    context.updateProjectPage.updateProject(
        "", 
        "", 
        "We need a skilled full-stack developer to build a real-time chat application for our internal team communication. The application should support group chats, file sharing, and real-time notifications. Experience with WebSocket technology, a modern frontend framework, and a scalable backend solution is essential.", 
        4000, 
        30
    )

@then('the edit project should be displayed in the "My Projects" page')
def stepUserLogsValidUsernameAndPassword(context):
    context.clientProjectPage = ClientProjectPage(context.driver)
    assert context.clientProjectPage.projectDisplayed("Real-Time Chat Application")

@then('an error should appear of the edit project')
def stepUserLogsValidUsernameAndPassword(context):
    assert context.updateProjectPage.isBudgetError()

@then('the edit project cant be created')
def stepUserLogsValidUsernameAndPassword(context):
    assert context.updateProjectPage.isLastNameShow()
    