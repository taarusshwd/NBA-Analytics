import requests
from bs4 import BeautifulSoup
import csv
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    '--year',
    '-year',
    default= 2021,
    help = 'Enter the NCAA Season'
)

args = parser.parse_args()
year = args.year

#limit = (year==2021) if 26 else 25

csv_file = open("ncaa_totals_2021.csv", 'w', encoding = 'utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['No.', "Players", "Team", "GP", "MIN", "FGM", "FGA", "FG%", "3PM", "3PA", "3P%", "FTM", "FTA", "FT%", "TOV", "PF", "ORB", "DRB", "REB", "AST", "STL", "BLK", "PTS"])

for page in range(1, 26):

    url = f"https://basketball.realgm.com/ncaa/stats/{year}/Totals/Qualified/All/Season/All/points/desc/{page}"

    source = requests.get(url)
    soup = BeautifulSoup(source.content, 'lxml')

    for article in soup.find('div', class_='main-container').table.tbody.find_all('tr'):
        index = article.find_all('td')[0].text
        name = article.find_all('td')[1].text
        Team = article.find_all('td')[2].text
        GP = article.find_all('td')[3].text
        MIN = article.find_all('td')[4].text
        FGM = article.find_all('td')[5].text
        FGA = article.find_all('td')[6].text
        FGpct = article.find_all('td')[7].text
        ThreePM = article.find_all('td')[8].text
        ThreePA = article.find_all('td')[9].text
        ThreePpct = article.find_all('td')[10].text
        FTM = article.find_all('td')[11].text
        FTA = article.find_all('td')[12].text
        FTpct = article.find_all('td')[13].text
        TOV = article.find_all('td')[14].text
        PF = article.find_all('td')[15].text
        ORB = article.find_all('td')[16].text
        DRB = article.find_all('td')[17].text
        REB = article.find_all('td')[18].text
        AST = article.find_all('td')[19].text
        STL = article.find_all('td')[20].text
        BLK = article.find_all('td')[21].text
        PTS = article.find_all('td')[22].text

        csv_writer.writerow([index, name, Team, GP, MIN, FGM, FGA, FGpct, ThreePM, ThreePA, ThreePpct, FTM, FTA, FTpct, TOV, PF, ORB, DRB, REB, AST, STL, BLK, PTS])

        #print(index + " " + name + " " + Team + " " + GP + " " + MIN + " " + FGM + " " + FGA + " " + FGpct + " " + ThreePM + " " + ThreePA + " " + ThreePpct + " " + FTM + " " + FTA + " " + FTpct + " " + TOV + " " + PF + " " + ORB + " " + DRB + " " + REB + " " + AST + " " + STL + " " + BLK + " " + PTS)


csv_file.close()