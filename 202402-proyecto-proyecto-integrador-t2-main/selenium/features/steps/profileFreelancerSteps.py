from behave import given, when, then
from selenium import webdriver
from pages.dashboardFreelancerPage import DashboardFreelancerPage
from pages.customizeProfilePage import CustomizeProfilePage

@when('the freelancer user navigates to "Customize profile" page')
def stepUserClicksRegisterClientButton(context):
    context.dashboardFreelancer = DashboardFreelancerPage(context.driver)
    context.dashboardFreelancer.navToProfile()

@when('the freelancer fills some profile fields with valid data')
def stepUserClicksRegisterClientButton(context):
    context.customizeProfilePage = CustomizeProfilePage(context.driver)
    context.customizeProfilePage.updateFreelancerProfile("Passionate software developer with 5+ years of experience in web and mobile app development. Adept at building scalable, secure, and user-friendly applications for diverse industries. Dedicated to delivering high-quality code and exceeding client expectations.",
                                                         "https://co.linkedin.com/",
                                                         "https://github.com/Juanda2005123",
                                                         "https://www.instagram.com/",
                                                         "django, python, javascript, react, node.js, postgresql, aws, google cloud, docker, kubernetes, data visualization, selenium")
    
@then('the freelancer profile is changed')
def stepUserClicksRegisterClientButton(context):
    context.customizeProfilePage = CustomizeProfilePage(context.driver)
    context.customizeProfilePage.isDisplayed()

