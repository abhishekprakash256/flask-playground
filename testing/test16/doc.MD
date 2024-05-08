## The Website Doc 

### Requirements 

Check the requirements.txt file for the specific versions - 
```
python3 
Flask 
mongodb 
nginx 
pymongo 
aws ec2 (static ip)
```

### File structure : - 

```
mongo (the files that are used for the mongo data hnadling and insertion)
    - mongo_helper (the file connects the mongo client and the data and the has the methods to add , insert , update, delete and show in the database, the database )
    - read_data_json (the file is used to read the data from the json for the insertion in the mongodb)
    - data_handling (the data handling file is used to add and update the database as per requirement)
    - bulk_data_insertion (The file is used for the addition of the data from the json file read it delete all and then write the lastest data , the problem is currently add the data by deletion of all rather than modifications)


static (The static files of the website are here )
    - images (all images as per sections of the website)
        - icons (all icons)
        - misc (the dummy images)
        - profile (The profile pic)
        - projects (The project images are in the respective project folder)
        - tech (The images for tech section of the website)
    - Projects (The project section files)
        - Academic-Webiste (The website project files)
    - resume ( The current resume file )
    - project_article_data (The project data of the articles )
    - route_template_map (not being used right now )
    - section_data (The section data from the section page with tech , life and proeject for card stucture)
    - tech_article_data ( The tech data of the articles )
    - style ( The css file for webiste )

templates (the templates of the sites that render in the front end)
    - base ( the base template for the staring templates has the cdm links and  file links)
    - components ( the pages are different section of the website that can be designed one for particular pages as per name explanamable)
    - projects ( The arrtice page to display the articles )
        - article-body (the body section that has heading, image, para , markdown )
        - article ( the artcile rendering file )
        - extra file ( the dummy files to test )
    - reusable ( the reusable components of the webiste template )
    - about ( the about page)
    - index ( the index page )
    - section ( the section display page ) find the diff in the two
    - showcase ( the showcase page ) might not be in use anymore, check the live version now 

app ( the main flask file for runner and making end points)

exp ( an experiment file can be changed anytime as per needed )

form_data (the file to store the data from the message fields)

read_data_mongo (read the data from the mongo and fetch it for render )
```

## The commands to use (mostle linux based)



### The nginx command 

```

sudo apt update
sudo apt install nginx
sudo systemctl start nginx
sudo systemctl enable nginx

sudo nginx -t
sudo systemctl reload nginx

```

### The mongo commands

```
mongosh 
use your_database_name
show collections
db.dropDatabase()  #delete the dropDatabase
db.<collection_name>.drop()  #drop the 
db.my_collection.find() #show all the data in collection
```

### cert bot commands 

```
sudo yum install certbot python3-certbot-nginx
sudo certbot --nginx -d meabhi.me -d www.meabhi.me
sudo certbot --nginx -d meabhi.me
```

### The Flask commands 

```
python3 app.py 

to run on the server 
flask run --host=0.0.0.0 --port=5000


kil flask by 
ps aux | grep flask
kil pid

run the flask in background 
flask run --host=0.0.0.0 --port=5000 > output.log 2>&1 & disown
```


##  Nginx Configurations 

The nginx configuration file is used to make the nginx connect to the certbot files , put the domain name as well. The file location - 




```

server {
    listen 80;
    server_name www.meabhi.me;

    # Redirect HTTP to HTTPS
    location / {
        return 301 https://$host$request_uri;
    }
}

server {
    listen 443 ssl;
    server_name www.meabhi.me;

    ssl_certificate /etc/letsencrypt/live/meabhi.me/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/meabhi.me/privkey.pem;

    # Other SSL configuration directives (e.g., SSL protocols, ciphers, etc.)

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}

```
