"""
Time:2020/1/31 0031
"""
import pytest

if __name__ == '__main__':
    pytest.main(["--reruns", "1", "--reruns-delay", "5",
                 "--junitxml=reports/allure.xml"])
