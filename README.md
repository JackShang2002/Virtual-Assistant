# Izzy
Personal assistance AI named Izzy (will be referred to as Izzy from now on) that can respond to several function calls through parsing keywords from microphone input. List of functions below:


Repeat: sentence containing "repeat please" will cause previous prompt to be repeated.

WikiSearch: sentence containing "get me notes on" will cause speaker output of a wikipedia search of the keyword that immediately follow. For example, if the input is "get me notes on Dick Cheney", then Izzy will return the wiki search result of "Dick Cheney" through speaker.

GetMorningNews: sentence containing "get the morning news" will cause speaker output of the top articles of CBC at the time of function call. Can be modified to webscrape other websites and output the full article/description instead of just the headline.

Exit: sentence containing "that will be all for now" will result in a sys.exit() call to terminate the program.
