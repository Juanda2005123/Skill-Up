from behave import given, when, then
from selenium import webdriver
from pages.loginPage import LoginPage
from pages.landpagePage import LandpagePage
from pages.dashboardClientPage import DashboardClientPage
from pages.dashboardFreelancerPage import DashboardFreelancerPage
from pages.clientProjectPage import ClientProjectPage
from pages.updateProjectPage import UpdateProjectPage
from pages.createProjectPage import CreateProjectPage
from pages.notificationPage import NotificationPage

@when('the client user in notifications logs out')
def stepUserLogsValidUsernameAndPassword(context):
    context.notification = NotificationPage(context.driver)
    context.notification.logOutClient()

@when('the freelancer user in notifications logs out')
def stepUserLogsValidUsernameAndPassword(context):
    context.notification = NotificationPage(context.driver)
    context.notification.logOutFreelancer()

@when('the freelancer user navigates to "Notifications" page')
def stepUserClicksRegisterClientButton(context):
    context.dashboardFreelancer = DashboardFreelancerPage(context.driver)
    context.dashboardFreelancer.navToNotifications()

@when('the client user navigates to "Notifications" page')
def stepUserClicksRegisterClientButton(context):
    context.dashboardClient = DashboardClientPage(context.driver)
    context.dashboardClient.navToNotifications()

@when('the user client clicks the notification')
def stepUserClicksRegisterClientButton(context):
    context.notification = NotificationPage(context.driver)
    context.notification.clickNotificationLink()

@when('the user freelancer clicks the notification')
def stepUserClicksRegisterClientButton(context):
    context.notification = NotificationPage(context.driver)
    context.notification.clickNotificationLink()

@then('the client register notification is show')
def stepUserClicksRegisterClientButton(context):
    context.notification = NotificationPage(context.driver)
    assert context.notification.isNotificationDisplayed("A Client account has been created for Juan Perez.")

@then('the freelancer register notification is show')
def stepUserClicksRegisterClientButton(context):
    context.notification = NotificationPage(context.driver)
    assert context.notification.isNotificationDisplayed("A Freelancer account has been created for Juan David Quintero.")

@then('the create project notification is show')
def stepUserClicksRegisterClientButton(context):
    context.notification = NotificationPage(context.driver)
    assert context.notification.isNotificationDisplayed('created the project "E-commerce Website Development"')

@then('the client profile notification is show')
def stepUserClicksRegisterClientButton(context):
    context.notification = NotificationPage(context.driver)
    assert context.notification.isNotificationDisplayed('Your profile has been updated, Maria Lopez.')

@then('the create freelancer profile notification is show')
def stepUserClicksRegisterClientButton(context):
    context.notification = NotificationPage(context.driver)
    assert context.notification.isNotificationDisplayed('Your profile has been updated, Juan David Quintero.')

@then('the freelancer apply project appears in the client page')
def stepUserLogsValidUsernameAndPassword(context):
    context.notification = NotificationPage(context.driver)
    assert context.notification.isNotificationDisplayed('The freelancer Juan David Quintero has requested to work on your project "E-commerce Website Development".')

@then('the client accepts apply project notification is show')
def stepUserLogsValidUsernameAndPassword(context):
    context.notification = NotificationPage(context.driver)
    assert context.notification.isNotificationDisplayed('The client Juan Perez has accepted your proposal for the project "E-commerce Website Development". You can now start creating deliverables to submit the proposal.')

@then('the client rejects apply project notification is show')
def stepUserLogsValidUsernameAndPassword(context):
    context.notification = NotificationPage(context.driver)
    assert context.notification.isNotificationDisplayed('The client Maria Lopez has rejected your proposal for the project "Real-Time Chat Application". You can send another proposal in 7 days.')

@then('the freelancer proposal with the deliverables is show')
def stepUserLogsValidUsernameAndPassword(context):
    context.notification = NotificationPage(context.driver)
    assert context.notification.isNotificationDisplayed('The freelancer Juan David Quintero has submitted their proposal with the deliverables for your project "E-commerce Website Development".')

@then('the client rejects the proposal is show')
def stepUserLogsValidUsernameAndPassword(context):
    context.notification = NotificationPage(context.driver)
    assert context.notification.isNotificationDisplayed('Your submitted deliverables for the project "E-commerce Website Development" have been rejected. You can resubmit your proposal by editing the deliverables.')

@then('the client approves the proposal is show')
def stepUserLogsValidUsernameAndPassword(context):
    context.notification = NotificationPage(context.driver)
    assert context.notification.isNotificationDisplayed('Your submitted deliverables for the project "E-commerce Website Development" have been accepted. You can check your projects to start working.')

@when('the user client goes to readed notifications')
def stepUserLogsValidUsernameAndPassword(context):
    context.notification = NotificationPage(context.driver)
    context.notification.readed()