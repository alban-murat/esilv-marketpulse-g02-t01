
# Checkpoint A - Foundations

## Student

- Name: Alexis Jacques
- GitHub: @Droopysss
- TD Group: G02
- Team: T01
- Repository: esilv-marketpulse-g02-t01

## Contribution

- Branch: `feature/display-observation-dates`
- Main commits:
  - `e59c7d3` - refactor: reuse market summary display
  - `a6a4775` - docs: add team information
  - `4ae974d` - feat: display first and last observation dates

## Work completed

### TD01 - Bootstrap and Linux

I accessed the team repository and created my own GitHub Codespace.
I used Linux commands such as pwd, ls, cd, cat, head and grep to navigate
the project and explore the CSV and JSON files.

I also completed the TEAM.md file with the information of our team.

### TD02 - Python, CSV and JSON

I worked on the main.py file to load market data and display a summary
for Apple and the S&P 500.

I implemented the following functions:

- get_first_close()
- get_last_close()
- display_market_summary()

The summary function is reused for both the instrument and the benchmark.
The closing prices are converted from strings to floats.

### TD03 - Git local workflow

I learned how to inspect, stage and commit my changes using Git.

I used git status, git diff, git add, git diff --staged,
git commit, git log and git show HEAD.

I checked that MarketPulse was still working before creating my commit.

### TD04 - Branches and merge

I created the branch feature/display-observation-dates to work
on a new feature without directly modifying main.

I implemented two new functions:

- get_first_date()
- get_last_date()

I updated the market summary to display the first and last observation
dates for both Apple and the S&P 500.

After testing the program, I committed my changes and compared the
feature branch with main.

I then merged the feature branch into main.
Git performed a fast-forward merge because main had not changed
since the feature branch was created.

The program still worked after the merge.
I captured the branch evidence before deleting the merged branch.

## Main difficulty

One of my main difficulties was understanding the different Git states,
especially the difference between modified files, staged changes
and committed changes.

I also had to understand the difference between the Python interpreter
and the Linux terminal.

During TD04, I learned how branches allow us to develop a feature
independently and integrate it into main when it is ready.

## Results

MarketPulse runs successfully with:

`python src/main.py`

The results obtained from the sample data are:

| Information | AAPL | SP500 |
|---|---|---|
| Observations | 21 | 21 |
| First date | 2026-09-01 | 2026-09-01 |
| Last date | 2026-09-30 | 2026-09-30 |
| First close | 250.00 USD | 6600.00 |
| Last close | 266.20 USD | 6742.00 |

## Evidence

- `01_terminal_python.png`
- `02_git_status_log.png`
- `03_branch_merge.png`
