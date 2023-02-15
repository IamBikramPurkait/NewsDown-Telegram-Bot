from google_drive_downloader import GoogleDriveDownloader as gdd
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import img2pdf
import html5lib  # (for parsing) pip install html5

today = datetime.now()
current_time = today.strftime("%H:%M")
paper_available_time = "07:00"
current_date = today.strftime("%d")
previous_date = str(int(current_date)-1)
current_month = today.strftime('%m')
current_year = today.strftime('%Y')


papers_link = {
    "TIMES OF INDIA": "https://dailyepaper.in/times-of-india-epaper-pdf-download-2023/",
    "STATESMAN": "https://dailyepaper.in/statesman-newspaper-today/",
    "TELEGRAPH": "https://dailyepaper.in/telegraph-newspaper/",
    "ECONOMIC TIMES": "https://dailyepaper.in/economic-times-newspaper-today/",
    "FINANCIAL EXPRESS": "https://dailyepaper.in/financial-express-newspaper/",
    "HINDU": "https://dailyepaper.in/hindu-analysis-notes-in-pdf-2023/",
    "TRIBUNE": "https://dailyepaper.in/the-tribune-epaper/",
    "DECCAN CHRONICLE": "https://dailyepaper.in/deccan-chronicle-epaper/",
    "NAVBHARAT": "https://dailyepaper.in/navbharat-times-epaper/",
    "DAINAIK BHASKAR": "https://dailyepaper.in/dainik-bhaskar-epaper/",
    "DAINIK JAGRAN": "https://dailyepaper.in/dainik-jagran-newspaper-download-2022/",
    "JANSATTA": "https://dailyepaper.in/jansatta-epaper-pdf/",
    "DAINIK NAVAJYOTI": "https://dailyepaper.in/dainik-navajyoti-epaper/",
    "RASHTRIYA SAHARA": "https://dailyepaper.in/rashtriya-sahara-epaper/",
    "RAJASTHAN PATRIKA": "https://dailyepaper.in/rajasthan-patrika-epaper/",
    "PUNJAB KESARI": "https://dailyepaper.in/punjab-kesari-epaper/",
    "PRABHAT KHABAR": "https://dailyepaper.in/prabhat-khabar-epaper/"
}


def paper_downloader(paper_name):
    if current_time <= paper_available_time:
        present_day = previous_date
        formatted_date = f"{previous_date}-{current_month}-{current_year}"
    else:
        present_day = current_date
        formatted_date = f"{current_date}-{current_month}-{current_year}"
    present_month = str(today.strftime("%b"))
    today_tag_text = f"{present_day} {present_month} {current_year}: Download Now"

    r = requests.get(papers_link.get(paper_name))
    # If this line causes an error, run 'pip install html5lib'
    soup = BeautifulSoup(r.content, 'html5lib')

    def get_link(today_tag_text):
        for tag in soup.find_all('span'):
            if (tag.text == today_tag_text):
                pdf_link = tag.a['href']
                return pdf_link

    link = get_link(today_tag_text)

    if "bit.ly" in link:
        resp = requests.get(link)
        file_id = resp.url.split('/')[5]
    else:
        file_id = link.split('/')[5]
    gdd.download_file_from_google_drive(file_id=file_id,
                                        dest_path=f"./paper/{formatted_date} {paper_name}.pdf", showsize=True, overwrite=True)
    return f"./paper/{formatted_date} {paper_name}.pdf"


def anandabazar(paper_name):
    if current_time <= paper_available_time:
        finaltime = previous_date+current_month+current_year
        formatted_date = f"{previous_date}-{current_month}-{current_year}"
        present_date = previous_date
    else:
        finaltime = current_date+current_month+current_year
        formatted_date = f"{current_date}-{current_month}-{current_year}"
        present_date = current_date

    r = requests.get(
        # f"https://epaper.anandabazar.com/calcutta/{year}-{month}-{date}/71/Page-1.html")
        # f"https://epaper.telegraphindia.com/calcutta/{year}-{month}-{date}/71/Page-1.html")
        f"https://epaper.{paper_name.lower()}.com/calcutta/{current_year}-{current_month}-{present_date}/71/Page-1.html")

    # If this line causes an error, run 'pip install html5lib'
    soup = BeautifulSoup(r.content, 'html5lib')
    text = soup.find('input', attrs={'id': 'totalpages'})
    page_no = int(text['value'])

    url = f"https://epaper.{paper_name.lower()}.com/epaperimages////{finaltime}////{finaltime}-md-hr-"
    lst = []
    for i in range(1, page_no+1):
        lst.append(url+f"{i}ll.png")

    with open(f"./paper/{formatted_date} {paper_name}.pdf", "wb") as f:
        f.write(img2pdf.convert([requests.get(i).content for i in lst]))

    return f.name


def ekdin(paper_name):
    if current_time <= paper_available_time:
        date_stamp = f"{previous_date}-{current_month}-{current_year}"
        formatted_date = f"{previous_date}-{current_month}-{current_year}"
    else:
        date_stamp = f"{current_date}-{current_month}-{current_year}"
        formatted_date = f"{current_date}-{current_month}-{current_year}"
    year_month_stamp = today.strftime('%Y-%m')

    link = f"https://www.ekdin-epaper.com/media/{year_month_stamp}/ekdin-{date_stamp}.pdf"
    response = requests.get(link)
    with open(f"./paper/{formatted_date} {paper_name}.pdf", "wb") as f:
        f.write(response.content)
    return f.name


def pioneer(paper_name):
    if current_time <= paper_available_time:
        date_stamp = f"{current_year}-{current_month}-{previous_date}"
        formatted_date = f"{previous_date}-{current_month}-{current_year}"
    else:
        date_stamp = f"{current_year}-{current_month}-{current_date}"
        formatted_date = f"{current_date}-{current_month}-{current_year}"

    link = f"https://www.dailypioneer.com/uploads/{current_year}/epaper/february/delhi-{paper_name.lower().split('-')[1]}-edition-{date_stamp}.pdf"

    response = requests.get(link)
    with open(f"./paper/{formatted_date} {paper_name}.pdf", "wb") as f:
        f.write(response.content)
    return f.name


def ajitjalandhar(paper_name):
    if current_time <= paper_available_time:
        # finaltime = previous_date+current_month+current_year
        formatted_date = f"{previous_date}-{current_month}-{current_year}"
        present_date = previous_date
    else:
        # finaltime = current_date+current_month+current_year
        formatted_date = f"{current_date}-{current_month}-{current_year}"
        present_date = current_date

    # r = requests.get(
    #     # f"https://static.ajitjalandhar.com/pages/20230215/1/1/1_page.jpg")
    #     # f"https://epaper.telegraphindia.com/calcutta/{year}-{month}-{date}/71/Page-1.html")
    #     f"https://static.ajitjalandhar.com/pages/{current_year}{current_month}{present_date}/1/1/1_page.jpg")

    # # If this line causes an error, run 'pip install html5lib'
    # soup = BeautifulSoup(r.content, 'html5lib')
    # text = soup.find('input', attrs={'id': 'totalpages'})
    # page_no = int(text['value'])

    # "https://static.ajitjalandhar.com/pages/20230215/1/1/1_page.jpg"
    url = f"https://static.ajitjalandhar.com/pages/{current_year}{current_month}{present_date}/1/"
    lst = []
    for i in range(1, 16):
        lst.append(url+f"{i}/{i}_page.jpg")

    with open(f"./paper/{formatted_date} {paper_name}.pdf", "wb") as f:
        f.write(img2pdf.convert([requests.get(i).content for i in lst]))
