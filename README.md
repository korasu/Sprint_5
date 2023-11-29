# Sprint_5
UI test for final project

В данном проекте реализованы тесты для сайта [Stellar Burgers](https://stellarburgers.nomoreparties.site)

Файлы с тестами лежат в папке tests и имеют следующие название:
* test_registration.py - в данном файле находятся тесты связанные с функциональностью регистрации;
* test_authorization.py - в данном файле находятся тесты связанные с функциональностью авторизации;
* test_lk.py - в данном файле находятся тесты связанные с функциональностью личного кабинета;
* test_constructor.py - в данном файле находятся тесты связанные с функциональностью конструктора бургеров.

Так-же в папке tests лежит файл с фикстурами для проекта.

## Тесты test_registration.py
В данном разделе описаны тесты находящиеся в файле test_registration.py.

1. test_success_registration - тест для выполнения успешной регистрации;
2. test_failed_registration_incorrect_password - негативный тест для выявления ошибки при пароле с неверной длинной.

## Тесты test_authorization.py
В данном разделе описаны тесты находящиеся в файле test_authorization.py.

1. test_success_login_with_click_button_entry_in_account - тест на авторизацию пользователя через кнопку "Войти в аккаунт";
2. test_success_login_with_click_button_lk - тест на авторизацию пользователя через кнопку "Личный кабинет";
3. test_success_login_across_registration_page - тест на авторизацию пользователя через страницу регистрации;
4. test_success_login_across_recovery_password_page - тест на авторизацию пользователя проходящий через страницу восстановления пароля;

## Тесты test_lk.py
В данном разделе описаны тесты находящиеся в файле test_lk.py.

1. test_open_lk_page - тест на переход в личный кабинет;
2. test_switch_lk_to_construct_with_click_to_logo - тест на переход из личнего кабинета на главную страницу через лого сайта;
3. test_switch_lk_to_construct_with_click_to_constructor_button - тест на переход из личного кабинета на главную страницу по кнопке конструктор бургеров;
4. test_exit_from_lk - тест на выход из личного кабинета

## Тесты test_constructor.py
В данном разделе описаны тесты находящиеся в файле test_constructor.py.

1. test_constructor_stay_at_rolls - тест на выбор рездела "Булки" конструктора;
2. test_constructor_stay_at_sauces - тест на выбор рездела "Соусы" конструктора;
3. test_constructor_stay_at_fillings - тест на выбор рездела "Начинки" конструктора.

## Содержание conftest.py
В данном файле лежат фикстуры для тестов.

1. create_name - генератор имени пользователя;
2. create_login - генератор электронной почты;
3. create_password - генератор верного пароля;
4. create_incorrect_password - генератор неверных паролей;
5. create_account - фикстура для передачи логина с паролем зарегистрированного пользователя;
6. authorized - фикстура для передачи параметров авторизированного пользователя.