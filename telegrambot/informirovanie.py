from bs4 import BeautifulSoup
import requests
from docxtpl import DocxTemplate
from tkinter import *

import tkinter.filedialog as fd

def clicked( tema, dol, zvan, UFIO, Ndol, group, NZvan, NFio):
    filename = "шаблон.docx"
    doc = DocxTemplate(filename)
    str_arr = [""]

    if tema == "Новости Орла и Орловской области":
        URL = "https://oreltimes.ru"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
        full_page = requests.get(URL, headers=headers)
        soups = BeautifulSoup(full_page.content, "html.parser")
        def f(url=""):
            full_page = requests.get(url, headers=headers)
            soupik = BeautifulSoup(full_page.content, "html.parser")
            title = soupik.find("h1", {"class": "entry-title"})
            print(title.text)
            str_arr.append(title.text)
            text = ""
            for st in soupik.findAll("p", {"style": "text-align: justify;"}):
                text += st.text
            str_arr.append(text)
        counter = 0
        for href in soups.findAll("a", {"class": "link-img"}):
            f(href["href"])
            counter += 1
            if (counter == 5):
                break

    elif tema == "Военно-политическая обстановка в мире":
        URL = "https://www.mk.ru/politics/army"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
        full_page = requests.get(URL, headers=headers)
        soups = BeautifulSoup(full_page.content, "html.parser")
        str_arr = [""]

        def f(url=""):
            try:
                full_page = requests.get(url, headers=headers)
                soupik = BeautifulSoup(full_page.content, "html.parser")
                title = soupik.find("h1", {"class": "article__title", "itemprop": "headline"})
                str_arr.append(title.text)
                print(title.text)
                text = soupik.find("div", {"class": "article__description", "itemprop": "description"})
                text2 = soupik.find("div", {"class": "article__body", "itemprop": "articleBody"})
                full_text = text.text + text2.text
                str_arr.append(full_text)
            except:
                print("Нейросеть обработала эту новость и она не подходит")

        counter = 0
        for href in soups.findAll("a", {"href": re.compile(".html"), "class": "listing-preview__content"}):
            f(href["href"])
            counter += 1
            if (counter == 5):
                break
    elif tema == "Новости культуры и спорта":
        URL = "https://www.culture.ru/news"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
        full_page = requests.get(URL, headers=headers)
        soups = BeautifulSoup(full_page.content, "html.parser")

        def f(url=""):
            full_page = requests.get(url, headers=headers)
            soupik = BeautifulSoup(full_page.content, "html.parser")
            title = soupik.find("h1", {"class": "entity-heading_title"})
            str_arr.append(title.text)
            print(title.text)
            full_text = ""
            for text in soupik.find("div", {"class": "styled-content_body"}).findAll("p", recursive=False):
                full_text += text.text
            str_arr.append(full_text)
        counter = 0
        for href in soups.findAll("a", {"class": "card-heading_title-link"}):
            f("https://www.culture.ru" + href["href"])
            counter += 1
            if (counter == 5):
                break

    elif tema == "Актуальные вопросы военной службы, новинки российской военной техники и вооружения":
        URL2 = "https://rg.ru/tema/sila/vooruzhenie/"
        URL = "https://rg.ru"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
        full_page = requests.get(URL2, headers=headers)
        soups = BeautifulSoup(full_page.content, "html.parser")
        str_arr = [""]
        print(str_arr)
        def f(dopurl=""):
            full_page = requests.get(URL + dopurl, headers=headers)
            soup = BeautifulSoup(full_page.content, "html.parser")
            title = soup.find("h1")
            title_str = str(title)
            print(title_str)
            title_str = title_str.replace("<h1 class=\"b-material-head__title\"> ", "")
            title_str = title_str.replace("</h1>", "")
            Text_str = ""
            str_arr.append(title_str)
            for child in soup.findAll("p"):
                str1 = str(child)
                k = 0
                for i in range(0, len(str1)):
                    if (str1[i] == '<'):
                        k = 1
                    elif (str1[i] == '>'):
                        k = 0
                    elif (k == 0):
                        Text_str += str1[i]
            str_arr.append(Text_str)
            print("Найс")
        j = 0
        for a in soups.findAll("a", {"href": re.compile(".html"), "class": "b-link b-link_title"}):
            j += 1
            print(URL + a["href"])
            f(a["href"])
            if (j == 5):
                break
    elif tema == "Социально-экономическая жизнь общества":
        URL = "https://www.mk.ru/economics"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
        full_page = requests.get(URL, headers=headers)
        soups = BeautifulSoup(full_page.content, "html.parser")
        str_arr = [""]
        def f(url=""):
            full_page = requests.get(url, headers=headers)
            soupik = BeautifulSoup(full_page.content, "html.parser")
            title = soupik.find("h1", {"class": "article__title", "itemprop": "headline"})
            str_arr.append(title.text)
            text = soupik.find("div", {"class": "article__description", "itemprop": "description"})
            text2 = soupik.find("div", {"class": "article__body", "itemprop": "articleBody"})
            full_text = text.text + text2.text
            str_arr.append(full_text)
        counter = 0
        for href in soups.findAll("a", {"href": re.compile(".html"), "class": "listing-preview__content"}):
            f(href["href"])
            print(href["href"])
            counter += 1
            if (counter == 5):
                break
    elif tema == "Новости информационных технологий":
        URL = "https://www.it-world.ru/tech/news/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
        full_page = requests.get(URL, headers=headers)
        soups = BeautifulSoup(full_page.content, "html.parser")
        def f(url=""):
            full_page = requests.get(url, headers=headers)
            soupik = BeautifulSoup(full_page.content, "html.parser")
            title = soupik.find("h1", {"class": "detail"})
            print(title.text)
            str_arr.append(title.text)
            text = ""
            counter = 0
            print(soupik.findAll("p", {"class": ""}).__sizeof__())
            for st in soupik.findAll("p", {"class": ""}):
                if(counter == soupik.findAll("p", {"class": ""}).__sizeof__()-2):
                    break
                text += st.text
                counter += 1
            str_arr.append(text)
        counter = 0
        for href in soups.findAll("div", {"class": "card__img"}):
            for href in soups.findAll("div", {"class": "card__img"})[counter]:
                f("https://www.it-world.ru" + href["href"])
                print("https://www.it-world.ru" + href["href"])
            counter += 1
            if (counter == 5):
                break

    URL22 = "https://yandex.by/news/?from=index"
    headers2 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
    full_page2 = requests.get(URL22, headers=headers2)
    soups2 = BeautifulSoup(full_page2.content, "html.parser")
    j = 0
    for st in soups2.findAll("h2"):
        str_arr.append(st.text)
        if (j == 10):
            break

    context = {'Должность': dol,
               'Звание': zvan,
               'ФИО_утверждающего': UFIO,
               'должность_написавшего': Ndol,
               'номер_группы': group,
               'звание_написавшего': NZvan,
               'ФИО_написавшего': NFio,
               'tema': tema,
               'Title_main_1': str_arr[1],
               'text_main_1': str_arr[2],
               'Title_main_2': str_arr[3],
               'text_main_2': str_arr[4],
               'Title_main_3': str_arr[5],
               'text_main_3': str_arr[6],
               'Title_main_4': str_arr[7],
               'text_main_4': str_arr[8],
               'Title_main_5': str_arr[9],
               'text_main_5': str_arr[10],
               'Title_oper_1': str_arr[11],
               'Title_oper_2': str_arr[12],
               'Title_oper_3': str_arr[13],
               'Title_oper_4': str_arr[14],
               'Title_oper_5': str_arr[15],
               'Title_oper_6': str_arr[16],
               'Title_oper_7': str_arr[17],
               'Title_oper_8': str_arr[18],
               'Title_oper_9': str_arr[19],
               'Title_oper_10': str_arr[20]
               }
    doc.render(context)
    filename = "информирование.docx"
    doc.save(filename)
