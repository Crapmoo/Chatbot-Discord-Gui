
![Logo](https://cdn.discordapp.com/attachments/1169126665935405126/1220334063626358814/logo.png?ex=660e8fa9&is=65fc1aa9&hm=bddc97c91b2fc5adb823b62d6ea8627037f91dd50f025c255a399046f9e8da1f&)


# Chatbot-discord-gui 

This is a easy way to use AI chatbot in discord server.



<div align="center">
    <img src="https://cdn.discordapp.com/attachments/1169126665935405126/1220337452020138096/image.png?ex=660e92d1&is=65fc1dd1&hm=ff53eb3172b42014f1c9d3c08589be7ebfcc20c578bdd93069d420356d5e8cf6&">
</div>


## Features

- Can select chat engine model Gemini or ChatGPT
- Start stop bot in one click
- Log
- Auto save config value


## Model support

| Color             | Model                                                               | Test |
| ----------------- | ------------------------------------------------------------------ | ------|
| Google | gemini-1.0-pro-001 | Pass ![#0a192f] |
| OpenAI | gpt-4-turbo-preview | Pass ![#0a192f] |
| OpenAI | gpt-4-1106-preview | Pass ![#0a192f] |
| OpenAI | gpt-4-0613 | Pass ![#0a192f] |
| OpenAI | gpt-4-0125-preview | Pass ![#0a192f] |
| OpenAI | gpt-4 | Pass ![#0a192f] |
| OpenAI | gpt-3.5-turbo-16k-0613 | Pass ![#0a192f] |
| OpenAI | gpt-3.5-turbo-16k | Pass ![#0a192f] |
| OpenAI | gpt-3.5-turbo-1106 | Pass ![#0a192f] |
| OpenAI | gpt-3.5-turbo-0613 | Pass ![#0a192f] |
| OpenAI | gpt-3.5-turbo-0301 | Pass ![#0a192f] |
| OpenAI | gpt-3.5-turbo-0125 | Pass ![#0a192f] |
| OpenAI | gpt-3.5-turbo | Pass ![#0a192f] |




## Installation


1.Install python (if you use 3.12.x version you may edit the eel library. See how to fix in the next step.)

2.install the library with this command

```bash
  pip install -r requirement.txt
```
3.open file `run.bat` and have fun


## Watch installation on youtube 
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/t0Hv2SqklPM/0.jpg)](https://www.youtube.com/watch?v=t0Hv2SqklPM)

Click image or click this link --> www.youtube.com/watch?v=t0Hv2SqklPM
## Fix error ModuleNotFoundError: No module named 'bottle.ext.websocket'

</details>
 If you have this problem 

### Method 1
- use `python 3.10`

### Method 2
- Change `import bottle.ext.websocket as wbs`  to  `import bottle_websocket as wbs`
  
go to this folder ( Change `"_YOUR_USER_"` to your user like `Administrator` or `Crapmoo-Pc` )
```bash
 C:\Users\"_YOUR_USER_"\AppData\Local\Programs\Python\Python312\Lib\site-packages\eel
```
![image](https://cdn.discordapp.com/attachments/1169126665935405126/1220347422904029194/image.png?ex=660e9c1a&is=65fc271a&hm=0deeb783c8d5b1c18b7c52d0d6b5d9c94f0c3b700018a00d8f1153e3bfe51212&)


 open `__init__.py` with notepad
 
![image](https://cdn.discordapp.com/attachments/1169126665935405126/1220349069004640317/image.png?ex=660e9da3&is=65fc28a3&hm=2c87ff3ac7ed57e9054f557398d93c8c48733ffb76f9468ba8ecadd5f86451f4&)


 edit `import bottle.ext.websocket as wbs`  to  `import bottle_websocket as wbs`
 ```bash
import bottle_websocket as wbs
```

![image](https://cdn.discordapp.com/attachments/1169126665935405126/1220349159685750854/image.png?ex=660e9db8&is=65fc28b8&hm=613efa62e8a75168c843da981e33ee323a7eb536587a6334ffe5eff67f234bd0&)



