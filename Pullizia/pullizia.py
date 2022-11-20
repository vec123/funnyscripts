import random
import pyautogui
import webbrowser
import time
import datetime

#Init
People = ["Ire", "Agnese", "Pietro", "Zack", "Antonino", "Boti", "Alio", "Giada", "Marti", "Victor", "Edo", "Marco"]
Places = ["Cucuina + Salloto (Strada)", "Cucuina + Salloto (No-Strada)", "Scala + Terazzo + Salloto picollo davanti Edos camera", "Spazza + Lavatrice", "Recupera", "Liberta"]
Assignments = []
current_time = datetime.datetime.now()
message_send = False
reminder_send = False


while True:
        current_time = datetime.datetime.now()
        if current_time.strftime('%A') == "Monday":
        reminder_send=False
                if message_send==False:
                        Ppl_placeholder = People.copy()

                        url = 'https://web.whatsapp.com/'
                        webbrowser.open_new_tab(url)
                        time.sleep(10)
                        pyautogui.click(x=287, y=385) 

                        pyautogui.write('CLEANING_PLAN - Reminder: ')
                        pyautogui.keyDown('shift')  # hold down the shift key
                        pyautogui.press('enter') 
                        pyautogui.keyUp('shift')    # release the shift key
                        
                        f = open("Assignments.txt", "a")
                        for i,place in enumerate(Places):
                                                person1 = random.choice(Ppl_placeholder)
                                                Ppl_placeholder.remove(person1)
                                                person2 = random.choice(Ppl_placeholder)
                                                Ppl_placeholder.remove(person2)
                                                assignment_string = "{},{},{}".format(person1, person2,place)
                                
                                                k=0
                                                while assigmnmnment_string in Assignments:
                                                                print("already occurs")
                                                                Ppl_placeholder = People.copy()         
                                                                person1 = random.choice(Ppl_placeholder)
                                                                Ppl_placeholder.remove(person1)
                                                                person2 = random.choice(Ppl_placeholder)
                                                                Ppl_placeholder.remove(person2)
                                                                assignment_string = "{},{},{}".format(person1, person2,place)
                
                                                Assignments.append(assignment_string)
                                                #print("{} and {} are assigned to {}" .format(person1, person2, place))
                                                f.write("{} and {} are assigned to {} \n" .format(person1, person2, place))
                                                pyautogui.write("{} and {} are assigned to {}" .format(person1, person2, place))
                                                pyautogui.keyDown('shift')  # hold down the shift key
                                                pyautogui.press('enter') 
                                                pyautogui.keyUp('shift')    # release the shift key
                        pyautogui.write("\n")
                        message_send = True       
                        f.close()
                else:
                        print("message has already been send")

        if current_time.strftime('%A') == "Friday" and reminder_send == False:
                f = open("Assignments.txt", "r")
                for line in (f.readlines() [-6:]):
                        print(line, end ='')
                f.close()
                reminder_send=True
                message_send = False
        else:
                print("reminder has already been send")

       time.sleep(60*60*3)