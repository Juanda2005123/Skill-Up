from behave import given, when, then
from selenium import webdriver
from pages.registerFreelancerPage import RegisterFreelancerPage
from pages import *
from pages.loginPage import LoginPage
from pages.dashboardClientPage import DashboardClientPage
from pages.updateProfileClientPage import UpdateProfileClientPage


@when('the client user navigates to "View Profile" page')
def stepUserClicksRegisterClientButton(context):
    context.dashboardClientPage = DashboardClientPage(context.driver)
    context.dashboardClientPage.navToProfile()

@when('the client fills the company description with valid data')
def stepUserClicksRegisterClientButton(context):
    context.UpdateProfileClient = UpdateProfileClientPage(context.driver)
    context.UpdateProfileClient.updateCompanyDescription("TechNova Solutions develops custom software and artificial intelligence solutions for businesses. They offer services such as mobile applications, web platforms, and machine learning models. Their clients include startups, banks, and digital health institutions.")

@when('the second client fills the company description with valid data')
def stepUserClicksRegisterClientButton(context):
    context.UpdateProfileClient = UpdateProfileClientPage(context.driver)
    context.UpdateProfileClient.updateCompanyDescription("EcoBuild Innovations provides sustainable construction materials and solutions for green building projects. They focus on energy-efficient designs and eco-friendly technologies. Their mission is to reduce environmental impact while maintaining high-quality standards in construction.")

@then('the client company description is changed')
def stepUserClicksRegisterClientButton(context):
    context.UpdateProfileClient = UpdateProfileClientPage(context.driver)
    assert context.UpdateProfileClient.isDisplayed()

@when('the client goes to the "notifications" page')
def stepUserClicksRegisterClientButton(context):
    context.UpdateProfileClient = UpdateProfileClientPage(context.driver)
    context.UpdateProfileClient.navToNotification()