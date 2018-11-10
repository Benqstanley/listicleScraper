import requests
import requests
import lxml.html
import pandas
from bs4 import BeautifulSoup, NavigableString, Tag

def returnNext(tag):
    return tag.name == 'a' and tag.get('class') == ['next']
def returnContent(tag):
    return tag.name == 'div' and tag.get('class') == ['inner_content']

ListicleFirstPage = requests.get('http://www.factinate.com/interesting/30-facts-donald-glover-2/1?fact=1&utm_source=fbkd&utm_medium=dglover_d_cpc_us', auth=('[username]', '[password]'), verify=False)

List = []
ListicleFirstPageT = ListicleFirstPage.text
LFPsoup = BeautifulSoup(ListicleFirstPageT, "lxml")
Next = LFPsoup.find(returnNext)
NextAddress = Next.get('href')
FirstEntry = {}
if LFPsoup.find(returnContent) is not None:
    FirstEntry["Content"] = (LFPsoup.find(returnContent).text.replace("\n", " "))
j = 0
List.append(FirstEntry)
while Next is not None and 'dglover' in NextAddress:
    ListEntry = {}
    j = j+1
    ListicleNextPage = requests.get(NextAddress, auth=('[username]', '[password]'), verify=False)
    ListicleNextPageT = ListicleNextPage.text
    print("Working on page " + str(j) +"\n")
    LFPsoup = BeautifulSoup(ListicleNextPageT, "lxml")
    Next = LFPsoup.find(returnNext)
    if LFPsoup.find(returnContent) is not None:
       ListEntry["Content"] = (LFPsoup.find(returnContent).text.replace("\n", " "))
    NextAddress = Next.get('href')
    List.append(ListEntry)
print(List)
df = pandas.DataFrame(List)
df.to_csv("DonaldList.csv")
