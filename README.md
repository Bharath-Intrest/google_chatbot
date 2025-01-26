# google_chatbot
AWS host link : https://search.app/pQMGijh9JjmiVn4W7
In local cmd:
* scp 'key-pair-path' 'upload-file-path' ubuntu@instance-public-ip  Note: path must be in single quotes.
* ssh -i "path/your-key-file.pem" ubuntu@instance-public-ip
* update server
* install python3 and nginx
* install pip
* install necessary packages in new environment
* run python file
* add default nginx path to uploaded html file
* to run permanently: nohup python3 chatbot_api.py &
