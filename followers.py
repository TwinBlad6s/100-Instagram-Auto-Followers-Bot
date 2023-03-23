from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

#replace with your 10 temp mail or with dot gmails for auto 100 instagram followers for each account 10 followers !

#one after one it take process after one bot run its close the tab and open new tab and create new one !

a=['google@gmail.com']
b=['yahoo@gmail.com'] 
c=['twitter@gmail.com'] 
d=['youtube@gmail.com']
e=['snapshot@gmail.com']
f=['instagram@gmail.com']
g=['blocker@gmail.com']
h=['linkedin@gmail.com']
i=['chrome@gmail.com']
j=['crickbuzz@gmail.com']

name = ["Alan", "Murat", "Azad", "Necati", "Aaron", "Aaron-James", "Aarron", "Aaryan", "Aaryn", "Aayan",
                 "Aazaan", "Abaan", "Abbas", "Abdallah", "Abdalroof", "Abdihakim", "Abdirahman", "Abdisalam", "Abdul",
                 "Abdul-Aziz", "Abdulbasir", "Abdulkadir", "Abdulkarem", "Abdulkhader", "Abdullah", "Abdul-Majeed",
                 "Abdulmalik", "Abdul-Rehman", "Abdur", "Abdurraheem", "Abdur-Rahman", "Abdur-Rehmaan", "Abel",
                 "Abhinav", "Abhisumant", "Abid", "Abir", "Abraham", "Abu", "Abubakar", "Ace", "Adain", "Adam",
                 "Adam-James", "Addison", "Addisson", "Adegbola", "Adegbolahan", "Aden", "Adenn", "Adie", "Adil",
                 "Aditya", "Adnan", "Adrian", "Adrien", "Aedan", "Aedin", "Aedyn", "Aeron", "Afonso", "Ahmad", "Ahmed",
                 "Ahmed-Aziz", "Ahoua", "Ahtasham", "Aiadan", "Aidan", "Aiden", "Aiden-Jack", "Aiden-Vee", "Aidian",
                 "Aidy", "Ailin", "Aiman", "Ainsley", "Ainslie", "Airen", "Airidas", "Airlie", "AJ", "Ajay", "A-Jay",
                 "Ajayraj", "Akan", "Akram", "Al", "Ala", "Alan", "Alanas", "Alasdair", "Alastair", "Alber", "Albert",
                 "Albie", "Aldred", "Alec", "Aled", "Aleem", "Aleksandar", "Aleksander", "Aleksandr", "Aleksandrs",
                 "Alekzander", "Alessandro", "Alessio", "Alex", "Alexander", "Alexei", "Alexx", "Alexzander", "Alf",
                 "Alfee", "Alfie", "Alfred", "Alfy", "Alhaji", "Al-Hassan", "Ali", "Aliekber", "Alieu", "Alihaider",
                 "Alisdair", "Alishan", "Alistair", "Alistar", "Alister", "Aliyaan", "Allan", "Allan-Laiton", "Allen",
                 "Allesandro", "Allister", "Ally", "Alphonse", "Altyiab", "Alum", "Alvern", "Alvin", "Alyas", "Amaan",
                 "Aman", "Amani", "Ambanimoh", "Ameer", "Amgad", "Ami", "Amin", "Amir", "Ammaar", "Ammar", "Ammer",
                 "Amolpreet", "Amos", "Amrinder", "Amrit", "Amro", "Anay", "Andrea", "Andreas", "Andrei", "Andrejs",
                 "Andrew", "Andy", "Anees", "Anesu", "Angel", "Angelo", "Angus", "Anir", "Anis", "Anish", "Anmolpreet",
                 "Annan", "Anndra", "Anselm", "Anthony", "Anthony-John", "Antoine", "Anton", "Antoni", "Antonio",
                 "Antony", "Antonyo", "Anubhav", "Aodhan", "Aon", "Aonghus", "Apisai", "Arafat", "Aran", "Arandeep",
                 "Arann", "Aray", "Arayan", "Archibald", "Archie", "Arda", "Ardal", "Ardeshir", "Areeb", "Areez",
                 "Aref", "Arfin", "Argyle", "Argyll", "Ari", "Aria", "Arian", "Arihant", "Aristomenis", "Aristotelis",
                 "Arjuna", "Arlo", "Armaan", "Arman", "Armen", "Arnab", "Arnav", "Arnold", "Aron", "Aronas", "Arran",
                 "Arrham", "Arron", "Arryn", "Arsalan", "Artem", "Arthur", "Artur", "Arturo", "Arun", "Arunas", "Arved",
                 "Arya", "Aryan", "Aryankhan", "Aryian", "Aryn", "Asa", "Asfhan", "Ash", "Ashlee-jay", "Ashley",
                 "Ashton", "Ashton-Lloyd", "Ashtyn", "Ashwin", "Asif", "Asim", "Aslam", "Asrar", "Ata", "Atal",
                 "Atapattu", "Ateeq", "Athol", "Athon", "Athos-Carlos", "Atli", "Atom", "Attila", "Aulay", "Aun",
                 "Austen", "Austin", "Avani", "Averon", "Avi", "Avinash", "Avraham", "Awais", "Awwal", "Axel", "Ayaan",
                 "Ayan", "Aydan", "Ayden", "Aydin", "Aydon", "Ayman", "Ayomide", "Ayren", "Ayrton", "Aytug", "Ayub",
                 "Ayyub", "Azaan", "Azedine", "Azeem", "Azim", "Aziz", "Azlan", "Azzam", "Azzedine", "Babatunmise",
                 "Babur", "Bader", "Badr", "Badsha", "Bailee", "Bailey", "Bailie", "Bailley", "Baillie", "Baley",
                 "Balian", "Banan", "Barath", "Barkley", "Barney", "Baron", "Barrie", "Barry", "Bartlomiej", "Bartosz",
                 "Basher", "Basile", "Baxter", "Baye", "Bayley", "Beau", "Beinn", "Bekim", "Believe", "Ben", "Bendeguz",
                 "Benedict", "Benjamin", "Benjamyn", "Benji", "Benn", "Bennett", "Benny", "Benoit", "Bentley", "Berkay",
                 "Bernard", "Bertie", "Bevin", "Bezalel", "Bhaaldeen", "Bharath", "Bilal", "Bill", "Billy", "Binod",
                 "Bjorn", "Blaike", "Blaine", "Blair", "Blaire", "Blake", "Blazej", "Blazey", "Blessing", "Blue",
                 "Blyth", "Bo", "Boab", "Bob", "Bobby", "Bobby-Lee", "Bodhan", "Boedyn", "Bogdan", "Bohbi", "Bony",
                 "Bowen", "Bowie", "Boyd", "Bracken", "Brad", "Bradan", "Braden", "Bradley", "Bradlie", "Bradly",
                 "Brady", "Bradyn", "Braeden", "Braiden", "Brajan", "Brandan", "Branden", "Brandon", "Brandonlee",
                 "Brandon-Lee", "Brandyn", "Brannan", "Brayden", "Braydon", "Braydyn", "Breandan", "Brehme", "Brendan",
                 "Brendon", "Brendyn", "Breogan", "Bret", "Brett", "Briaddon", "Brian", "Brodi", "Brodie", "Brody",
                 "Brogan", "Broghan", "Brooke", "Brooklin", "Brooklyn", "Bruce", "Bruin", "Bruno", "Brunon", "Bryan",
                 "Bryce", "Bryden", "Brydon", "Brydon-Craig", "Bryn", "Brynmor", "Bryson", "Buddy", "Bully", "Burak",
                 "Burhan", "Butali", "Butchi", "Byron", "Cabhan", "Cadan", "Cade", "Caden", "Cadon", "Cadyn", "Caedan",
                 "Caedyn", "Cael", "Caelan", "Caelen", "Caethan", "Cahl", "Cahlum", "Cai", "Caidan", "Melim"]

#below code is for block the notification for these website no needed!
#chrome_options = webdriver.ChromeOptions()
#prefs = {"profile.default_content_setting_values.notifications" : 2}
#chrome_options.add_experimental_option("prefs",prefs)
#driver = webdriver.Chrome(chrome_options=chrome_options)

driver = webdriver.Chrome()
driver.get("https://bsp-panel.com/")
time.sleep(2)
driver.find_element_by_xpath('/html/body/section[1]/div/div/div[2]/form/span[1]/a').click()#three dots
time.sleep(2)
driver.find_element_by_name("name").send_keys(random.choice(name))#name
time.sleep(2)
driver.find_element_by_name("email").send_keys(random.choice(a)) #email
time.sleep(2)
driver.find_element_by_name("password").send_keys('Loose123@#$%')#password
time.sleep(2)
driver.find_element_by_name("password_confirmation").send_keys('Loose123@#$%')#password_confirmation

time.sleep(30)#you only click that i am not a robot and clear that verification select all images with ------ in 20 seconds or 25 seconds(your capacity) remaining things go automatic!

driver.find_element_by_name("RegistrationForm[termsofservice]").click()#check box tick
time.sleep(2)
driver.find_element_by_xpath('/html/body/section/div/div/div/div/form/button[1]').click()#sign up button click
time.sleep(5)
#they ask for ok button click that!
#driver.find_element_by_xpath('/html/body/div[5]/div/div[3]/button[1]')#Ok Button Click
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/form/fieldset/div[6]/input').send_keys('https://www.instagram.com/using_robot/')#which acc you want to make followers paste that acc link here.
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/form/fieldset/div[7]/input').send_keys('10')#quantity
time.sleep(2)
driver.find_element_by_id("btn-proceed").click()#proceed
time.sleep(15)
driver.close()

driver = webdriver.Chrome()
driver.get("https://bsp-panel.com/")
time.sleep(2)
driver.find_element_by_xpath('/html/body/section[1]/div/div/div[2]/form/span[1]/a').click()#three dots
time.sleep(2)
driver.find_element_by_name("name").send_keys(random.choice(name))#name
time.sleep(2)
driver.find_element_by_name("email").send_keys(random.choice(b)) #email
time.sleep(2)
driver.find_element_by_name("password").send_keys('Loose123@#$%')#password
time.sleep(2)
driver.find_element_by_name("password_confirmation").send_keys('Loose123@#$%')#password_confirmation

time.sleep(30)#you only click that i am not a robot and clear that verification select all images with ------ in 20 seconds or 25 seconds(your capacity) remaining things go automatic!

driver.find_element_by_name("RegistrationForm[termsofservice]").click()#check box tick
time.sleep(2)
driver.find_element_by_xpath('/html/body/section/div/div/div/div/form/button[1]').click()#sign up button click
time.sleep(5)
#they ask for ok button click that!
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/form/fieldset/div[6]/input').send_keys('https://www.instagram.com/using_robot/')#which acc you want to make followers paste that acc link here.
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/form/fieldset/div[7]/input').send_keys('10')#quantity
time.sleep(2)
driver.find_element_by_id("btn-proceed").click()#proceed
time.sleep(15)
driver.close()

driver = webdriver.Chrome()
driver.get("https://bsp-panel.com/")
time.sleep(2)
driver.find_element_by_xpath('/html/body/section[1]/div/div/div[2]/form/span[1]/a').click()#three dots
time.sleep(2)
driver.find_element_by_name("name").send_keys(b(name))#name
time.sleep(2)
driver.find_element_by_name("email").send_keys(random.choice(c)) #email
time.sleep(2)
driver.find_element_by_name("password").send_keys('Loose123@#$%')#password
time.sleep(2)
driver.find_element_by_name("password_confirmation").send_keys('Loose123@#$%')#password_confirmation

time.sleep(30)#you only click that i am not a robot and clear that verification select all images with ------ in 20 seconds or 25 seconds(your capacity) remaining things go automatic!

driver.find_element_by_name("RegistrationForm[termsofservice]").click()#check box tick
time.sleep(2)
driver.find_element_by_xpath('/html/body/section/div/div/div/div/form/button[1]').click()#sign up button click
time.sleep(5)
#they ask for ok button click that!
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/form/fieldset/div[6]/input').send_keys('https://www.instagram.com/using_robot/')#which acc you want to make followers paste that acc link here.
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/form/fieldset/div[7]/input').send_keys('10')#quantity
time.sleep(2)
driver.find_element_by_id("btn-proceed").click()#proceed
time.sleep(15)
driver.close()

driver = webdriver.Chrome()
driver.get("https://bsp-panel.com/")
time.sleep(2)
driver.find_element_by_xpath('/html/body/section[1]/div/div/div[2]/form/span[1]/a').click()#three dots
time.sleep(2)
driver.find_element_by_name("name").send_keys(random.choice(name))#name
time.sleep(2)
driver.find_element_by_name("email").send_keys(random.choice(d)) #email
time.sleep(2)
driver.find_element_by_name("password").send_keys('Loose123@#$%')#password
time.sleep(2)
driver.find_element_by_name("password_confirmation").send_keys('Loose123@#$%')#password_confirmation

time.sleep(30)#you only click that i am not a robot and clear that verification select all images with ------ in 20 seconds or 25 seconds(your capacity) remaining things go automatic!

driver.find_element_by_name("RegistrationForm[termsofservice]").click()#check box tick
time.sleep(2)
driver.find_element_by_xpath('/html/body/section/div/div/div/div/form/button[1]').click()#sign up button click
time.sleep(5)
#they ask for ok button click that!
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/form/fieldset/div[6]/input').send_keys('https://www.instagram.com/using_robot/')#which acc you want to make followers paste that acc link here.
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/form/fieldset/div[7]/input').send_keys('10')#quantity
time.sleep(2)
driver.find_element_by_id("btn-proceed").click()#proceed
time.sleep(15)
driver.close()

driver = webdriver.Chrome()
driver.get("https://bsp-panel.com/")
time.sleep(2)
driver.find_element_by_xpath('/html/body/section[1]/div/div/div[2]/form/span[1]/a').click()#three dots
time.sleep(2)
driver.find_element_by_name("name").send_keys(random.choice(name))#name
time.sleep(2)
driver.find_element_by_name("email").send_keys(random.choice(e)) #email
time.sleep(2)
driver.find_element_by_name("password").send_keys('Loose123@#$%')#password
time.sleep(2)
driver.find_element_by_name("password_confirmation").send_keys('Loose123@#$%')#password_confirmation

time.sleep(30)#you only click that i am not a robot and clear that verification select all images with ------ in 20 seconds or 25 seconds(your capacity) remaining things go automatic!

driver.find_element_by_name("RegistrationForm[termsofservice]").click()#check box tick
time.sleep(2)
driver.find_element_by_xpath('/html/body/section/div/div/div/div/form/button[1]').click()#sign up button click
time.sleep(5)
#they ask for ok button click that!
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/form/fieldset/div[6]/input').send_keys('https://www.instagram.com/using_robot/')#which acc you want to make followers paste that acc link here.
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/form/fieldset/div[7]/input').send_keys('10')#quantity
time.sleep(2)
driver.find_element_by_id("btn-proceed").click()#proceed
time.sleep(15)
driver.close()

driver = webdriver.Chrome()
driver.get("https://bsp-panel.com/")
time.sleep(2)
driver.find_element_by_xpath('/html/body/section[1]/div/div/div[2]/form/span[1]/a').click()#three dots
time.sleep(2)
driver.find_element_by_name("name").send_keys(random.choice(name))#name
time.sleep(2)
driver.find_element_by_name("email").send_keys(random.choice(f)) #email
time.sleep(2)
driver.find_element_by_name("password").send_keys('Loose123@#$%')#password
time.sleep(2)
driver.find_element_by_name("password_confirmation").send_keys('Loose123@#$%')#password_confirmation

time.sleep(30)#you only click that i am not a robot and clear that verification select all images with ------ in 20 seconds or 25 seconds(your capacity) remaining things go automatic!

driver.find_element_by_name("RegistrationForm[termsofservice]").click()#check box tick
time.sleep(2)
driver.find_element_by_xpath('/html/body/section/div/div/div/div/form/button[1]').click()#sign up button click
time.sleep(5)
#they ask for ok button click that!
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/form/fieldset/div[6]/input').send_keys('https://www.instagram.com/using_robot/')#which acc you want to make followers paste that acc link here.
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/form/fieldset/div[7]/input').send_keys('10')#quantity
time.sleep(2)
driver.find_element_by_id("btn-proceed").click()#proceed
time.sleep(15)
driver.close()

driver = webdriver.Chrome()
driver.get("https://bsp-panel.com/")
time.sleep(2)
driver.find_element_by_xpath('/html/body/section[1]/div/div/div[2]/form/span[1]/a').click()#three dots
time.sleep(2)
driver.find_element_by_name("name").send_keys(random.choice(name))#name
time.sleep(2)
driver.find_element_by_name("email").send_keys(random.choice(g)) #email
time.sleep(2)
driver.find_element_by_name("password").send_keys('Loose123@#$%')#password
time.sleep(2)
driver.find_element_by_name("password_confirmation").send_keys('Loose123@#$%')#password_confirmation

time.sleep(30)#you only click that i am not a robot and clear that verification select all images with ------ in 20 seconds or 25 seconds(your capacity) remaining things go automatic!

driver.find_element_by_name("RegistrationForm[termsofservice]").click()#check box tick
time.sleep(2)
driver.find_element_by_xpath('/html/body/section/div/div/div/div/form/button[1]').click()#sign up button click
time.sleep(5)
#they ask for ok button click that!
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/form/fieldset/div[6]/input').send_keys('https://www.instagram.com/using_robot/')#which acc you want to make followers paste that acc link here.
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/form/fieldset/div[7]/input').send_keys('10')#quantity
time.sleep(2)
driver.find_element_by_id("btn-proceed").click()#proceed
time.sleep(15)
driver.close()

driver = webdriver.Chrome()
driver.get("https://bsp-panel.com/")
time.sleep(2)
driver.find_element_by_xpath('/html/body/section[1]/div/div/div[2]/form/span[1]/a').click()#three dots
time.sleep(2)
driver.find_element_by_name("name").send_keys(random.choice(name))#name
time.sleep(2)
driver.find_element_by_name("email").send_keys(random.choice(h)) #email
time.sleep(2)
driver.find_element_by_name("password").send_keys('Loose123@#$%')#password
time.sleep(2)
driver.find_element_by_name("password_confirmation").send_keys('Loose123@#$%')#password_confirmation

time.sleep(30)#you only click that i am not a robot and clear that verification select all images with ------ in 20 seconds or 25 seconds(your capacity) remaining things go automatic!

driver.find_element_by_name("RegistrationForm[termsofservice]").click()#check box tick
time.sleep(2)
driver.find_element_by_xpath('/html/body/section/div/div/div/div/form/button[1]').click()#sign up button click
time.sleep(5)
#they ask for ok button click that!
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/form/fieldset/div[6]/input').send_keys('https://www.instagram.com/using_robot/')#which acc you want to make followers paste that acc link here.
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/form/fieldset/div[7]/input').send_keys('10')#quantity
time.sleep(2)
driver.find_element_by_id("btn-proceed").click()#proceed
time.sleep(15)
driver.close()

driver = webdriver.Chrome()
driver.get("https://bsp-panel.com/")
time.sleep(2)
driver.find_element_by_xpath('/html/body/section[1]/div/div/div[2]/form/span[1]/a').click()#three dots
time.sleep(2)
driver.find_element_by_name("name").send_keys(random.choice(name))#name
time.sleep(2)
driver.find_element_by_name("email").send_keys(random.choice(i)) #email
time.sleep(2)
driver.find_element_by_name("password").send_keys('Loose123@#$%')#password
time.sleep(2)
driver.find_element_by_name("password_confirmation").send_keys('Loose123@#$%')#password_confirmation

time.sleep(30)#you only click that i am not a robot and clear that verification select all images with ------ in 20 seconds or 25 seconds(your capacity) remaining things go automatic!

driver.find_element_by_name("RegistrationForm[termsofservice]").click()#check box tick
time.sleep(2)
driver.find_element_by_xpath('/html/body/section/div/div/div/div/form/button[1]').click()#sign up button click
time.sleep(5)
#they ask for ok button click that!
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/form/fieldset/div[6]/input').send_keys('https://www.instagram.com/using_robot/')#which acc you want to make followers paste that acc link here.
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/form/fieldset/div[7]/input').send_keys('10')#quantity
time.sleep(2)
driver.find_element_by_id("btn-proceed").click()#proceed
time.sleep(15)
driver.close()

driver = webdriver.Chrome()
driver.get("https://bsp-panel.com/")
time.sleep(2)
driver.find_element_by_xpath('/html/body/section[1]/div/div/div[2]/form/span[1]/a').click()#three dots
time.sleep(2)
driver.find_element_by_name("name").send_keys(random.choice(name))#name
time.sleep(2)
driver.find_element_by_name("email").send_keys(random.choice(j)) #email
time.sleep(2)
driver.find_element_by_name("password").send_keys('Loose123@#$%')#password
time.sleep(2)
driver.find_element_by_name("password_confirmation").send_keys('Loose123@#$%')#password_confirmation

time.sleep(30)#you only click that i am not a robot and clear that verification select all images with ------ in 20 seconds or 25 seconds(your capacity) remaining things go automatic!

driver.find_element_by_name("RegistrationForm[termsofservice]").click()#check box tick
time.sleep(2)
driver.find_element_by_xpath('/html/body/section/div/div/div/div/form/button[1]').click()#sign up button click
time.sleep(5)
#they ask for ok button click that!
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/form/fieldset/div[6]/input').send_keys('https://www.instagram.com/using_robot/')#which acc you want to make followers paste that acc link here.
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/form/fieldset/div[7]/input').send_keys('10')#quantity
time.sleep(2)
driver.find_element_by_id("btn-proceed").click()#proceed
time.sleep(15)
driver.close()
