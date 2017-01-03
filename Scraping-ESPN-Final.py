import requests
from bs4 import BeautifulSoup as BS

def scrape():

	url = "http://www.espncricinfo.com/ci/engine/match/index.html?view=live"
	r=requests.get(url)
	soup=BS(r.text, "html.parser")
	tableHeads=soup.find_all('div', {'class' : 'match-section-head'})
	tableData=soup.find_all('section', {'class' : 'matches-day-block'})

	print "\n" + "*"*100
	print "Welcome to Live Cricket Scores Terminal App v1.0 by Navjot Singh"
	print "\nHere are the events going on live right now: "

	for ix in range(0,len(tableHeads)):
		print "\t" + str(ix+1) + ". " + str(tableHeads[ix].h2.text)

	ch=input("\nChoose the event for which you wish to check out the matches (Press 0 to See All): ")

	if ch>0:
		matches=tableData[ch-1].find_all('section', {'class' : 'default-match-block'})
	elif ch>len(tableData):
		print "Sorry. Invalid Input. Please run the terminal app again!"
		exit(0)
	else:
		matches=tableData[0].find_all('section', {'class' : 'default-match-block'})
		for ix in range(1, len(tableData)):
			matches = matches + tableData[ix].find_all('section', {'class':'default-match-block'})

	for ix in range(0,len(matches)):
		
		matchDetails=matches[ix].find_all('div')
		
		team1= str(matchDetails[1].text.split('\n',1)[1].split(' ')[0])
		if len(str(matchDetails[1].text.split('\n',1)[1].split(' ')[1]))>0:
			team1 = team1 + " " + str(matchDetails[1].text.split('\n',1)[1].split(' ')[1])
		score1= str(matchDetails[1].find('span').text)
		if len(str(matchDetails[1].text.split('\n',1)[1].split(' ')[2]))>0:
			team1 = team1 + " " + str(matchDetails[1].text.split('\n',1)[1].split(' ')[2])
		score2= str(matchDetails[2].find('span').text)
		
		team2= str(matchDetails[2].text.split('\n',1)[1].split(' ')[0])
		if len(str(matchDetails[2].text.split('\n',1)[1].split(' ')[1]))>0:
			team2 = team2 + " " + str(matchDetails[2].text.split('\n',1)[1].split(' ')[1])
		if len(str(matchDetails[2].text.split('\n',1)[1].split(' ')[2]))>0:
			team2 = team2 + " " + str(matchDetails[2].text.split('\n',1)[1].split(' ')[2])

		headerline = "Match " + str(ix+1) + ": " + team1 + " vs " + team2
		if len(headerline)<40:
			headerline += (" "*(40-len(headerline)))
		print "\n" + headerline + "\t\t(" + str(matchDetails[0].find('span', {'class':'bold'}).text) +")"
		print str(matchDetails[0].find('span', class_='match-no').a.text.split('     ',1)[1])
		print "\t" + team1 + ": " + score1 + "\n\t" + team2 + ": " + score2
		print "\n" + matchDetails[3].text.split('\n')[1]
		print "_"*50

	ch=input("\nChoose the event for which you wish to see the whole scorecard (Press 0 to Exit): ")

	if(ch==0):
		sys.exit(0)
	else:
		url2="http://www.espncricinfo.com" + matches[ch-1].find_all('div')[4].find_all('a')[0]['href'] + "?view=scorecard"

	print "\n" + "*"*100

	r=requests.get(url2)
	soup=BS(r.text, "html.parser")

	matchDetails=matches[ch-1].find_all('div')
	team1= str(matchDetails[1].text.split('\n',1)[1].split(' ')[0])
	if len(str(matchDetails[1].text.split('\n',1)[1].split(' ')[1]))>0:
		team1 = team1 + " " + str(matchDetails[1].text.split('\n',1)[1].split(' ')[1])
	score1= str(matchDetails[1].find('span').text)
	if len(str(matchDetails[1].text.split('\n',1)[1].split(' ')[2]))>0:
		team1 = team1 + " " + str(matchDetails[1].text.split('\n',1)[1].split(' ')[2])
	score2= str(matchDetails[2].find('span').text)

	team2= str(matchDetails[2].text.split('\n',1)[1].split(' ')[0])
	if len(str(matchDetails[2].text.split('\n',1)[1].split(' ')[1]))>0:
		team2 = team2 + " " + str(matchDetails[2].text.split('\n',1)[1].split(' ')[1])
	if len(str(matchDetails[2].text.split('\n',1)[1].split(' ')[2]))>0:
		team2 = team2 + " " + str(matchDetails[2].text.split('\n',1)[1].split(' ')[2])

	print soup.find('div', {'class':'match-information-strip'}).text.split('      ', 1)[1].split(',',1)[0] + soup.find('div', {'class':'match-information-strip'}).text.split('      ', 1)[1].split(',',1)[1]
	print "\t" + team1 + ": " + score1 + "\n\t" + team2 + ": " + score2
	print "\n" + matchDetails[3].text.split('\n')[1] + "\n"

	inningsBat = soup.find_all('table', {'class':'batting-table innings'})

	rows = soup.find_all('tr')

	#inningsBowl = soup.find_all('table', {'class':'bowling-table'})

	for ix in range(0, len(inningsBat)):
		print "-"*100
		
		rows = inningsBat[ix].find_all('tr')

		inningHead = rows[0].find_all('th')[1].text.split('innings', 1)[0] + 'Innings'
		if len(inningHead) < 60:
			inningHead += " "*(60-len(inningHead))
		print "\n" + inningHead + "\t" + "Runs" + "\t"+ "Balls" + "\t" + "Strike Rate" + "\n"

		for px in range(1, len(rows)-2, 2):
			playerData = rows[px].find_all('td')
			playerName = playerData[1].text
			if len(playerName)<25:
				playerName += " "*(25-len(playerName))
			dismissalMode = playerData[2].text
			if len(dismissalMode)<35:
				dismissalMode += " "*(35-len(dismissalMode))
			runs = playerData[3].text
			if len(runs)<4:
				runs += " "*(4-len(runs))
			balls = playerData[len(playerData)-4].text
			if len(balls)<5:
				balls += " "*(5-len(balls))
			print playerName + dismissalMode + "\t" + runs + "\t" + balls + "\t" + playerData[len(playerData)-1].text

		playerData = rows[len(rows)-2].find_all('td')
		playerName = playerData[1].text
		playerName += " "*(25-len(playerName))
		dismissalMode = playerData[2].text
		if len(dismissalMode)<35:
			dismissalMode += " "*(35-len(dismissalMode))
		runs = playerData[3].text
		if len(runs)<4:
			runs += " "*(4-len(runs))
		print "\n" + playerName + dismissalMode + "\t" + runs

		playerData = rows[len(rows)-1].find_all('td')
		playerName = playerData[1].text
		playerName += " "*(25-len(playerName))
		dismissalMode = playerData[2].text
		if len(dismissalMode)<35:
			dismissalMode += " "*(35-len(dismissalMode))
		runs = playerData[3].text
		if len(runs)<4:
			runs += " "*(4-len(runs))
		print playerName + dismissalMode + "\t" + runs + "\t" + playerData[4].text

		########################################################
		print "-"*20
	'''
		rows = inningsBowl[ix].find_all('tr')

		inningHead = rows[0].find_all('th')[1].text
		if len(inningHead) < 30:
			inningHead += " "*(30-len(inningHead))
		print "\n" + inningHead + "\t\t" + "Overs" + "\t\t"+ "Runs" + "\t\t" + "Wickets" + "\t\t" + "Economy" + "\n"
		
		for px in range(1, len(rows), 2):
			playerData = rows[px].find_all('td')
			playerName = playerData[1].text
			if len(playerName)<30:
				playerName += " "*(30-len(playerName))
			overs = playerData[2].text
			if len(overs)<5:
				overs += " "*(5-len(overs))
			runs = playerData[4].text
			if len(runs)<4:
				runs += " "*(4-len(runs))
			wickets = playerData[5].text
			if len(wickets)<6:
				wickets += " "*(6-len(wickets))
			economy = playerData[6].text
			print playerName + "\t" + overs + "\t\t" + runs + "\t\t" + balls + "\t\t" + playerData[len(playerData)-1].text'''

if __name__ == '__main__':
	scrape()