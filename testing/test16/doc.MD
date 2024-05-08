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


```






