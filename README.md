# Free Lunch with Python

A python script that alerts you when free food is posted to subreddits via discord bot. 

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)

## Description
This project uses PRAW to check food subreddits to see when free coupons/rewards have been posted. It will send an alert to a discord server via a discord bot, allowing you to get there first. 

I would have used the Twilio API to send an SMS message, but they have strict restrictions now that take forever to get around.

## Installation

Clone the repository:

```sh
git clone https://github.com/aaron10l/free-lunch.git
cd free-lunch
```

Install dependencies:
```sh
pip install -r requirements.txt
```

## Usage

 **Add Environment Variables:**
   You will need reddit API credentials (script) and also discord bot credentials. Add these in a .env file according to the names in the script.

**Run the Script:**
   ```bash
   python bot.py
   ```

