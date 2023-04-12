# #1. Loading BeautifulSoup and test request
# import asyncio
# from bs4 import BeautifulSoup
# import ssl
# import requests
# from requests.adapters import HTTPAdapter
# from requests.packages.urllib3.poolmanager import PoolManager
# from requests.packages.urllib3.util import ssl_
#
#
# class TlsAdapter(HTTPAdapter):
#
#     def __init__(self, ssl_options=0, **kwargs):
#         self.ssl_options = ssl_options
#         super(TlsAdapter, self).__init__(**kwargs)
#
#     def init_poolmanager(self, *pool_args, **pool_kwargs):
#         CIPHERS = """ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:AES256-SHA"""
#         ctx = ssl_.create_urllib3_context(ciphers=CIPHERS, cert_reqs=ssl.CERT_REQUIRED, options=self.ssl_options)
#         self.poolmanager = PoolManager(*pool_args, ssl_context=ctx, **pool_kwargs)
#
#
# session = requests.session()
# adapter = TlsAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)
# session.mount("https://", adapter)
#
# async def load_flat_dicts(url, i):
#     print(i, 0)
#     cian_html = session.request('GET', url)
#     print(cian_html, i, 1)
#     return
#     soup = BeautifulSoup(cian_html[0].text, features="lxml")
#     print(cian_html.text[:1000])
#     flats_dict = {}
#     flats = soup.find_all('article', {'data-name': 'CardComponent'})
#     flats += soup.find_all('div', {'data-name': 'OfferCard'})
#     for f in flats:
#         flat_imgs = []
#
#         additional_imgs = f.find_all('img', {'data-name': 'GalleryImage'})
#         flat_imgs.append(f.find('img')['src'])
#
#         for fa in additional_imgs:
#             flat_imgs.append(fa['src'])
#
#         links = f.find_all('a', {'target': '_blank'})
#         for a in links:
#             if 'https://www.cian.ru/rent/flat/' or 'https://www.cian.ru/sale/flat/' in a['href']:
#                 if '/cat.php?' not in a['href']:
#                   flats_dict[a['href']] = flat_imgs
#                   break
#     return flats_dict
#
#
#
#
# loop = asyncio.get_event_loop()
# tasks = []
# for i in range(25):
#     tasks.append(loop.create_task(load_flat_dicts('https://www.cian.ru/sale/flat/278349187/', i)))
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
