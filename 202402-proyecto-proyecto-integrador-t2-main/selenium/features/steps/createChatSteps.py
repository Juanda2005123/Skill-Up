from behave import given, when, then
from selenium import webdriver
from pages.loginPage import LoginPage
from pages.dashboardFreelancerPage import DashboardFreelancerPage
from pages.browseProjectPage import BrowseProjectPage
from pages.informationProjectPage import InformationProjectPage
from pages.freelancerMessagePage import FreelancerMessagePage
from pages.freelancerProfilePage import FreelancerProfilePage
from pages.clientMessagePage import ClientMessagePage


@when('the user clicks the create chat button')
def stepUserLogsValidUsernameAndPassword(context):
    context.informationProjectPage = InformationProjectPage(context.driver)
    context.informationProjectPage.chat()

@then('the chat with the freelancer is created')
def stepUserLogsValidUsernameAndPassword(context):
    context.freelancerMessagePage = FreelancerMessagePage(context.driver)
    assert context.freelancerMessagePage.isTitleDisplayed("Juan David Quintero")

@when('the client chats with the freelancer')
def stepUserLogsValidUsernameAndPassword(context):
    context.freelancerProfilePage = FreelancerProfilePage(context.driver)
    context.freelancerProfilePage.chat()

@then('the chat with the client is created')
def stepUserLogsValidUsernameAndPassword(context):
    context.clientMessagePage = ClientMessagePage(context.driver)
    assert context.clientMessagePage.isTitleDisplayed("Juan Perez")