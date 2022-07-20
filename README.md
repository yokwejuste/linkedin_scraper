## LinkedIn Scraper 2022

This is the new update concerning the data scraping from [LinkedIn](https://linkedin.com).

![linked data mining](https://woz-u.com/wp-content/uploads/2021/04/woz-what-is-data-mining-1280x720.jpg)

## Tools used for this project
- [Python](https://www.python.org/)
- [Selenium](https://www.seleniumhq.org/)
- [parsel](https://parsel.readthedocs.io/)
- [iPython](https://ipython.org/)

To contribute, you know the story,

- [Fork](https://github.com/yokwejuste/linkedin-scraper/fork)
- Clone
    - ```
        git clone https://github.com/<your github username>/linkedin-scraper.git
        ```
- Make commits and PRs
    - ```
        git add .
        git commit -m "message"
        git push
        ```

### System Setup

- Download dependencies
    ```bash
        pip install -r requrements.txt

    ```
- Create a `.env` file with the following variables:
    ```bash
        LINKEDIN_USERNAME=**************
        LINKEDIN_PASSWORD=**************
    ```
- Run the scraper
    ```bash
        python main.py
    ```

    The scraper will automatically login and scrape the data.

You will notice a results.csv file in the root directory, open and see the data. Play around with the code from `varibles.py` modify the xpath data in the main file to scrape more and different data.

Add me a start and fork the repository.

This is a project under the [MIT License](https://opensource.org/licenses/MIT).