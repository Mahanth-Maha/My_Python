# info that u dont care :
# Author : https://github.com/Mahanth-Maha
# Cause : Boredom
# Language : Nagin

import re
import sys
import argparse
import subprocess
try:
    import pandas as pd
    from bs4 import BeautifulSoup
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pandas"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "beautifulsoup4"])
finally:
    import pandas as pd
    from bs4 import BeautifulSoup

def main(args):
    with open(args.file, "r") as f:
        soup = BeautifulSoup(f, "html.parser")

    Avengers = []
    movie_name = ''
    # Find all question panels
    question_panels = soup.find_all("div", class_="question-pnl")

    for panel in question_panels:
        question_number = panel.find("td", class_="bold").text.strip().split(".")[1]
        
        The_core_of_multiverse = panel.find("table", class_="menu-tbl")
        menu_text = panel.find("table", class_="menu-tbl").text
        results = {}
        for row in The_core_of_multiverse.findAll('tr'):
            aux = row.findAll('td')
            results[aux[0].string] = aux[1].string
        question_id = question_status =  question_chosen = ""
        for k,v in results.items():
            if "ID" in k:
                question_id = v
            elif "Status" in k:
                question_status = v
            elif "Chosen" in k:
                question_chosen = v        
        Nat_Answer = ''
        Option_A_ID = ''
        Option_B_ID = ''
        Option_C_ID = ''
        Option_D_ID = ''
        MCQ_Answer = ''
        MSQ_Answer = ''
        Answered_Options = ''
        Marvel_Jesus = ''
        
        question_table = panel.find("table", class_="questionRowTbl")
        
        image_tags = panel.find_all('img')
        Marvel_Jesus = image_tags[0]['src'].split('_')[-1].split('.')[0]
        if 'NAT' in menu_text:
            question_type = "NAT"
            if 'Not Answered' not in menu_text:
                l = question_table.find("tr", class_ = "bold", text="Given Answer")
                last_row = question_table("tr")[-1]
                Nat_Answer = (last_row.findAll('td')[1].contents)[0]
                Answered_Options  = Nat_Answer
        else:
            image_tags = panel.find_all('img')
            tags = ["A","B","C","D"]
            ids = {}
            for i,option in enumerate(image_tags[1:]):
                ids[tags[i]] = option['src']
            
            Option_A_ID = ids['A'].split('_')[-1].split('.')[0]
            Option_B_ID = ids['B'].split('_')[-1].split('.')[0]
            Option_C_ID = ids['C'].split('_')[-1].split('.')[0]
            Option_D_ID = ids['D'].split('_')[-1].split('.')[0]
            
            if 'MCQ' in menu_text:
                question_type = "MCQ"
                if 'Not Answered' not in menu_text:
                    MCQ_Answer = question_chosen
                    Answered_Options = ids[MCQ_Answer].split('_')[-1].split('.')[0][-1].upper()
                
            elif 'MSQ' in menu_text:
                if 'Not Answered' not in menu_text:
                    question_type = "MSQ"
                    MSQ_Answer = question_chosen
                    Answered_Options_list = []
                
                    for i in tags:
                        if i in MSQ_Answer:
                            Answered_Options_list.append(ids[i].split('_')[-1].split('.')[0][-1].upper())
                    Answered_Options_list.sort()                  
                    Answered_Options = ",".join(Answered_Options_list)
            else :
                raise ValueError("I don't know, it F-ed up")
        
        jukega = Marvel_Jesus[0:3].upper()

        nahi = re.search(r"q(\d+)$", Marvel_Jesus).group(1)
        
        if "GA" in jukega:
            Peter_pAkaaar = int(nahi)
            nahi = "0" * (2 - len(nahi)) + nahi
        else:
            movie_name = jukega 
            Peter_pAkaaar = int(nahi) + 0
            
        pushpa =  jukega + "-" + nahi
        
        SuperHeroes = [question_number, question_type, question_id, question_status,MCQ_Answer,MSQ_Answer, Nat_Answer,
                Option_A_ID, Option_B_ID, Option_C_ID, Option_D_ID,Answered_Options,pushpa,Peter_pAkaaar]
        
        Avengers.append(SuperHeroes)
        
    columns = ["Q_No", "Q_Type", "Q_ID", "Status", "MCQ_Answer","MSQ_Answer", "Nat_Answer",
                "Option_A_ID", "Option_B_ID", "Option_C_ID", "Option_D_ID","Answered_Options","Actual_Key","Question_Key"]
    Marvel_studios = pd.DataFrame(Avengers, columns=columns)
    Marvel_studios.sort_values('Question_Key',inplace=True)
    release_movies = Marvel_studios [['Question_Key','Actual_Key','Q_Type','Status','Answered_Options']]
    release_movies.to_csv(f'{movie_name}_results.csv', index=False)
    print("\n\n\nResponses : \n",release_movies,'\n\nCheck Result in ',f'{movie_name}_results.csv')
    
def print_help():
    print("Help:")
    print("Usage: python ResponseSheet.py -f <file_path>")
    print("-f, --file <file_path>: Path to the file to process")
    sys.exit(0)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="GATE 2024 Response sheet is released, but its all jumbled, even the options,so I correct it and even separated 1marks and 2 Marks Question, save the response in html and pass it to the app. it should produce a csv with ordered response")
    parser.add_argument("-f", "--file", type=str, help="Path to the file to process")
    

    args = parser.parse_args()

    if args.file == None:
        print('Usage: python ResponseSheet.py -f <file_path>')
    else:
        main(args)
