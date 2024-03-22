
# Chatbot-discord-gui 

This is a easy way to use AI chatbot in discord server.



<div align="center">
    <img src="https://cdn.discordapp.com/attachments/1169126665935405126/1220337452020138096/image.png?ex=660e92d1&is=65fc1dd1&hm=ff53eb3172b42014f1c9d3c08589be7ebfcc20c578bdd93069d420356d5e8cf6&">
</div>

---

## Features

- Can select chat engine model Gemini or ChatGPT
- Start stop bot in one click
- Log
- Auto save config value

---


## Status symbol
|   Symbol  | Status |
|----------|---------|
| 🔴      | Not test |
| 🟡 | Pending |
|🟢 |  Test |
| ✔️ | Pass |
| ❌ | Fail |
| ⏳ | Penging|



## Model support

|    Developer          | Model                                                               | Test | Pass |
| ----------------- | ------------------------------------------------------------------ | ------| ------|
| Google | gemini-1.0-pro-001 | 🟢 | ✔️ |
| OpenAI | gpt-4-turbo-preview | 🟢 | ✔️ |
| OpenAI | gpt-4-1106-preview | 🟢 | ✔️ |
| OpenAI | gpt-4-0613 | 🟢| ✔️ |
| OpenAI | gpt-4-0125-preview | 🟢 | ✔️ |
| OpenAI | gpt-4 | 🟢 | ✔️ |
| OpenAI | gpt-3.5-turbo-16k-0613 | 🟢 | ✔️ |
| OpenAI | gpt-3.5-turbo-16k | 🟢 | ✔️ |
| OpenAI | gpt-3.5-turbo-1106 | 🟢 | ✔️ |
| OpenAI | gpt-3.5-turbo-0613 | 🟢 | ✔️ |
| OpenAI | gpt-3.5-turbo-0301 | 🟢 | ✔️ |
| OpenAI | gpt-3.5-turbo-0125 | 🟢 | ✔️ |
| OpenAI | gpt-3.5-turbo | 🟢 | ✔️ |

## Os support

|    Os          | Test | Pass |
| -------------- | -----| ---- |
| Windows 10     | 🟢   | ✔️  |
| Windows 11     | 🔴   | ⏳  |
| Mac os     | 🔴   | ⏳  |
| Linux    | 🔴   | ⏳  |

---

## Installation

1. Install [python](https://www.python.org/) ( if you use 3.12.x version you may edit the eel library. See how to fix in the [next step](https://github.com/Crapmoo/Chatbot-Discord-Gui?tab=readme-ov-file#fix-error-modulenotfounderror-no-module-named-bottleextwebsocket) )
2. install the library with this command

```bash
  pip install -r requirement.txt
```
3. open file `run.bat` and have fun


## Watch installation on youtube 
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/t0Hv2SqklPM/0.jpg)](https://www.youtube.com/watch?v=t0Hv2SqklPM)

Click image or [`Click Here`](www.youtube.com/watch?v=t0Hv2SqklPM)

---

## Fix error ModuleNotFoundError: No module named 'bottle.ext.websocket'

 If you have `ModuleNotFoundError: No module named bottle.ext.websocket`  problem 

### Method 1
 - use `python 3.10`

### Method 2
 - Change `import bottle.ext.websocket as wbs`  to  `import bottle_websocket as wbs`
   
 1. go to this folder ( Change `"_YOUR_USER_"` to your user like `Administrator` or `Crapmoo-Pc` )
 ```bash
  C:\Users\"_YOUR_USER_"\AppData\Local\Programs\Python\Python312\Lib\site-packages\eel
 ```
 ![image](https://cdn.discordapp.com/attachments/1169126665935405126/1220347422904029194/image.png?ex=660e9c1a&is=65fc271a&hm=0deeb783c8d5b1c18b7c52d0d6b5d9c94f0c3b700018a00d8f1153e3bfe51212&)

 2. open `__init__.py` with notepad
 
 ![image](https://cdn.discordapp.com/attachments/1169126665935405126/1220349069004640317/image.png?ex=660e9da3&is=65fc28a3&hm=2c87ff3ac7ed57e9054f557398d93c8c48733ffb76f9468ba8ecadd5f86451f4&)


 3. edit `import bottle.ext.websocket as wbs`  to  `import bottle_websocket as wbs`
 ```bash
 import bottle_websocket as wbs
 ```

 ![image](https://cdn.discordapp.com/attachments/1169126665935405126/1220349159685750854/image.png?ex=660e9db8&is=65fc28b8&hm=613efa62e8a75168c843da981e33ee323a7eb536587a6334ffe5eff67f234bd0&)

Watch video on youtube
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/uOdp_E1vL68/0.jpg)](https://www.youtube.com/watch?v=uOdp_E1vL68)

Click image or [`Click Here`](www.youtube.com/watch?v=uOdp_E1vL68)

---


# How to use

1. Open `run.bat`

2. Select `Chat model`

3. Add your `Discord bot token`

4. Add your `API key`

5. Add your `Discord channel id`

6. Click `Start`

---


# How to get Discord token

1. Create discord bot

2. Invite your bot

3. Get `token`

---

# How to get API key

### Google Gemini
 1. go to [Google AI studio](https://aistudio.google.com/app/apikey)
 2. create `API Key`
 3. Copy

### Openai ChatGPT

1. go to [OpenAI](https://platform.openai.com/api-keys)
2. Create new secret key
3. Copy
   
---

# How to get Discord channel id
1. enable deverloper mode
2. right click at discord chat you want
3. copy channel id

---
    


