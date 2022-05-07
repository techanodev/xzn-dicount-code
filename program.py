import requests
from bs4 import BeautifulSoup

page = requests.get('https://xzn.ir/discount-code')

soup = BeautifulSoup(page.text, 'html.parser')
for slice in soup.find_all('div', {'class': 'wof-slice'}):
    print(slice['data-slice'], '.', slice.get_text())

slice_id = int(input('Enter slice id: '))

headers = {
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
}
body = "action=wof-email-optin&id=3363&seq=TGVLSkpnaE9ySXdxdm84aDdUM3ZHTlJSWnQ0a0Q5YXYvVnQva0d3Y3JWOD0%3D&pseq=TGVLSkpnaE9ySXdxdm84aDdUM3ZHTlJSWnQ0a0Q5YXYvVnQva0d3Y3JWOD0%3D&nonce=3953b4c0c0"

i = 0
while True:
    i += 1
    result = requests.post(
        'https://xzn.ir/wp-admin/admin-ajax.php', data=body, headers=headers)

    data = result.json()['data']
    print(i, data['segment'])
    if data['segment'] == slice_id:
        print(data['value'])
        break
