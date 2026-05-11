from selenium import webdriver
from Pages import LoginPage
from Pages import DropdownPage
import time
#from add_remove_page import AddRemovePage

driver = webdriver.Firefox()
page_log = LoginPage(driver)
page_drop = DropdownPage(driver)
username = "tomsmith"
password ="SuperSecretPassword!"

try:
    print("=" * 60)
    print("TP 1 SELENIUM PYTHON")
    print("=" * 60)
    
    print("=" * 40)
    print("Partie 1 : LogIn/LogOut")
    print("=" * 40)

    print("\n--- Phase 1: Ouverture de la page web ---")
    page_log.open()
    print("Accédé à practicesoftwaretesting.com")
    
    print("\n--- Phase 2: Ouverture de la page de formulaire pour le LOGIN ---")
    page_log.open_login_page()
    
    print("\n--- Phase 3: Saisie des identifiants ---")
    page_log.input_username(username)
    page_log.input_password(password)
    page_log.click_login()
    
    assert "You logged into a secure area!" in page_log.verif_message(),"La connexion a échoué"
    
    print("\n--- Phase 4: Déconnexion ---")
    page_log.click_logout()

    assert "You logged out of the secure area!" in page_log.verif_message(),"La déconnexion a échoué"
    
    print("=" * 40)
    print("Partie 2 : DropDown")
    print("=" * 40)
    
    print("\n--- Phase 1: Retour sur la page d'acceuil ---")
    page_drop.open()
    print("Accédé à practicesoftwaretesting.com")
    
    print("\n--- Phase 2: Ouverture de la page du dropdown ---")
    page_drop.open_dropdown_page()
    
    print("\n--- Phase 3: Tests sur le dropdown ---")
    option_select = page_drop.select("Option 1")
    assert option_select == "Option 1", f"Texte sélectionné incorrect : {option_select}"
    option_select = page_drop.select("Option 2")
    assert option_select == "Option 2", f"Texte sélectionné incorrect : {option_select}"
    
    
except Exception as e:
        print(f"\nErreur: {e}")
        import traceback
        traceback.print_exc()

finally:
    driver.quit()