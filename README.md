## Reddit & Notion integrated datatable

An auto-updated notion datatable built with reddit api, notion api and github actions
See demo : https://wooden-hortensia-2e9.notion.site/f93f03ce6289490c9fd819000d888cf3?v=ec3daf44b6fb4a73b9fdaed9e704be63

## What it does

1. Fetch data from the user's notion page to see determine which subreddits to scrape 
  - Notion api for retrieving page block data
2. Scrape top 10 monthly submissions from subreddits
  - PRAW, a reddit api wrapper for python for scraping
  - Data includes title, url, score, created date, subreddit
3. Update the submission info as rows at a pre-defined notion datatable 
  - Before updating, retrieve url data from the notion datatable and create a hashmap to use for searching (in order to prevent entry of duplicates)
  - Notion api for retrieving and updating the notion datatable
4. Schedule the above tasks (1 ~ 3) so that it is performed automatically, every day
  - Github actions for task automation

## How it works


## pre-requisites 

 



