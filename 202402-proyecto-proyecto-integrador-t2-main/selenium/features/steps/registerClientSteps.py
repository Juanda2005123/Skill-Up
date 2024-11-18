from behave import given, when, then
from selenium import webdriver
from pages.registerClientPage import RegisterClientPage
from pages import *
from pages.loginPage import LoginPage
from pages.landpagePage import LandpagePage

@when('the user clicks the register button on the landpage')
def stepUserClicksRegisterButton(context):
    context.landpagePage = LandpagePage(context.driver)
    context.landpagePage.register()

@when('the user clicks the register client button on the landpage')
def stepUserClicksRegisterClientButton(context):
    context.landpagePage.registerClient()

@when('the user register a client with valid credentials')
def stepUserRegistersClientWithValidCredentials(context):
    context.registerClientPage = RegisterClientPage(context.driver)
    context.registerClientPage.register(
        first_name='Juan', 
        last_name='Perez', 
        username='juanperez123', 
        email='juanperez@example.com', 
        password1='TestPassword123', 
        password2='TestPassword123', 
        phone_number='987654321', 
        tax_id='9876543210', 
        company_name='TechNova Solutions', 
        type_of_company='Retail', 
        address='Calle Falsa 123, Ciudad, País'
    )
    
@when('the user register a second client with valid credentials')
def stepUserClicksRegisterClientButton(context):
    context.registerClientPage = RegisterClientPage(context.driver)
    context.registerClientPage.register(
        first_name='Maria', 
        last_name='Lopez', 
        username='mariaLopez1', 
        email='mariaLopez@example.com', 
        password1='TestPassword123', 
        password2='TestPassword123', 
        phone_number='123456789', 
        tax_id='12345678901', 
        company_name='GreenWorks Industries', 
        type_of_company='Retail', 
        address='Calle Falsa 123, Ciudad, País'
    )

@when('the user attempts to register a client with an invalid phone number format')
def stepUserClicksRegisterClientButton(context):
    context.registerClientPage = RegisterClientPage(context.driver)
    context.registerClientPage.register(
        first_name='Maria', 
        last_name='Lopez', 
        username='mariaLopesz1', 
        email='mariaLopez@example.com', 
        password1='TestPassword123', 
        password2='TestPassword123', 
        phone_number='123juanD', 
        tax_id='12345678901', 
        company_name='Empresa Test', 
        type_of_company='Retail', 
        address='Calle Falsa 123, Ciudad, País'
    )

@when('the user attempts to register a client with an invalid tax ID format')
def stepUserClicksRegisterClientButton(context):
    context.registerClientPage = RegisterClientPage(context.driver)
    context.registerClientPage.register(
        first_name='Maria', 
        last_name='Lopez', 
        username='mariaLopesz1', 
        email='mariaLopez@example.com', 
        password1='TestPassword123', 
        password2='TestPassword123', 
        phone_number='12331525', 
        tax_id='juans14kas', 
        company_name='Empresa Test', 
        type_of_company='Retail', 
        address='Calle Falsa 123, Ciudad, País'
    )

@when('the user attempts to register a client with passwords that do not match')
def stepUserClicksRegisterClientButton(context):
    context.registerClientPage = RegisterClientPage(context.driver)
    context.registerClientPage.register(
        first_name='Maria', 
        last_name='Lopez', 
        username='mariaLopesz1', 
        email='mariaLopez@example.com', 
        password1='TestPassword123', 
        password2='TestPassword12345', 
        phone_number='123131525', 
        tax_id='1234556789', 
        company_name='Empresa Test', 
        type_of_company='Retail', 
        address='Calle Falsa 123, Ciudad, País'
    )

@when('the user attempts to register a client with some fields empty')
def stepUserClicksRegisterClientButton(context):
    context.registerClientPage = RegisterClientPage(context.driver)
    context.registerClientPage.register(
        first_name='Maria', 
        last_name='', 
        username='kiafdawloa12', 
        email='kiadfawf@kia.com', 
        password1='TestPassword123', 
        password2='TestPassword123', 
        phone_number='167241241', 
        tax_id='12345678901', 
        company_name='Empresa Test', 
        type_of_company='Retail', 
        address='Calle Falsa 123, Ciudad, País'
    )

@when('the user tries to register a client with invalid email format')
def stepUserClicksRegisterClientButton(context):
    context.registerClientPage = RegisterClientPage(context.driver)
    context.registerClientPage.register(
        first_name='Maria', 
        last_name='Lopez', 
        username='mariaLossspesz1', 
        email='mariaLopez@s', 
        password1='TestPassword123', 
        password2='TestPassword123', 
        phone_number='123456789', 
        tax_id='12345678901', 
        company_name='Empresa Test', 
        type_of_company='Retail', 
        address='Calle Falsa 123, Ciudad, País'
    )

@when('error is show of already created user')
def stepUserClicksRegisterClientButton(context):
    context.registerClientPage.errorMessageDisplayed()
    
@when('the user client go backs to the landpage')
def stepUserClicksRegisterClientButton(context):
    context.registerClientPage.landpageRedirect()

@then('the user must be redirected to the login page')
def stepUserIsRedirectedToLoginPage(context):
    context.loginPage = LoginPage(context.driver)
    assert context.loginPage.isLoginDisplayed()

@then('the user should see an error message indicating the phone number is invalid')
def stepUserClicksRegisterClientButton(context):
    context.registerClientPage.errorMessagePhoneNumberDisplayed()

@then('the user should see an error message indicating the tax ID is invalid')
def stepUserClicksRegisterClientButton(context):
    context.registerClientPage.errorMessageTaxIdDisplayed()

@then('the user should see an error message indicating the passwords do not match')
def stepUserClicksRegisterClientButton(context):
    context.registerClientPage.errorMessagePasswordisplayed()

@then('the user should see an error message indicating that all required fields must be filled')
def stepUserClicksRegisterClientButton(context):
    context.registerClientPage.errorMessageEmptyDisplayed()

@then('an error message is displayed indicating "Invalid email format"')
def stepUserClicksRegisterClientButton(context):
    context.registerClientPage.errorMessageEmailDisplayed()