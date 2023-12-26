diff --color -r ./hw/code/tests/group_adv_test.py ../backup_before_rebase/homework-selenium-2023-autumn/hw/code/tests/group_adv_test.py
79a80,82
>     def test_url(self, group_adv_page: GroupAdvPage):
>         group_adv_page.get_page().wait_load_page()
> 
Only in ./hw/code/tests: links.py
diff --color -r ./hw/code/tests/test_company.py ../backup_before_rebase/homework-selenium-2023-autumn/hw/code/tests/test_company.py
40c40
<         company_page.create_company()
---
>         yield company_page
42c42,44
<         time.sleep(5)
---
>     def test_create(self, preparations):
>         preparations.create_company()
>         assert is_matching_link(preparations.get_current_url(), AllLinks.COMPANY_CREATE)
44c46,48
<         datetime_moscow = datetime.now(timezone(timedelta(hours=+3), "MSC"))
---
>     def test_group(self, preparations):
>         preparations.group_view(5)
>         assert is_matching_link(preparations.get_current_url(), AllLinks.GROUP)
46,49c50,136
<         assert (
<             f"Кампания {datetime_moscow.strftime('%Y-%m-%d')}"
<             in self.driver.page_source
<         )
---
>     def test_advertisment(self, preparations):
>         preparations.advertisment_view(5)
>         assert is_matching_link(preparations.get_current_url(), AllLinks.ADVERTISEMENTS)
> 
>     def test_list(self, preparations):
>         preparations.select_action_list()
> 
>         selector_classes = preparations.get_selector_attribute()
>         assert "vkuiCustomSelect--pop-down" not in selector_classes
> 
>     @pytest.fixture
>     def setup_started_filters(self, preparations):
>         preparations.select_filter().select_started_filter().apply_filters()
>         while True:
>             try:
>                 preparations.select_company().select_action_list().select_delete_action()
>             except:
>                 break
>         yield preparations
>         preparations.select_filter().select_started_filter().apply_filters()
> 
>     def test_download(self, setup_started_filters):
>         setup_started_filters.download(5)
>         assert not setup_started_filters.is_on_site_text("Отчет по датам")
> 
>     def test_settings(self, setup_started_filters):
>         setup_started_filters.settings(5)
>         # NOTE can be taken out
>         assert not setup_started_filters.is_on_site_text("Настроить столбцы")
> 
>     @pytest.fixture
>     def setup_filter(self, preparations):
>         preparations.select_filter().select_deleted_filter().apply_filters()
>         yield preparations
>         preparations.select_filter()
>         preparations.select_deleted_filter()
>         preparations.apply_filters()
> 
>     def test_select_company_settings(self, setup_filter: CompanyPage):
>         setup_filter.select_company().settings()
>         assert setup_filter.is_on_site_text("Настроить столбцы")
> 
>     def test_select_company_downloads(self, setup_filter):
>         setup_filter.select_company().download()
>         assert setup_filter.is_on_site_text("Отчет по датам")
> 
>     @pytest.fixture
>     def create_company(self, new_company_page):
>         page = AdvPage.__new__(AdvPage)
>         page.driver = new_company_page.driver
>         page.create_company()
> 
>         company_page = CompanyPage(new_company_page.driver)
>         company_page.select_filter().select_started_filter().apply_filters()
>         yield company_page
> 
>     def test_company_deletion(self, create_company):
>         while True:
>             try:
>                 create_company.select_company().select_action_list().select_delete_action()
>             except:
>                 break
>         assert create_company.is_on_site_text(
>             "Ничего не нашлось"
>         ) or create_company.is_on_site_text("Создайте первую рекламную кампанию")
> 
>     @pytest.fixture
>     def create_draft(self, company_page):
>         page = GroupAdvPage(company_page.driver)
>         page.get_to_next()
> 
>         company_page.open()
> 
>         yield company_page
> 
>     def test_draft(self, create_draft):
>         create_draft.go_to_drafts()
>         while True:
>             try:
>                 cnt = create_draft.select_draft_option()
>                 create_draft.delete_draft().click_approve_delete().wait_until_draft_delete(
>                     cnt
>                 )
>             except:
>                 break
> 
>         assert create_draft.is_on_site_text("Создайте первую рекламную кампанию")
diff --color -r ./hw/code/tests/test_login.py ../backup_before_rebase/homework-selenium-2023-autumn/hw/code/tests/test_login.py
17,18c17,20
<     def test_login(self, credentials, login_page: LoginPage):
<         login_page.login(credentials["user"], credentials["password"])
---
>     # # HACK
>     # def test_login(self, login_page):
>     #     time.sleep(100)
>     #     save_localstorage_cookies_to_env(login_page.driver)
20,23c22,24
<         try:
<             self.driver.get_cookie("remixnsid")
<         except Exception as e:
<             assert False, f"self.driver.get_cookie raised {e}"
---
>     # TODO remove comments
>     # def test_login(self, credentials, login_page: LoginPage):
>     # login_page.login(credentials["user"], credentials["password"])
25,29c26,34
<     @pytest.mark.skip
<     @pytest.mark.parametrize("invalid_creds", [{"user": "stegozavr", "password": "a"}])
<     def test_login_neg(self, invalid_creds, login_page: LoginPage):
<         with pytest.raises(TimeoutException):
<             login_page.login(invalid_creds["user"], invalid_creds["password"])
---
>     # try:
>     #     self.driver.get_cookie("remixnsid")
>     # except Exception as e:
>     #     assert False, f"self.driver.get_cookie raised {e}"
> 
>     # @pytest.mark.parametrize("invalid_creds", [{"user": "stegozavr", "password": "a"}])
>     # def test_login_neg(self, invalid_creds):
>     #     with pytest.raises(TimeoutException):
>     #         self.login_page.login(invalid_creds["user"], invalid_creds["password"])
diff --color -r ./hw/code/ui/fixtures.py ../backup_before_rebase/homework-selenium-2023-autumn/hw/code/ui/fixtures.py
25d24
<         # service  = ServiceChrome(executable_path='/usr/local/bin/geckodriver')
29,34d27
< 
<     elif browser == "yandex":
<         service = ServiceChrome(
<             executable_path="/Users/mochalovskiy/Technopark/QA/homework-selenium-2023-autumn/chromedriver-mac-x64/chromedriver"
<         )
< 
67,71d59
< 
<     elif browser == "yandex":
<         options = webdriver.ChromeOptions()
<         options.binary_location = "/Applications/Yandex.app/Contents/MacOS/Yandex"
<         driver = webdriver.Chrome(options=options, service=service)
diff --color -r ./hw/code/ui/pages/company_page.py ../backup_before_rebase/homework-selenium-2023-autumn/hw/code/ui/pages/company_page.py
43,44d42
<         return self
< 
80a79,83
>         self.action_click(element)
>         return self
> 
>     def select_delete_action(self):
>         element = self.find(self.locators.DELETE_ACTION)
