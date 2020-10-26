"""it’s purpose is to test our web service. It will get the application
URL as an input, open a browser to that URL, select the score element in our web page,
check that it is a number between 1 to 1000 and return a boolean value if it’s true or not."""


def test_scores_service(url, port) -> int:
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('--no-default-browser-check')
    chrome_options.add_argument('--no-first-run')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--enable-automation')

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    try:
        driver.get("http://" + url + ":" + port)
        driver.implicitly_wait(5)  # wait up to
        actual = driver.find_element_by_id("score").text
        #print(actual)
        if 1 <= int(actual) <= 1000:
            driver.close()
            return 0
        else:
            return 1
    except Exception:
        driver.close()
        return 1


'''to call our tests function. The main function will return -1 as an OS exit
code if the tests failed and 0 if they passed.'''


def main_function(url, port):
    import sys
    if 0 == int(test_scores_service(url, port)):
        sys.exit(0)
    else:
        sys.exit(-1)


if __name__ == "__main__":
    from sys import argv

    try:
        # print(len(argv))
        if len(argv) == 3:
            param_1 = argv[1:]
            param_2 = argv[2:]
            main_function(param_1, param_2)
        elif len(argv) == 2:
            param_1 = argv[1:]
            param_2 = "8777"
            main_function(param_1, param_2)
        elif len(argv) == 1:
            param_1 = "127.0.0.1"
            param_2 = "8777"
            main_function(param_1, param_2)
        # main_function(param_1, param_2)
        else:
            print('Please provide IP and Port number...')
    except IndexError:
        param_1 = "192.168.95.5"
        param_2 = "8777"
