""" zid_project1.py

"""
import json
import os

import toolkit_config as cfg

# ----------------------------------------------------------------------------
# Location of files and folders
# Instructions:
#   - Replace the '<COMPLETE THIS PART>' strings with the appropriate
#   expressions.
# IMPORTANT:
#   - Use the appropriate method from the `os` module to combine paths
#   - Do **NOT** include full paths like "C:\\User...". You **MUST* combine
#     paths using methods from the `os` module
#   - See the assessment description for more information
# ----------------------------------------------------------------------------
ROOTDIR = os.path.join(cfg.PRJDIR, 'project1')
DATDIR = os.path.join(ROOTDIR, 'data')
TICPATH = os.path.join(ROOTDIR, 'TICKERS.txt')

# ----------------------------------------------------------------------------
# Variables describing the contents of ".dat" files
# Instructions:
#   - Replace the '<COMPLETE THIS PART>' string with the appropriate
#     expression.
#   - See the assessment description for more information
# ----------------------------------------------------------------------------
# NOTE: `COLUMNS` must be a list, where each element is a column name in the
# order they appear in the ".dat" files
COLUMNS = ['Volume', 'Date', 'Adj Close', 'Close', 'Open', 'High']

# NOTE: COLWIDTHS must be a dictionary with {<col> : <width>}, where
# - Each key (<col>) is a column name in the `COLUMNS` list
# - Each value (<width>) is an **integer** with the width of the column, as
#   defined in your README.txt file
#
COLWIDTHS = {
    'Volume': 14,
    'Date': 11,
    'Adj Close': 19,
    'Close': 10,
    'Open': 6,
    'High': 20
}


# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def get_tics(pth):
    """ Reads a file containing tickers and their corresponding exchanges.
    Each non-empty line of the file is guaranteed to have the following format:

    "XXXX"="YYYY"

    where:
        - XXXX represents an exchange.
        - YYYY represents a ticker.

    This function should return a dictionary, where each key is a properly formatted
    ticker, and each value the properly formatted exchange corresponding to the ticker.

    Parameters
    ----------
    pth : str
        Full path to the location of the TICKERS.txt file.

    Returns
    -------
    dict
        A dictionary with format {<tic> : <exchange>} where
            - Each key (<tic>) is a ticker found in the file specified by pth (as a string).
            - Each value (<exchange>) is a string containing the exchange for this ticker.

    Notes
    -----
    The keys and values of the dictionary returned must conform with the following rules:
        - All characters are in lower case
        - Only contain alphabetical characters, i.e. does not contain characters such as ", = etc.
        - No spaces
        - No empty tickers or exchanges

    """
    tickers_dict = {}

    with open(pth, 'r') as file:
        for line in file:

            line = line.strip()
            if not line:
                continue

            exchange, ticker = line.split('=')

            exchange = exchange.strip().lower()
            ticker = ticker.strip().lower()

            if exchange.isalpha() and ticker.isalpha():
                tickers_dict[ticker] = exchange

    return tickers_dict

# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def read_dat(tic):
    """ Returns a list with the lines of the ".dat" file containing the stock
    price information for the ticker `tic`.


    Parameters
    ----------
    tic : str
        Ticker symbol, in lower case.

    Returns
    -------
    list
        A list with the lines of the ".dat" file for this `tic`. Each element
        is a line in the file, without newline characters (e.g. '\n')


    Hints (optional)
    ----------------
    - Create a variable with the location of the relevant file using the `os`
      module, the `DATDIR` constant, and f-strings.

    """
    # IMPORTANT: The answer to this question should NOT include full paths
    # like "C:\\Users...". There should be no forward or backslashes.
    file_path = os.path.join(DATDIR, f"{tic}.dat")

    lines = []

    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line.strip())

    return lines

# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def line_to_dict(line):
    """Returns the information contained in a line of a ".dat" file as a
    dictionary, where each key is a column name and each value is a string
    with the value for that column.

    This line will be split according to the field width in `COLWIDTHS`
    of each column in `COLUMNS`.

    Parameters
    ----------
    line : str
        A line from ".dat" file, without any newline characters

    Returns
    -------
    dict
        A dictionary with format {<col> : <value>} where
        - Each key (<col>) is a column in `COLUMNS` (as a string)
        - Each value (<value>) is a string containing the correct value for
          this column.

    Hints (optional)
    ----------------
    - Your solution should include the constants `COLUMNS` and `COLWIDTHS`
    - For each line in the file, extract the correct value for each column
      sequentially.

    """
    result = {}

    position = 0

    for column in COLUMNS:
        width = COLWIDTHS[column]
        value = line[position:position + width].strip()
        result[column] = value
        position += width

    return result

# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def verify_tickers(tic_exchange_dic, tickers_lst=None):
    """Verifies if the tickers provided are valid according to the rules provided in the Notes.
        If a rule is broken, this function should raise an Exception.

        Parameters
        ----------
        tic_exchange_dic : dict
            A dictionary returned by the `get_tics` function

        tickers_lst : list, optional
            A list containing tickers (as strings) to be verified

        Returns
        -------
        None
            This function does not return anything

        Notes
        -----
        If tickers_lst is not None, raise an Exception if any of the below rules are violated:
            1. tickers_lst is an empty list.

            2. tickers_lst contains a ticker that does not correspond to a key tic_exchange_dic

               Example:
               If tic_exchange_dic is {'tsm':'nyse', 'aal':'nasdaq'},
               tickers_lst = ['aal', 'Tsm'] would raise an Exception because
               'Tsm' is not a key of tic_exchange_dic.

    """
    if tickers_lst is not None:
        if not tickers_lst:
            raise Exception("The tickers list is empty.")

        for ticker in tickers_lst:
            if ticker.lower() not in tic_exchange_dic:
                raise Exception(f"Ticker '{ticker}' is not valid or not found in the exchange dictionary.")


# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def verify_cols(col_lst=None):
    """Verifies if the column names provided are valid according to the rules provided in the Notes.
        If a rule is broken, this function should raise an Exception.

        Parameters
        ----------
        col_lst : list, optional
            A list containing column names (as strings) to be verified

        Returns
        -------
        None
            This function does not return anything

        Notes
        -----
        If col_lst is not None, raise an Exception if any of the below rules are violated:
            1. col_lst is an empty list.

            2. col_lst contains a column that is not found in `COLUMNS`.

               Example:
               If COLUMNS = ['Close', 'Date'],
               col_lst = ['close'] would raise an Exception because 'close' is not found in `COLUMNS`

    """
    if col_lst is not None:
        if not col_lst:
            raise Exception("The column list is empty.")

        for col in col_lst:
            if col not in COLUMNS:
                raise Exception(f"Column '{col}' is not valid or not found in COLUMNS.")


# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def create_data_dict(tic_exchange_dic, tickers_lst=None, col_lst=None):
    """Returns a dictionary containing the data for the tickers specified in tickers_lst.
        An Exception is raised if any of the tickers provided in tickers_lst or any of the
        column names provided in col_lst are invalid.

        Parameters
        ----------
        tic_exchange_dic: dict
            A dictionary returned by the `get_tics` function

        tickers_lst : list, optional
            A list containing tickers (as strings)

        col_lst : list, optional
            A list containing column names (as strings)

        Returns
        -------
        dict
            A dictionary with format {<tic> : <data>} where
            - Each key (<tic>) is a ticker in tickers_lst (as a string)
            - Each value (<data>) is a dictionary with format
                {
                    'exchange': <tic_exchange>,
                    'data': [<dict_0>, <dict_1>, ..., <dict_n>]
                }
              where
                - <tic_exchange> refers to the exchange that <tic> belongs to in lower case.
                - <dict_0> refers to the dictionary returned by line_to_dict(read_dat(<tic>)[0]),
                  but that only contains the columns listed in col_lst
                - <dict_n> refers to the dictionary returned by line_to_dict(read_dat(<tic>)[-1]),
                  but that only contains the columns listed in col_lst

        Notes
        -----
        - Please refer to the assessment description for an example of what the returned dictionary should look like.
        - If tickers_lst is None, the dictionary returned should contain the data for
          all tickers found in tic_exchange_dic.
        - If col_lst is None, <dict_0>, <dict_1>, ... should contain all the columns found in `COLUMNS`

        Hints (optional)
        ----------------
        - To check if tickers_lst contains any invalid tickers, you can call `verify_tickers`
        - To check if col_lst contains any invalid column names, you can call `verify_cols`
        - This function should call the `read_dat` and `line_to_dict` functions

    """

    if tickers_lst is None:
        tickers_lst = list(tic_exchange_dic.keys())

    if col_lst is None:
        col_lst = COLUMNS

    verify_tickers(tic_exchange_dic, tickers_lst)
    verify_cols(col_lst)

    data_dict = {}

    for ticker in tickers_lst:
        lines = read_dat(ticker)

        ticker_data = [line_to_dict(line) for line in lines]
        filtered_data = [{col: entry[col] for col in col_lst} for entry in ticker_data]

        data_dict[ticker] = {
            'exchange': tic_exchange_dic[ticker],
            'data': filtered_data
        }

    return data_dict


# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def create_json(data_dict, pth):
    """Saves the data found in the data_dict dictionary into a
        JSON file whose name is specified by pth.

        Parameters
        ----------
        data_dict: dict
            A dictionary returned by the `create_data_dict` function

        pth : str
            The complete path to the output JSON file. This is where the file with
            the data will be saved.


        Returns
        -------
        None
            This function does not return anything

    """
    with open(pth, 'w') as json_file:
        json.dump(data_dict, json_file, indent=4)


# ----------------------------------------------------------------------------
#    Please put your answers for the last question here:
# ----------------------------------------------------------------------------
    """1.In Step 1, set the locations of files and folders using variables that help code run seamlessly on different operating systems. 
Because it handles file paths in a platform-independent manner. The use of relative paths with ‘os.path.join()’ ensures the code can be shared and run on other systems without modification.
It also helps to centralise path variables making the code easier to maintain and minimising potential errors. 
If folder structures change in the future, we only need to update the variables in one place. The constants simplify the process of expanding the project structure. 
2.Hypothesis 1 is “Investors' evaluations of those firms”. We assume that Journalists’ articles reflect the collective sentiments and evaluations of investors regarding the firm's fundamentals. 
If the articles reflect investors' opinions, then the negative words in the articles would likely align with a change in firm fundamentals or investor expectations and the stock price would adjust accordingly. 
If the market overreacts initially, stock prices might correct or revert over the long run.
We observed that stock returns decrease in the short run but do not recover over time. This weakens the argument for this hypothesis because, typically, 
if articles reflect investor sentiment, overreactions will result in “price reversals” as new information emerges, or the market corrects itself.
Hypothesis 2 is “Valuable information beyond firm fundamentals”. We assumed that Journalists have insights or information not yet fully reflected in firm fundamentals, which affects investor behaviour. 
The articles with “negative words” provide new, unfavourable information to the market. Investors react to this new information, leading to an immediate decline in stock prices. 
Since the information provided by the articles is relevant beyond short-term sentiment, the market reaction becomes persistent.
The supposed observation aligns well with this hypothesis. It suggests that the information provided in the articles was meaningful and reflected changes beyond firm fundamentals.
Based on the observed data, Hypothesis 2 is more likely to be true. The absence of price reversal over the long run indicates that the articles likely contained valuable information beyond what was previously known about the firm. 
If the articles had merely reflected existing investor evaluations (Hypothesis 1), a long-run correction or reversal in stock prices would be expected.
3. Based on Hypothesis 2, which suggests that articles provide valuable information beyond firm fundamentals, we can imply that new information affects market behaviour.  
When articles contain negative words and provide insights not yet reflected in firm fundamentals, investors react quickly, triggering short-term trading activity.
It may increase trading volume with short-run predictability. As investors act on the newly revealed information, some may sell off their holdings to avoid further losses. 
Other market participants may buy shares expecting future opportunities.The reasons are that the market reacts to unexpected news, and trading volume tends to spike right after the release of such articles with negative words. 
Because any new and impactful information, especially negative, typically prompts immediate buying and selling activities. 
Investors and traders react to the newly available information, resulting in increased volume right after the article’s publication. 
This surge in volume is predictable as it is a typical market response to relevant, unexpected information.
    """

# ----------------------------------------------------------------------------
#   Test functions:
#   The purpose of these functions is to help you test the functions above as
#   you write them.
#   IMPORTANT:
#   - These functions are optional, you do not have to use them
#   - These functions do not count as part of your assessment (they will not
#     be marked)
#   - You can modify these functions as you wish, or delete them altogether.
# ----------------------------------------------------------------------------
def _test_get_tics():
    """ Test function for the `get_tics` function. Will print the tickers as
    returned by the `get_tics` function.
    """
    pth = TICPATH
    tics = get_tics(pth)
    print(tics)


def _test_read_dat():
    """ Test function for the `read_dat` function. Will read the lines of the
    first ticker in `TICPATH` and print the first line in the list.
    """
    pth = TICPATH
    tics = sorted(list(get_tics(pth).keys()))
    tic = tics[0]
    lines = read_dat(tic)
    # Print the first line in the file
    print(f'The first line in the dat file for {tic} is:')
    print(lines[0])


def _test_line_to_dict():
    """ Test function for the `read_dat` function. This function will perform
    the following operations:
    - Get the tickers using `get_tics`
    - Read the lines of the ".dat" file for the first ticker
    - Convert the first line of this file to a dictionary
    - Print this dictionary
    """
    pth = TICPATH
    tics = sorted(list(get_tics(pth).keys()))
    lines = read_dat(tics[0])
    dic = line_to_dict(lines[0])
    print(dic)


def _test_create_data_dict():
    """ Test function for the `create_data_dict` function. This function will perform
    the following operations:
    - Get the tickers using `get_tics`
    - Call `create_data_dict` using
        - tickers_lst =  ['aapl', 'baba']
        - col_lst = ['Date', 'Close']
    - Print out the dictionary returned, but only the first 3 items of the data list for each ticker for brevity

    """
    pth = TICPATH
    tic_exchange_dic = get_tics(pth)
    tickers_lst = ['aapl', 'baba']
    col_lst = ['Date', 'Close']
    data_dict = create_data_dict(tic_exchange_dic, tickers_lst, col_lst)

    for tic in tickers_lst:
        data_dict[tic]['data'] = data_dict[tic]['data'][:3]

    print(data_dict)


def _test_create_json(json_pth):
    """ Test function for the `create_json_ function.
    This function will save the dictionary returned by `create_data_dict` to the path specified.

    """
    pth = TICPATH
    tic_exchange_dic = get_tics(pth)
    tickers_lst = ['aapl', 'baba']
    col_lst = ['Date', 'Close']
    data_dict = create_data_dict(tic_exchange_dic, tickers_lst, col_lst)
    create_json(data_dict, json_pth)
    print(f'Data saved to {json_pth}')


# ----------------------------------------------------------------------------
#  Uncomment the statements below to call the test and/or main functions.
# ----------------------------------------------------------------------------
# if __name__ == "__main__":
#     #Test functions
#     _test_get_tics()
#     _test_read_dat()
#     _test_line_to_dict()
#     _test_create_data_dict()
#     _test_create_json(os.path.join(DATDIR, 'data.json'))  # Save the file to data/data.json
#     pass





