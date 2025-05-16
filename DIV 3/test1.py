from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import unittest
import time

class SearchTests(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(30)
        self.driver.get("https://demo-m2.bird.eu/")

    def tearDown(self):
        self.driver.quit()

    def test_title_is_not_empty(self):
        title = self.driver.title
        print("Titre de la page :", title)
        self.assertTrue(len(title) > 0, "Le titre de la page est vide.")

    def test_search_backpack(self):
        driver = self.driver
        search_field = driver.find_element(By.ID, "search")
        search_field.send_keys("backpack")
        search_field.send_keys(Keys.RETURN)
        time.sleep(15)

        product_names = driver.find_elements(By.CSS_SELECTOR, ".product.name.product-item-name")
        result_count = len(product_names)
        print(f"Nombre de résultats trouvés : {result_count}")

        if result_count == 0:
            print("Aucun produit n'a été affiché pour la recherche 'backpack'.")
        else:
            all_valid = True
            for product in product_names:
                product_text = product.text
                print("Produit trouvé :", product_text)
                if "Backpack" not in product_text:
                    print(f"⚠️ Le produit '{product_text}' ne contient pas 'Backpack'.")
                    all_valid = False
            if all_valid:
                print("✅ Tous les produits affichés contiennent 'Backpack' dans leur nom.")


if __name__ == "__main__":
    unittest.main()
