from selenium import webdriver
from POM.InterviewQuery import Shopping

driver = webdriver.Chrome()
driver.maximize_window()
shop=Shopping(driver)

shop.openpage()
shop.searchbar()
shop.searchbtn()

results=shop.productfilters(3)

for items in results :
    print("Products agsint Olpers on Page 1 to Page 3 are",items)
    assert len(items)==len(set(items)) ,"Duplicate Products Found"

print("Total Products are" , len(results))

    #titles = ['A','B','C']
    #len(titles) = 3
    #len(set(titles)) = 3 (It Removes Duplicate Items)
    #Assertion passes ✅

def Validations () :

  prod_found = False

  for page in range(1,4):

    products=shop.productfilters(page)
    for item in products:
        print(item)
    if any ("Olpers UHT Milk 1500ml" in item[0] for item in products):
        print(f"Product :Olpers UHT Milk 1500ml found on Page {page}")
        prod_found=True
        break

  assert prod_found, "Olpers UHT Milk 1500ml not found in first 3 pages"

Validations()