import requests
from bs4 import BeautifulSoup
import inquirer
from progress.spinner import Spinner

page = requests.get('https://xzn.ir/discount-code')

slices = BeautifulSoup(page.text, 'html.parser').find_all('div', {'class': 'wof-slice'})
slices_text = [slice.get_text() for slice in slices]

questions = [
  inquirer.List('segment',
                message="which one ?",
                choices=slices_text,
            ),
]
answer = inquirer.prompt(questions)['segment']

slice_id = int(slices[slices_text.index(answer)]['data-slice'])

headers = {
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
}
body = "action=wof-email-optin&id=3363&seq=TGVLSkpnaE9ySXdxdm84aDdUM3ZHTlJSWnQ0a0Q5YXYvVnQva0d3Y3JWOD0%3D&pseq=TGVLSkpnaE9ySXdxdm84aDdUM3ZHTlJSWnQ0a0Q5YXYvVnQva0d3Y3JWOD0%3D&nonce=3953b4c0c0"


sp = Spinner('Please wait...')
while True:
    sp.next()
    result = requests.post(
        'https://xzn.ir/wp-admin/admin-ajax.php', data=body, headers=headers)

    data = result.json()['data']

    if data['segment'] == slice_id:
        print("\n\rYour code: ", data['value'])
        sp.finish()
        break
