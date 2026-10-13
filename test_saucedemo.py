import re

import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com"


@pytest.fixture
def prihlasovaci_stranka(page: Page) -> Page:
    """Otevře přihlašovací stránku e-shopu."""
    page.goto(BASE_URL)
    return page


@pytest.fixture
def prihlasena_stranka(prihlasovaci_stranka: Page) -> Page:
    """Přihlásí standardního uživatele a vrátí stránku se seznamem produktů."""
    prihlasovaci_stranka.get_by_placeholder("Username").fill("standard_user")
    prihlasovaci_stranka.get_by_placeholder("Password").fill("secret_sauce")
    prihlasovaci_stranka.get_by_role("button", name="Login").click()
    return prihlasovaci_stranka


def test_prihlaseni_platne_udaje(prihlasena_stranka: Page):
    """Po přihlášení platnými údaji se zobrazí seznam produktů."""
    expect(prihlasena_stranka).to_have_url(re.compile("inventory.html"))
    expect(prihlasena_stranka.locator('[data-test="title"]')).to_have_text("Products")


def test_prihlaseni_spatne_heslo(prihlasovaci_stranka: Page):
    """Při špatném hesle se zobrazí chybová hláška a uživatel zůstane na přihlášení."""
    prihlasovaci_stranka.get_by_placeholder("Username").fill("standard_user")
    prihlasovaci_stranka.get_by_placeholder("Password").fill("spatne_heslo")
    prihlasovaci_stranka.get_by_role("button", name="Login").click()

    expect(prihlasovaci_stranka.locator('[data-test="error"]')).to_contain_text(
        "Username and password do not match"
    )
    expect(prihlasovaci_stranka).not_to_have_url(re.compile("inventory.html"))


def test_pridani_produktu_do_kosiku(prihlasena_stranka: Page):
    """Po přidání produktu do košíku se na ikoně košíku zobrazí počet 1."""
    prihlasena_stranka.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    expect(prihlasena_stranka.locator('[data-test="shopping-cart-badge"]')).to_have_text("1")
    expect(prihlasena_stranka.locator('[data-test="remove-sauce-labs-backpack"]')).to_be_visible()
