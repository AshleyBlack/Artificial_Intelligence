import re
from urllib.request import urlopen
from lxml import html
import requests
from pyknow import *


class TrainTickets(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(action="route")

    @Rule(Fact(action='route'),
          NOT(Fact(departing_station=W())))
    def departure(self):
        self.declare(Fact(departing_station='Norwich'))
        
    @Rule(Fact(action='route'),
          NOT(Fact(arriving_station=W())))
    def arrival(self):
        self.declare(Fact(arriving_station='London'))

    @Rule(Fact(action='route'),
          NOT(Fact(time=W())))
    def time(self):
        self.declare(Fact(time='09:00'))

    @Rule(Fact(action='route'),
          NOT(Fact(date=W())))
    def date(self):
        self.declare(Fact(date='2018-11-21'))

    @Rule(Fact(action='route'),
          Fact(departing_station=MATCH.departing_station),
          Fact(arriving_station=MATCH.arriving_station),
          Fact(time=MATCH.time),
          Fact(date=MATCH.date))
    def route(self, departing_station, arriving_station, time, date):
        url = "https://traintimes.org.uk/" + departing_station + "/" + arriving_station + "/" + time + "/" + date
        page = requests.get(url)
        tree = html.fromstring(page.content)
        if 'a' in time:
            time = time.replace('a', '')
            print(departing_station + ' to ' + arriving_station + ' arriving at ' + time + ' on ' + date)
        else:
            print(departing_station + ' to ' + arriving_station + ' departing at ' + time + ' on ' + date)
        for x in range(5):
            printout = ''
            times = tree.xpath('//li[@id="result' + str(x) + '"]/strong[1]/text()')
            printout = printout + re.sub('[\[\'\]' ']', '', str(times))
            platform_temp = tree.xpath('//li[@id="result' + str(x) + '"]/small/em/text()')
            platform_temp = str(platform_temp).replace('\\n', '').replace('\\t', '').replace('Platform', 'Platform ')\
                .replace(';', ' ')
            platform = re.sub('[^a-zA-Z\d\s:]', '', str(platform_temp))
            if platform_temp:
                printout = printout + ' ' + platform + ' '
            else:
                printout = printout + '             '
            price = tree.xpath('//li[@id="result'+ str(x) + '"]/small[2]/span[@class="tooltip" and 1]/text()')
            printout = printout + re.sub('[\[\'\]' ']', '', str(price))
            print(printout)


engine = TrainTickets()
engine.reset()  # Prepare the engine for the execution.
engine.run()  # Run it!
