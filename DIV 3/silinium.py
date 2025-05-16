from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialiser le navigateur Firefox
driver = webdriver.Chrome()

# Étape 1: Accéder à la page de création de compte
driver.get("https://demo-m2.bird.eu/customer/account/create/")

# Étape 2: Remplir le formulaire de création de compte
wait = WebDriverWait(driver, 40)

# Saisir le prénom
first_name = wait.until(EC.presence_of_element_located((By.ID, "firstname")))
first_name.send_keys("firstname")

# Saisir le nom de famille
last_name = driver.find_element(By.ID, "lastname")
last_name.send_keys("lastname")

# Saisir l'adresse email
email = driver.find_element(By.ID, "email_address")
email.send_keys("XXXXX@exampl.com")

# Saisir le mot de passe
password = driver.find_element(By.ID, "password")
password.send_keys("Password123")

# Attendre que le champ de confirmation de mot de passe soit visible et l'identifier avec le bon ID
password_confirm = driver.find_element(By.ID, "password-confirmation")
password_confirm.send_keys("Password123")
time.sleep(5)
# Soumettre le formulaire
submit_button = driver.find_element(By.CLASS_NAME, "action.submit.primary")
submit_button.click()

time.sleep(5)

# Vérifier si le texte de confirmation est bien présent dans la page source
if "Thank you for registering with Main Website Store." in driver.page_source:
    print("Le message de confirmation est bien affiché.")
else:
    print("Le message de confirmation n'a pas été trouvé.")

time.sleep(5)

# Saisir l'email et le mot de passe dans les champs de connexion
#email_field = driver.find_element(By.ID, "email")
#password_field = driver.find_element(By.ID, "password")

#email_field.send_keys("examp@example.com")
#password_field.send_keys("Password123")

# Soumettre le formulaire de connexion
##login_button = driver.find_element(By.CLASS_NAME, "action.login.primary")
#login_button.click()

#driver.quit()
