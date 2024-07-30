#!/usr/bin/env python

"""This module calculates the grades for the undergrad school as needed."""

from bs4 import BeautifulSoup

with open("pages/grades.html", "r") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

TOTAL_GRADE = 0
TOTAL_CREDITS = 0

for row in soup.find_all(class_="column_odd"):
    tds = row.find_all("td")
    year = tds[6].get_text(strip=True)
    # if tds[3].get_text(strip=True) and (
    #     (tds[7].get_text(strip=True)[0] == "S" and year == "2020")
    # ):
    if tds[3].get_text(strip=True):
        credit = int(tds[3].get_text())
        grade_l = tds[5].get_text(strip=True)
        if grade_l == "AA":
            TOTAL_GRADE += credit * 4
        elif grade_l == "A":
            TOTAL_GRADE += credit * 3
        elif grade_l == "B":
            TOTAL_GRADE += credit * 2
        elif grade_l == "C":
            TOTAL_GRADE += credit * 1
        elif grade_l == "D":
            TOTAL_GRADE += credit * 0
            # continue
        else:
            continue
        TOTAL_CREDITS += credit

print(TOTAL_GRADE, TOTAL_CREDITS, TOTAL_GRADE / TOTAL_CREDITS)
