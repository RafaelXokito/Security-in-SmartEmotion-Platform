#importing the module 
import logging 
import subprocess
import time

#now we will Create and configure logger 
logging.basicConfig(filename="logger.log", 
					format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%b %d %H:%M:%S', 
					filemode='w') 

#Let us Create an object 
logger=logging.getLogger() 

while True:

    # pm2 websocket
    output = subprocess.getoutput("pm2 ls | grep online")

    if output == "":

        #Now we are going to Set the threshold of logger to DEBUG 
        logger.setLevel(logging.INFO) 

        #some messages to test
        logger.info("PM2:Websocket offline")

        # .Popen("pm2", "start", "/var/www/project/websocket/index.js", "--watch", "--time", stdout=subprocess.PIPE)
        subprocess.getoutput("pm2 start /var/www/project/websocket/index.js --watch --time")

        logger.info("PM2:Websocket restarting")

    else:

        #Now we are going to Set the threshold of logger to DEBUG 
        logger.setLevel(logging.INFO) 

        #some messages to test
        logger.info("PM2:Websocket online") 

    # service php
    output = subprocess.getoutput("systemctl status php7.4-fpm | grep active")

    if output == "":

        #Now we are going to Set the threshold of logger to DEBUG 
        logger.setLevel(logging.CRITICAL) 

        #some messages to test
        logger.critical("systemctl:Php7.4-fpm offline") 

    else:

        #Now we are going to Set the threshold of logger to DEBUG 
        logger.setLevel(logging.INFO) 

        #some messages to test
        logger.info("systemctl:Php7.4-fpm online")

    # service php
    output = subprocess.getoutput("systemctl status mysql | grep active")

    if output == "":

        #Now we are going to Set the threshold of logger to DEBUG 
        logger.setLevel(logging.CRITICAL) 

        #some messages to test
        logger.critical("systemctl:mysql offline") 

    else:

        #Now we are going to Set the threshold of logger to DEBUG 
        logger.setLevel(logging.INFO) 

        #some messages to test
        logger.info("systemctl:mysql online")

    time.sleep(30)
