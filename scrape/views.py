from django.shortcuts import render

# Create your views here.
import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse

def apple(request):
    url = "https://www.gsmarena.com.bd/apple/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    phones = []

    product_containers = soup.find_all('div', class_='product-thumb')
    for container in product_containers:
        name = container.find('div', class_='mobile_name').text
        image = container.find('img', class_='img-responsive')['src']
        price = container.find('div', class_='mobile_price').text
        
        phones.append({
            'name': name,
            'image': image,
            'price': price
        })

    return JsonResponse(phones, safe=False)


def xiaomi(request):
    base_url = "https://www.gsmarena.com.bd/xiaomi/"
    current_page_url = base_url
    phones = []

    while current_page_url:
        response = requests.get(current_page_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        product_containers = soup.find_all('div', class_='product-thumb')
        for container in product_containers:
            name = container.find('div', class_='mobile_name').text
            image = container.find('img', class_='img-responsive')['src']
            price = container.find('div', class_='mobile_price').text
            
            phones.append({
                'name': name,
                'image': image,
                'price': price
            })

        # Find the next page link
        pagination = soup.find('ul', class_='pagination')
        next_page = pagination.find('a', text='»')
        if next_page:
            current_page_url = next_page['href']
        else:
            current_page_url = None

    return JsonResponse(phones, safe=False)
