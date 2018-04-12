# Youtube-Trends-Crawler
A crawler to get the latest hot video information from https://www.youtube.com/feed/trending

Required modules: openpyxl, bs4, requests, pandas, numpy, datetime

Please run `pip3 install + <module_name>` to install these modules if needed.

Note: This script works only in Traditional Chinese Environment, Please substitute local language to "觀看次數：" which refers to the views of the video.

## The whole crawler can split into 5 parts:
1. Crawl Hot Video infos from YouTube.
2. Get the part that we are interested.
3. Store these parts into lists.
4. Store everything from lists in to DataFrame.
5. Get the correct file name and Export


### Part 1 - Crawl Hot Video infos from YouTube
To do this, I used `requests` and `BeautifulSoup` modules. More information can be found in this documentation https://www.crummy.com/software/BeautifulSoup/bs4/doc/

After getting the response from the url, I would look at our target text, I stored a target text's Template at the end of the ".py" file.

### Part 2 - Get the part that we are interested
To do this, I used `.find()` and `.find_all()` functions.
- `.find()` is a function that scans through the entire document looking for *only one* result.
- `.find_all()` is a function that scans through the entire document looking for results.
All the examples can be found in BeautifulSoup's documentation document.
- `.get_text()` is a useful function that can extract the text within the tag.

### Part 3 - Store these parts into lists
- Title, Author and Length data
I use the `.append()` function to gather everything in a list. However, I came to realize that all of the contents(title, author, length) are in the same lists. I have to find a way to extract all of them.

Fortunately, I found that title, author, length all these three type of data came in order in the list. As a results, I use numpy's function `np.arage()` to create three arithmetic series then use a for loop to run through all of them to extract the three type of data.

Another problem is that the video length data contains '\n\n' which is bad if we want to store these data in a DataFrame. As a result, I create another list and use the `split()` function with a for loop to extract everything.

- Date, Views data
This part is same as what I did in Title, Author, Length data.

### Part 4 - Store everything from lists in to DataFrame
I use `pd.DataFrame()` to import the first list into DataFrame. You can reference this Stackoverflow article: https://stackoverflow.com/questions/19112398/getting-list-of-lists-into-pandas-dataframe

As to follow the DRY(Don't Repeat Yourself) rule, for the rest of the list in the code, I write a function that imports everything implied in `data_header` and `data` this two lists.

### Part 5 - Get the right file name and Export
I created a variable called `file_name` and use `dt.date.today()` module to get today's time and create the correct file name for storing our results.

Finally, I store everything into ".xlsx" file with the correct file name using `to_excel()` function from Pandas. You can also store everything into ".csv" Since there are some encoding problems with traditional Chinese using ".csv", I export everything to ".xlsx" format.

If you have any questions/problems, welcome to <a href="mailto:samchen0727@gmail.com">email me</a>
Wish you enjoy this tutorial about creating a crawler for YouTube Trends Videos.
Have fun coding!
