import random 

api_1  = "bb02fc26-4955-4b88-86cd-71003e245eca"  # 1_Health_harvest
api_2  = "fa08072b-f2c3-4230-ae1b-6324c73b28bd"  # 2_Mobile_Portal_India
api_3  = "3d3e6f57-d729-4b82-861f-4fde5148bb10"  # 3_my_book_buddy
api_4  = "db7d8c78-f866-4e6a-9378-f61ba54dd251"  # 4_My_compute
api_5  = "8740a16f-c01a-4cee-bff7-0c760cadf76c"  # 5_My_fatty_cats
api_6  = "7198c231-27f8-464e-9953-ce8587a26662"  # 6_Only_Books
api_7  = "87a7f658-3e2a-4748-8462-555c36a57423"
api_8  = "3596ce97-ce45-4b5c-93ef-9f62d7877109"
api_9  = "7a8bb104-4cf2-43b3-9194-35f37b4c3576"
api_10 = "95df58fb-21d8-46a5-ae0a-d86c723f9071"


def website_urls():
    website_url_list = [
        
        "https://landmark-cases-impact-wwzwt0q.gamma.site/",
        "https://navigating-digital-lands-lpxrapl.gamma.site/",
        "https://privacy-security-insight-et5gafc.gamma.site/",
        "https://justice-reform-chronicle-k2yh2vs.gamma.site/",
        "https://ip-wars-shaping-innovati-ig7p4yj.gamma.site/",
        "https://media-impact-cases-8zuacwq.gamma.site/",
        "https://constitutional-landmarks-7ksjq7u.gamma.site/",
        "https://landmark-environmental-l-5q9f523.gamma.site/",
        "https://family-law-chronicles-wct9d99.gamma.site/",
        "https://corporate-legal-conseque-gstsnfs.gamma.site/",
    ]

   
    random_website = random.choice(website_url_list)

    return random_website

# print(website_urls())

def element_xpath():
    X_path_1 = """//*[@id="__next"]/div/div[4]/div/div/div/div/div/div/div/div/div[3]/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div/a/div/div/div"""
    X_path_2 = """ //*[@id="__next"]/div/div[3]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/a/div/div/div"""



