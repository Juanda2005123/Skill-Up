from behave import given, when, then
from selenium import webdriver
from pages.loginPage import LoginPage
from pages.dashboardFreelancerPage import DashboardFreelancerPage
from pages.browseProjectPage import BrowseProjectPage
from pages.informationProjectPage import InformationProjectPage
from pages.freelancerProfilePage import FreelancerProfilePage
from pages.addDeliverablesProjectPage import AddDeliverablesProjectPage
from pages.addMilestoneDeliverablePage import AddMilestoneDeliverablePage
from pages.applyProjectFreelancerPage import ApplyProjectFreelancerPage
from pages.notificationPage import NotificationPage
from pages.browseOwnProjectsPage import BrowseOwnProjectsPage

@when('the freelancer logs out')
def stepUserLogsValidUsernameAndPassword(context):
    context.browseProjectPage = BrowseProjectPage(context.driver)
    context.browseProjectPage.logOut()

@when('the freelancer clicks the apply project button')
def stepUserLogsValidUsernameAndPassword(context):
    context.informationProjectPage = InformationProjectPage(context.driver)
    context.informationProjectPage.applyProject()

@when('the client approves the freelancer')
def stepUserLogsValidUsernameAndPassword(context):
    context.freelancerProfilePage = FreelancerProfilePage(context.driver)
    context.freelancerProfilePage.approveFreelancer()

@when('the client rejects the freelancer')
def stepUserLogsValidUsernameAndPassword(context):
    context.freelancerProfilePage = FreelancerProfilePage(context.driver)
    context.freelancerProfilePage.rejectFreelancer()

@when('the user freelancer fills the milestones')
def stepUserLogsValidUsernameAndPassword(context):
    context.addDeliverablesProjectPage = AddDeliverablesProjectPage(context.driver)
    context.addDeliverablesProjectPage.registerMilestone("Platform Setup and Core Features")
    context.addDeliverablesProjectPage.nav1Milestone()


    context.addMilestoneDeliverablePage = AddMilestoneDeliverablePage(context.driver)
    context.addMilestoneDeliverablePage.registerMilestoneSaveAddAnother("Backend and Database Setup",
                                                           "Develop the backend architecture using a scalable framework and set up a secure database for storing user, product, and transaction data. Include user authentication with role-based access.",
                                                           6)
    context.addMilestoneDeliverablePage = AddMilestoneDeliverablePage(context.driver)
    context.addMilestoneDeliverablePage.registerMilestoneSave("Product Management Module",
                                                              "Implement features to allow product listing with categories, detailed descriptions, and images. Admins should be able to add, update, and delete products easily.",
                                                              8)
    context.addDeliverablesProjectPage = AddDeliverablesProjectPage(context.driver)
    context.addDeliverablesProjectPage.registerMilestone("Shopping Cart and Payment Gateway")
    context.addDeliverablesProjectPage.nav2Milestone()


    context.addMilestoneDeliverablePage = AddMilestoneDeliverablePage(context.driver)
    context.addMilestoneDeliverablePage.registerMilestoneSaveAddAnother("Shopping Cart Integration",
                                                           "Create a shopping cart feature that supports adding, updating, and removing items. Include persistent storage so users' carts are saved even after they log out.",
                                                           10)
    context.addMilestoneDeliverablePage = AddMilestoneDeliverablePage(context.driver)
    context.addMilestoneDeliverablePage.registerMilestoneSave("Secure Payment Gateway",
                                                              "Integrate a secure payment system supporting credit cards, PayPal, and other payment methods. Ensure compliance with PCI DSS standards.",
                                                              10)

    context.addDeliverablesProjectPage = AddDeliverablesProjectPage(context.driver)
    context.addDeliverablesProjectPage.sendProposal()

@when('the freelancer fills another milestone')
def stepUserLogsValidUsernameAndPassword(context):
    context.addDeliverablesProjectPage = AddDeliverablesProjectPage(context.driver)
    context.addDeliverablesProjectPage.registerMilestone("User Experience and Testing")
    context.addDeliverablesProjectPage.nav1Milestone()


    context.addMilestoneDeliverablePage = AddMilestoneDeliverablePage(context.driver)
    context.addMilestoneDeliverablePage.registerMilestoneSave("Responsive Design Implementation",
                                                              "Ensure the platform is fully responsive across devices (mobile, tablet, desktop) with a focus on UX/UI. Conduct usability testing to refine the design.",
                                                              10)
    context.addDeliverablesProjectPage = AddDeliverablesProjectPage(context.driver)
    context.addDeliverablesProjectPage.sendProposal()

@when('the client rejects the deliverables of the freelancer')
def stepUserLogsValidUsernameAndPassword(context):
    context.applyProjectFreelancerPage = ApplyProjectFreelancerPage(context.driver)
    context.applyProjectFreelancerPage.reject()

@when('the client approves the deliverables of the freelancer')
def stepUserLogsValidUsernameAndPassword(context):
    context.applyProjectFreelancerPage = ApplyProjectFreelancerPage(context.driver)
    context.applyProjectFreelancerPage.approve()

@then('the client approves the deliverables of the freelancer')
def stepUserLogsValidUsernameAndPassword(context):
    context.applyProjectFreelancerPage = ApplyProjectFreelancerPage(context.driver)
    context.applyProjectFreelancerPage.approve()

@then('the project is show in deliver work')
def stepUserLogsValidUsernameAndPassword(context):
    context.notification = NotificationPage(context.driver)
    context.notification.deliverWork()
    context.browseOwnProjectsPage = BrowseOwnProjectsPage(context.driver)
    assert context.browseOwnProjectsPage.isTitleDisplayed("E-commerce Website Development")