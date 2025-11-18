from pages.HomePage import HomePage

email = 'abdulurrehman@abc.com'
name = 'Abdul-ur-Rehman'
password = 'abc123'




def test_register_user(setup):
    driver = setup

    home_page = HomePage(driver)

    assert home_page.homePage_verification() == 'AutomationExercise'

    login_page = home_page.click_login_button()
    loginPage_verificcation_text = login_page.login_page_verification()

    assert loginPage_verificcation_text == 'New User Signup!'

    accountPage = login_page.account_signup(name, email)


    accountPage_verification_text = accountPage.accountPage_verification()
    assert accountPage_verification_text == "ENTER ACCOUNT INFORMATION"

    account_created = accountPage.account_detials_form_filling(password)
    assert account_created == "ACCOUNT CREATED!"
    accountPage.continue_to_HomePage()

    account_logged_in = home_page.logged_in_user()

    assert account_logged_in == "Logged in as Abdul-ur-Rehman"


    account_deleted_verification = accountPage.delete_account()
    assert account_deleted_verification == "ACCOUNT DELETED!"

    accountPage.continue_to_HomePage()

