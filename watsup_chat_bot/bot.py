from openai import OpenAI
import pyautogui
import pyperclip
import time
from openai import OpenAI

client = OpenAI(
    api_key="Enter Your api key"
)
def is_last_message(chat_log,sender_name="rohan das"):
    messages =chat_log.strip().split("\n")
    if sender_name in messages:
        return True
    return False  
pyautogui.click(1011,1058)
time.sleep(1)
while True:
  pyautogui.moveTo(416,145)
  pyautogui.dragTo(1808,950,duration=1.0,button='left')
  pyautogui.hotkey('ctrl','c')
  time.sleep(1)
  chatHistory=pyperclip.paste()
  print(chatHistory)
  if is_last_message(chatHistory):
    completion = client.chat.completions.create(
      model='gpt-3.5-turbo',
    
    messages=[
      {"role":"system","content":"You are a person named Nauruto who speaks hindi as well as english . you are from  india and you are a coder. You analyze chat history  and respond like Naruto.output should be the next chat response as Naruto"},
     {'role':"user","content":chatHistory}
    ])
    response =completion.choices[0].message.content
    pyperclip.copy(response)
    pyautogui.click(1808,1328)
    time.sleep(1)
    pyautogui.hotkey('ctrl','v')
    pyautogui.sleep(1)
    pyautogui.press('enter')