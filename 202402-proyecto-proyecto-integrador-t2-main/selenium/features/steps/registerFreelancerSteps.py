from behave import given, when, then
from selenium import webdriver
from pages.registerFreelancerPage import RegisterFreelancerPage
from pages import *
from pages.loginPage import LoginPage

@when('the user clicks the register freelancer button on the landpage')
def stepUserClicksRegisterClientButton(context):
    context.landpagePage.registerFreelancer()

@when('the user register a freelancer with valid credentials')
def stepUserRegistersFreelancerWithValidCredentials(context):
    context.registerFreelancerPage = RegisterFreelancerPage(context.driver)
    context.registerFreelancerPage.register(
        first_name='Juan David',
        last_name='Quintero',
        username='juanQuintero',
        email='juanQuintero@example.com',
        password1='TestPassword123',
        password2='TestPassword123',
        phone_number=987654321,
        identification=9876543210,  
    )

@when('the user attempts to register a freelancer with an invalid phone number format')
def stepUserClicksRegisterClientButton(context):
    context.registerFreelancerPage = RegisterFreelancerPage(context.driver)
    context.registerFreelancerPage.register(
        first_name='Juan David',
        last_name='Quintero',
        username='juanQuinsteros',
        email='juanperez@example.com',
        password1='TestPassword123',
        password2='TestPassword123',
        phone_number='9876543ss21',
        identification=9876543210,  
    )

@when('the user attempts to register a freelancer with an invalid identification format')
def stepUserClicksRegisterClientButton(context):
    context.registerFreelancerPage = RegisterFreelancerPage(context.driver)
    context.registerFreelancerPage.register(
        first_name='Juan David',
        last_name='Quintero',
        username='juanQuinteros',
        email='juanperez@example.com',
        password1='TestPassword123',
        password2='TestPassword123',
        phone_number=987654321,
        identification='98765ss43210',  
    )

@when('the user attempts to register a freelancer with passwords that do not match')
def stepUserClicksRegisterClientButton(context):
    context.registerFreelancerPage = RegisterFreelancerPage(context.driver)
    context.registerFreelancerPage.register(
        first_name='Juan David',
        last_name='Quintero',
        username='juanQuinteros',
        email='juanperez@example.com',
        password1='ssTestPasswosrd123',
        password2='TestPassword123',
        phone_number=987654321,
        identification=9876543210,  
    )

@when('the user attempts to register a freelancer with some fields empty')
def stepUserClicksRegisterClientButton(context):
    context.registerFreelancerPage = RegisterFreelancerPage(context.driver)
    context.registerFreelancerPage.register(
        first_name='Juan David',
        last_name='',
        username='juanQuinteros',
        email='juanperez@example.com',
        password1='TestPassword123',
        password2='TestPassword123',
        phone_number=987654321,
        identification=9876543210,  
    )

@when('the user tries to register a freelancer with invalid email format')
def stepUserClicksRegisterClientButton(context):
    context.registerFreelancerPage = RegisterFreelancerPage(context.driver)
    context.registerFreelancerPage.register(
        first_name='Juan David',
        last_name='Quintero',
        username='juanQuinsteros',
        email='juanperez@exs',
        password1='TestPassword123',
        password2='TestPassword12s3',
        phone_number=987654321,
        identification=9876543210,  
    )
    
@when('the user freelancer go backs to the landpage')
def stepUserClicksRegisterClientButton(context):
    context.registerFreelancerPage.landpageRedirect()

@then('the user should see an error message')
def stepUserClicksRegisterClientButton(context):
    context.registerFreelancerPage.errorMessageDisplayed()

@when('the user should see an error message')
def stepUserClicksRegisterClientButton(context):
    context.registerFreelancerPage.errorMessageDisplayed()

@then('the user should see an error message with the empty field')
def stepUserClicksRegisterClientButton(context):
    context.registerFreelancerPage.errorEmptyField()