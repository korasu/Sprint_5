from selenium.webdriver.common.by import By


class Locator:
    account_entry = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")  # локатор для кнопки "Войти в аккаунт"
    register = (By.XPATH, ".//a[@href = '/register']")  # локатор для кнопки перехода к форме регистрации
    form_login = (By.CSS_SELECTOR, ".Auth_login__3hAey")  # локатор страницы логина
    name = (By.XPATH, ".//label[text() = 'Имя']/following-sibling::input")  # локатор ввода имени пользователя
    login = (By.XPATH, ".//label[text() = 'Email']/following-sibling::input")  # локатор ввода email пользователя
    password = (By.XPATH, ".//label[text() = 'Пароль']/following-sibling::input")  # локатор ввода пароля пользователя
    button_registration = (By.XPATH, ".//button[text() = 'Зарегистрироваться']")  # локатор кнопки "Зарегистрироваться"
    button_login = (By.XPATH, ".//button[text() = 'Войти']")  # локатор кнопки "Войти"
    error = (By.XPATH, ".//p[@class = 'input__error text_type_main-default']")  # локатор текста ошибки при неверном
    # пароля
    login_email = (By.NAME, "name")  # локатор ввода email пользователя на странице логина
    login_password = (By.NAME, "Пароль")  # локатор ввода пароля пользователя на странице логина
    constructr_block = (By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2")  # локатор секции с конструкторами
    # бургеров
    lk_in_header = (By.XPATH, ".//a[@href = '/account']")  # локатор кнопки личного кабинета
    login_page_from_registration = (By.CLASS_NAME, "Auth_link__1fOlj")  # локатор страницы логина через регистрацию
    link_for_recovery_password = (
        By.XPATH, ".//a[@href = '/forgot-password']")  # локатор для перехода на страницу восстановления пароля
    link_for_setting_profile = (By.XPATH, ".//a[@href = '/account/profile']")  # локатор для настроек профиля
    logo_in_header = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")  # локатор для лога в заголовке страницы
    constructor_in_header = (
        By.CLASS_NAME, "AppHeader_header__linkText__3q_va")  # локатор для кнопки конструктора в заголовке
    logout_button = (By.XPATH,
                     ".//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']")  #
    # локатор для кнопки выхода из ЛК
    button_sauces = (By.XPATH, ".//span[text() = 'Соусы']")  # локатор для кнопки соусов в конструкторе бургеров
    button_buns = (By.XPATH, ".//span[text() = 'Булки']")  # локатор для кнопки булки в конструкторе бургеров
    button_fillers = (By.XPATH, ".//span[text() = 'Начинки']")  # локатор для кнопки начинки в конструкторе бургеров
    # локатор для подтверждения, что выбрана начинка
    constructor_page_fillers_proof_element = (By.XPATH,'.//span[text()="Начинки"]/parent::div')

    # локатор для подтверждения, что выбрана соусы
    constructor_page_sauces_proof_element = (By.XPATH,'.//span[text()="Соусы"]/parent::div')

    # локатор для подтверждения, что выбрана булки
    constructor_page_buns_proof_element = (By.XPATH, './/span[text()="Булки"]/parent::div')
