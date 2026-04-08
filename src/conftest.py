import os
import pytest
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()


@pytest.fixture(scope="session", autouse=True)
def BASE_URL():
    return os.environ["BASE_URL"]


@pytest.fixture(scope="session", autouse=True)
def EMAIL():
    return os.environ["EMAIL"]


@pytest.fixture(scope="session", autouse=True)
def PASSWORD():
    return os.environ["PASSWORD"]
