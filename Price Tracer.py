import requests
from bs4 import BeautifulSoup

class PriceTracer:
    def __init__(self ,  url):
        self.url = url
        self.user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
        self.response = requests.get(url=self.url, headers=self.user_agent).text
        self.soup = BeautifulSoup(self.response, 'lxml')

    def product_title(self):
        title = self.soup.find('span', {'id':'productTitle'})
        if title is not None:
            return title.text.strip()
        else:
            return " Tag Not Found"

    def product_price(self):
        price =self.soup.find("span", {"class": "a-price-whole"})
        if price is not None:
            return price.text
        else:
            return " Tag Not Found"


#device = PriceTracer(url ="https://www.amazon.in/Samsung-Smartphone-Titanium-Snapdragon-ProVisual/dp/B0DSKNQW8F/ref=sr_1_1_sspa?crid=1CP8C1PYXMWR&dib=eyJ2IjoiMSJ9.TSTIzp91Ds-y0dHIMXcN96_TeM4-RzDK-fLvPfUdOzVprt77OH_iSdTqQzJqw3sSZlgZVGAmblatN1wfvtVPsHr6d5HmAcovQzTt-CL_EL8ql9MnXC3IczB9UPZI63Nq8ULsXYLso-s2mIab40yRyqGigO357EqAc9y9xfvB7UGAua3BSYT2t_VgQkq-CpwqRbeSfYed8PVQYPvyELuaVZQcrb_jf9VrcwC1FeVEum4.dxFRlg4aErNt7kVaTtE3uEmPrV9TnoZbAUOrN7rkWTM&dib_tag=se&keywords=s24%2Bultra%2B256gb&qid=1761890948&sprefix=s24%2Caps%2C718&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")
#print(device.product_title())
#print(device.product_price())

device = PriceTracer(url = "https://www.amazon.in/iPhone-Pro-256-Promotion-Breakthrough/dp/B0FQFYYPZF/ref=sr_1_1_sspa?crid=VUUJFAIYAZEJ&dib=eyJ2IjoiMSJ9.n4-R94E3SRhBSa7osaRxSRY_5k20EyKxVxd1RIiEwuoMw_Xi8IW3e_jZ-V71Viy8j5gjufI-ONvVOX_HdRfcr5Iue5D6GJvJQX-DZAAy9mJ4SwnIsS4FmEs2qGMzh08A1us0fot2WTQ3dzOEkGj_fuUqAOruMPaRhDMyQMzdJXcxclUECX43ha4XmlTJzdHx0GLqyUxgbSzXs6TapyAHClSrcEUOmmLFFW4TICIlqDQ.HfO7DCYxE2M7RduQKubsCcvzEETJofsvSza0-JYSSx4&dib_tag=se&keywords=iphone&qid=1761896125&sprefix=i%2Caps%2C328&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")
print(device.product_title())
print(device.product_price())
