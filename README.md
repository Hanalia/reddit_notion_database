## Reddit & Notion Integrated datatable

An auto-updated notion datatable built with reddit api, notion api and github actions  
See demo : https://wooden-hortensia-2e9.notion.site/Reddit-Collections-7f1b12c4517a4d2eb4157a8db89d74aa  
datatable url : https://wooden-hortensia-2e9.notion.site/f93f03ce6289490c9fd819000d888cf3?v=ec3daf44b6fb4a73b9fdaed9e704be63  
<img width="959" alt="Notion_01h2HmFyaR" src="https://user-images.githubusercontent.com/75914909/129497997-cc34d67a-5738-432d-a9cd-a0c12abf90ef.png">

## What it does

- Fetch data from the user's notion page to see determine which subreddits to scrape  
  Notion api for retrieving page block data  
  <img width="580" alt="Notion_t1idU08sUo" src="https://user-images.githubusercontent.com/75914909/129497956-53550149-3ca0-4a6f-9da4-ecde13a63d50.png">

- Scrape top 10 monthly submissions from subreddits  
 PRAW, a reddit api wrapper for python for scraping  
 Data includes title, url, score, created date, subreddit  

- Update the submission info as rows at a pre-defined notion datatable   
 Before updating, retrieve url data from the notion datatable and create a hashmap to use for searching (in order to prevent entry of duplicates)  
 Notion api for retrieving and updating the notion datatable  

- Schedule the above tasks (1 ~ 3) so that it is performed automatically, every day.  
  Github actions for task automation  


## How to set up your own datatable

### Initial Setup
Clone this repository
Duplicate both notion templates 
  a) page template https://www.notion.so/Reddit-Collections-7f1b12c4517a4d2eb4157a8db89d74aa
  b) database template https://www.notion.so/f93f03ce6289490c9fd819000d888cf3?v=ec3daf44b6fb4a73b9fdaed9e704be63

### Setting your secrets
Set the repository secrets for the below :
You can follow this [link](https://www.edwardthomson.com/blog/github_actions_11_secrets.html) for instructions
| Secrets  | Values                          | Description              |
|-----------|-----------------------------------|-----------------------------|
| `NOTION_API_KEY`     | your notion integration secrets | Create your own integration [here](https://developers.notion.com/) and get the API key.  Make sure to add integration from your notion page and datatable → this allows the integration to access your page and datatable |
|`REDDIT_CLIENT_ID`  `REDDIT_CLIENT_SECRET` `REDDIT_USER_AGENT`     | your reddit api client id, secret, and user-agent                          | Refer to this [link](https://github.com/reddit-archive/reddit/wiki/OAuth2#getting-started)                     |
| `DATABASE_KEY`   |   your notion database id                              | the id is in the url of your database. For example, from my url the database id is 'f93f03ce6289490c9fd819000d888cf3' (after /, before right before ?)                   |
| `PAGE_KEY`  | your notion page id                   | the id is in the url of your page. For example, from my url the page id is '7f1b12c4517a4d2eb4157a8db89d74aa' (after /, before right before ?) |


3. Set the repository secrets for the below :
 - You can follow this [link](https://www.edwardthomson.com/blog/github_actions_11_secrets.html) for instructions
a. `NOTION_API_KEY` - your notion integration secrets
 1) Create your own integration [here](https://developers.notion.com/) and get the API key
 2) Make sure to add integration from your notion page and datatable → this allows the integration to access your page and datatable
b. `REDDIT_CLIENT_ID` - your reddit api client id
c. `REDDIT_CLIENT_SECRET` - your reddit api client secret
d. `REDDIT_USER_AGENT` - your reddit api user agent 
 - for b ~ d, please refer to this [link](https://github.com/reddit-archive/reddit/wiki/OAuth2#getting-started)
e. `DATABASE_KEY` - your notion database id
 - the id is in the url of your database. For example, from my url the database id is 'f93f03ce6289490c9fd819000d888cf3' (after /, before right before ?)
f. `PAGE_KEY` = your notion page id 
- the id is in the url of your page. For example, from my url the page id is '7f1b12c4517a4d2eb4157a8db89d74aa' (after /, before right before ?)

<img width="702" alt="chrome_FE13QUwWCR" src="https://user-images.githubusercontent.com/75914909/129500058-2ae9756c-b844-495e-becf-5ce53ec274ac.png">

4. Customize your own subreddits and enjoy!


## Comments
1. If you add any blocks or text before the 'Subreddits to Scrape' block, the notion api will not be able to fetch subreddit information.
2. When adding new subreddits, please 'shift+enter' and add so that all the subreddits are inside a single block. 
The 'newly-Added' is in a single block with the previous text.
<img width="587" alt="Notion_8CulTB7xbG" src="https://user-images.githubusercontent.com/75914909/129499182-ac1ef849-901b-4d9b-b793-f786ab00a3c7.png">
However the below 'newly-Added' is in a separate block with the previous text.
<img width="590" alt="Notion_iWxTnHURRK" src="https://user-images.githubusercontent.com/75914909/129499229-b4ebd9c6-fd9c-4d0f-a52b-d83674716660.png">
 - Currently the code fetchs data from a specific block at a specific point from the page, so any changes in block location will break the code.

3. Currently the notion api does not support uploading of files/images. So for image-dense submissions (eg. dataisbeautiful), unfortunately I couldn't directly upload the images to the database. This feature can be updated in the future along with updates from the notion api.
 



