from __future__ import print_function
import eel
import web.modules.properties as properties
import subprocess
import atexit
from web.modules.log import logger  # Import logger from log.py

bot_process = None

def run():
    eel.init('web')

    bot_module = "web/modules/bot.py"

    @eel.expose
    def Bot_Start(engine, token, key, chanel):
        global bot_process

        properties.properties_write(engine, token, key, chanel)
        logger.info(f'Saving engine token key chanel Successfully')

        # Launch the bot script
        if not bot_process:
            bot_process = subprocess.Popen(['python', bot_module])
            logger.info("Bot process started")

    @eel.expose
    def Bot_Stop():
        global bot_process
        if bot_process:
            # Terminate the bot process
            bot_process.terminate()
            bot_process = None
            logger.info("Bot process stopped")

    @eel.expose
    def Bot_Log():
        logger.info("Open log file")
        log_file = "bot.log"
        subprocess.Popen(["notepad", log_file])

    # Register function to handle cleanup on exit
    atexit.register(on_exit)

    @eel.expose
    def Bot_Status():
        if bot_process:
            return "Online"
        else:
            return "Offline"
            
    @eel.expose
    def Message_Callbace(message):
        logger.info(message)


    eel.start("index.html", size=(500, 700))

    
def on_exit():
    global bot_process
    if bot_process:
        # Terminate the bot process before exiting
        bot_process.terminate()
        bot_process = None
        logger.info("Bot process terminated before exit")

if __name__ == "__main__":
    run()
