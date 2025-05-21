This repository was created to help augment and optimise the job searching process, resulting in more leads. The script searches `Google jobs` via [SerpApi](https://medium.com/r/?url=http%3A%2F%2Fserpapi.com), for which you'll require an `API Key`.

`Script Modifications:`

The following lines should be modified and saved based on preference before running the script:
- `Line 6:` Input the `API Key` derived from `SerpApi`.
- `Line 9:` `max_results=2000` is the default value, requiring the script to return up to `2000` values, if available. This can be modified.
- `Line 32:` Add the `job role` and other words you want queried during the search.
- `Line 63:` Input the name of the file with the scraped results where you see `filename`.
- `Line 69:` Input the `job role` where you see `query`.
- `Line 70:` Input the `location` of your preference.
- `Line 72:` Re-enter the `max_results`

`Run Script:`
- To run the `job_search.py` file, copy and paste this into your terminal or bash `python3 job_search.py` and run. Depending on the `Python` version you have installed, you may use `python job_search.py`.

-----------------

A brief background can be found [here](https://medium.com/@aoluf/improve-optimise-your-job-search-f33a543bb54e)
