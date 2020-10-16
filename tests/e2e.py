import sys

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

try:
    param_1 = sys.argv[1]
    param_2 = sys.argv[2]
except IndexError:
    param_1 = "192.168.95.5"
    param_2 = "8777"
driver = webdriver.Chrome(ChromeDriverManager().install())

'''it’s purpose is to test our web service. It will get the application
URL as an input, open a browser to that URL, select the score element in our web page,
check that it is a number between 1 to 1000 and return a boolean value if it’s true or not.'''


def test_scores_service(url, port) -> int:
    try:
        driver.get("http://" + url + ":" + port)
        driver.implicitly_wait(5)  # wait up to
        actual = driver.find_element_by_id("score").text
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
    if 0 == int(test_scores_service(url, port)):
        sys.exit(0)
    else:
        sys.exit(-1)


if __name__ == "__main__":
    param_1 = "192.168.95.5"
    param_2 = "8777"
    main_function(param_1, param_2)
