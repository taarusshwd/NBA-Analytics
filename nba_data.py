from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.basketball-reference.com/leagues/NBA_2021_totals.html"
source = requests.get(url).text

soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())

csv_file = open('nba_totals_2021.csv', 'w', encoding="utf-8")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Player', 'Position', 'Age', 'Games', 'GS', 'MP', 'FG', 'FGA', 'FG_PCT', 'FG3', 'FG3A', 'FG3_PCT', 'FG2', 'FG2A', 'FG2_PCT', 'EFG_PCT', 'FT', 'FTA', 'FT_PCT', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS'])


for article in soup.find('div', id='div_totals_stats').table.tbody.find_all('tr', class_=["full_table"]) :
    #index = article.find('th').text
    #print(index)
    name = article.find('td', attrs={"data-stat":"player"}).a.text
    #print(name)
    pos = article.find('td', attrs={"data-stat":"pos"}).text
    #print(pos)
    age = article.find('td', attrs={"data-stat":"age"}).text
    #print(age)
    #team = article.find('td', attrs={"data-stat":"team_id"}).a.text
    #print(team)
    g = article.find('td', attrs={"data-stat":"g"}).text
    #print(g)
    gs = article.find('td', attrs={"data-stat":"gs"}).text
    #print(gs)
    mp = article.find('td', attrs={"data-stat":"mp"}).text
    #print(mp)
    fg = article.find('td', attrs={"data-stat":"fg"}).text
    #print(fg)
    fga = article.find('td', attrs={"data-stat":"fga"}).text
    #print(fga)
    fg_pct = article.find('td', attrs={"data-stat":"fg_pct"}).text
    #print(fg_pct)
    fg3 = article.find('td', attrs={"data-stat":"fg3"}).text
    #print(fg3)
    fg3a = article.find('td', attrs={"data-stat":"fg3a"}).text
    #print(fg3a)
    fg3_pct = article.find('td', attrs={"data-stat":"fg3_pct"}).text
    #print(fg3_pct)
    fg2 = article.find('td', attrs={"data-stat":"fg2"}).text
    #print(fg2)
    fg2a = article.find('td', attrs={"data-stat":"fg2a"}).text
    #print(fg2a)
    fg2_pct = article.find('td', attrs={"data-stat":"fg2_pct"}).text
    #print(fg2_pct)
    efg_pct = article.find('td', attrs={"data-stat":"efg_pct"}).text
    #print(efg_pct)
    ft = article.find('td', attrs={"data-stat":"ft"}).text
    #print(ft)
    fta = article.find('td', attrs={"data-stat":"fta"}).text
    #print(fta)
    ft_pct = article.find('td', attrs={"data-stat":"ft_pct"}).text
    #print(ft_pct)
    orb = article.find('td', attrs={"data-stat":"orb"}).text
    #print(orb)
    drb = article.find('td', attrs={"data-stat":"drb"}).text
    #print(drb)
    trb = article.find('td', attrs={"data-stat":"trb"}).text
    #print(trb)
    ast = article.find('td', attrs={"data-stat":"ast"}).text
    #print(ast)
    stl = article.find('td', attrs={"data-stat":"stl"}).text
    #print(stl)
    blk = article.find('td', attrs={"data-stat":"blk"}).text
    #print(blk)
    tov = article.find('td', attrs={"data-stat":"tov"}).text
    #print(tov)
    pf = article.find('td', attrs={"data-stat":"pf"}).text
    #print(pf)
    pts = article.find('td', attrs={"data-stat":"pts"}).text
    #print(pts)
    csv_writer.writerow([name, pos, age, g, gs, mp, fg, fga, fg_pct, fg3, fg3a, fg3_pct, fg2, fg2a, fg2_pct, efg_pct, ft, fta, ft_pct, orb, drb, trb, ast, stl, blk, tov, pf, pts])

csv_file.close()

#trial1 = article.find_all('div')

#print(article)