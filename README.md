# Tři automatizované testy – Playwright

Automatizované testy webu [saucedemo.com](https://www.saucedemo.com) (cvičný e-shop určený k testování).
Projekt z kurzu Testing Akademie (Engeto).

## Co se testuje

| Test | Co ověřuje |
|---|---|
| `test_prihlaseni_platne_udaje` | Přihlášení platnými údaji otevře stránku s produkty. |
| `test_prihlaseni_spatne_heslo` | Při špatném hesle se zobrazí chybová hláška a uživatel se nepřihlásí. |
| `test_pridani_produktu_do_kosiku` | Po přidání produktu do košíku se u košíku zobrazí počet 1. |

## Požadavky

- Python 3.9 nebo novější
- knihovny z `requirements.txt` (pytest, pytest-playwright)

## Instalace

```
pip install -r requirements.txt
playwright install
```

Na macOS případně `pip3` a `python3 -m playwright install`.

## Spuštění testů

```
pytest test_saucedemo.py
```

S viditelným oknem prohlížeče:

```
pytest test_saucedemo.py --headed
```

## Soubory

- `test_saucedemo.py` – testy; adresa webu je jednou v konstantě `BASE_URL` a otevření stránky i přihlášení řeší fixtures `prihlasovaci_stranka` a `prihlasena_stranka`, takže se kód v testech neopakuje
- `requirements.txt` – potřebné knihovny
