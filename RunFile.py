import cgi
import webbrowser

import testing


def get_file(days, search_term):
    file = open("data.php", "w")

    name = search_term.__str__()

    mid = "," \
          "\n    data: [{" \
          "\n        type: \"line\"," \
          "\n        axisYType: \"secondary\"," \
          "\n        name: " + "\"" + name + "\"" + "," \
                                                    "\n        showInLegend: true," \
                                                    "\n        markerSize: 0," \
                                                    "\n        yValueFormatString: \"# Sentiments,\"," \
                                                    "\n        dataPoints: ["

    for date in days:
        mid += "\n        {x: new Date(" + str(date.year) + ", " + str(date.month) + ", " + str(
            date.day) + "), y: " + str(date.sentiment) + "},"

    mid += "\n       ]" \
           "\n    }]"

    front = "\n<!DOCTYPE HTML> " \
            "\n<html>" \
            "\n<head>" \
            "\n<script>" \
            "\nwindow.onload = function () {" \
            "\nvar chart = new CanvasJS.Chart(\"chartContainer\", {" \
            "\n   title: {" \
            "\n        text: \"Popularity\"" \
            "\n    }," \
            "\n    axisX: {	  " \
            "\n       valueFormatString: \"DDDD\"" \
            "\n    }," \
            "\n    axisY2: {" \
            "\n        title: \"Tweets\"," \
            "\n        suffix: \" Tweets\"" \
            "\n    }," \
            "\n    toolTip: {" \
            "\n        shared: true" \
            "\n    }," \
            "\n    legend: {" \
            "\n        cursor: \"pointer\"," \
            "\n        verticalAlign: \"top\"," \
            "\n        horizontalAlign: \"center\"," \
            "\n        dockInsidePlotArea: true," \
            "\n        itemclick: toogleDataSeries" \
            "\n    }"

    back = "\n});" \
           "\nchart.render();" \
           "\nfunction toogleDataSeries(e){" \
           "\n if (typeof(e.dataSeries.visible) === \"undefined\" || e.dataSeries.visible    ) {" \
           "\n     e.dataSeries.visible = false;" \
           "\n } else{" \
           "\n     e.dataSeries.visible = true;" \
           "\n }" \
           "\n chart.render();" \
           "\n}" \
           "\n}" \
           "\n </script>" \
           "\n</head>" \
           "\n <?php if (isset($_GET['hello'])) { exec('c:\WINDOWS\system32\cmd.exe /c START C:\MAMP\htdocs\RunFile.py'); } ?>" \
           "\n<body>" \
           "\n<form name=\"search\" method=\"get\">" \
           "\n      <input type=\"text\" data_test=\"twitter_handle\" style=\"height: 50px; width: 50%; margin-left: 25%; margin-top: 5%;\">" \
           "\n</form>" \
           "\n<a href = \"?hello=true\">.</a>" \
           "\n  <div id=\"chartContainer\" style=\"height: 370px; width: 80%; margin-top: 10%; margin-left: 10%;\"></div>" \
           "\n	<script src=\"graph.js\"></script>" \
           "\n<a href = \"?hello=true\">.</a>" \
           "\n</body>" \
           "\n<style>" \
           "\n   input {" \
           "\n      font-size: 2em;" \
           "\n      text-align: center;" \
           "\n      border: 0;" \
           "\n      outline: 0;" \
           "\n      background: transparent;" \
           "\n      border-bottom: 1px solid black;" \
           "\n  }" \
           "\n</style>" \
           "\n</html>"

    html = front + mid + back

    with file as f:
        f.write(html)

    return file


class Date:
    def __init__(self, year, month, day, s):
        self.year = year
        self.month = month
        self.day = day
        self.sentiment = s

    def __str__(self):
        return str(self.year) + " " + str(self.month) + " " + str(self.day) + " " + str(self.sentiment)

    def getYear(self):
        return self.year


days = []


def main():
    form = cgi.FieldStorage()
    search_term = form.getvalue('searchbox')
    sentiments = testing.get_sentiment(search_term)

    for tweetday in sentiments:
        date = tweetday.get_date()
        days.append(Date(date[0:4], date[5:7], date[8:10], tweetday.sentiment))

    get_file(days, search_term)
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new_tab(
        "http://localhost:81/data.php")


if __name__ == "__main__":
    main()
