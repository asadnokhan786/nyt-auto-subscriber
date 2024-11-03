# nyt-auto-subscriber

## Abstract
- Many readers of *New York Times* have a premium subscribtion with a code that expires once every 1 - 2 days. It becomes a hassle constantly re-redeeming the same code for the purpose of reading an article
- This program aims to automate that process by using Selenium to auto-redeem your subscription codes based on user account email and password in a timely fashion, thus giving the user the impression they always have premium subscribtion of the *New York Times*

## TODO
- [ ] Create function for redeeming the codes
- [ ] Create automated testing for selenium function
- [ ] Implement logging
- [ ] Crate a routine check to run the redeem request at an interval specified by the user (1 day by default)
- [ ] Store credentials for redeeming in a  .env file
- [ ] Create script for making sure chrome is installed in operating system's default location
- [ ] Create cli interface for entering username, password, and code for persistent use
- [ ] Create cli interface for modifying routine update for redeming code
- [ ] Create automated tseting for cli comamnds
- [ ] Create a setup script to automatically setup python virtual environment       
- [ ] Create docker image for program for easy self deployment