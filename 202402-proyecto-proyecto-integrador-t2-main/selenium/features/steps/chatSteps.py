from behave import given, when, then
from selenium import webdriver
from pages.loginPage import LoginPage
from pages.dashboardFreelancerPage import DashboardFreelancerPage
from pages.dashboardClientPage import DashboardClientPage
from pages.freelancerMessagePage import FreelancerMessagePage
from pages.clientMessagePage import ClientMessagePage
from pages.messageHomePage import MessageHomePage

@when('the freelancer navigates to "messages" page')
def stepUserLogsValidUsernameAndPassword(context):
    context.dashboardFreelancerPage = DashboardFreelancerPage(context.driver)
    context.dashboardFreelancerPage.navToMessages()

@when('the client navigates to "messages" page')
def stepUserLogsValidUsernameAndPassword(context):
    context.dashboardClientPage = DashboardClientPage(context.driver)
    context.dashboardClientPage.navToMessages()

@when('the user clicks the first message chat')
def stepUserLogsValidUsernameAndPassword(context):
    context.messageHomePage = MessageHomePage(context.driver)
    context.messageHomePage.latestChat()

@when('the freelancer sends a valid message')
def stepUserLogsValidUsernameAndPassword(context):
    context.freelancerMessagePage = FreelancerMessagePage(context.driver)
    context.freelancerMessagePage.sendMessage("Hi, just a quick update! I have completed the initial designs for the homepage")

@when('the client sends a valid message')
def stepUserLogsValidUsernameAndPassword(context):
    context.freelancerMessagePage = FreelancerMessagePage(context.driver)
    context.freelancerMessagePage.sendMessage("Hey, just checking in! Do you think the project will be ready for the first review by Friday?")

@when('the client message is show')
def stepUserLogsValidUsernameAndPassword(context):
    context.clientMessagePage = ClientMessagePage(context.driver)
    assert context.clientMessagePage.messageDisplayed("Hey, just checking in! Do you think the project will be ready for the first review by Friday?")

@when('the message is show')
def stepUserLogsValidUsernameAndPassword(context):
    context.freelancerMessagePage = FreelancerMessagePage(context.driver)
    assert context.freelancerMessagePage.messageDisplayed("Hi, just a quick update! I have completed the initial designs for the homepage")

@then('the freelancer message is show')
def stepUserLogsValidUsernameAndPassword(context):
    context.clientMessagePage = ClientMessagePage(context.driver)
    assert context.clientMessagePage.messageDisplayed("Hi, just a quick update! I have completed the initial designs for the homepage")

@then('the client message is show')
def stepUserLogsValidUsernameAndPassword(context):
    context.clientMessagePage = ClientMessagePage(context.driver)
    assert context.clientMessagePage.messageDisplayed("Hey, just checking in! Do you think the project will be ready for the first review by Friday?")

@when('the freelancer user logs out from messages')
def stepUserLogsValidUsernameAndPassword(context):
    context.freelancerMessagePage = FreelancerMessagePage(context.driver)
    context.freelancerMessagePage.logOut()

@when('the client user logs out from messages')
def stepUserLogsValidUsernameAndPassword(context):
    context.clientMessagePage = ClientMessagePage(context.driver)
    context.clientMessagePage.logOut()

@when('the freelancer sends an invalid message')
def stepUserLogsValidUsernameAndPassword(context):
    context.freelancerMessagePage = FreelancerMessagePage(context.driver)
    context.freelancerMessagePage.sendMessage("")

@then('the message is not show')
def stepUserLogsValidUsernameAndPassword(context):
    context.freelancerMessagePage = FreelancerMessagePage(context.driver)
    assert not context.freelancerMessagePage.messageDisplayed("")