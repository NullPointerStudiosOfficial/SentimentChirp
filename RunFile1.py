import webbrowser


def get_file(days):
    file = open("data.html", "w")

    show = "true"
    marker_size = 0
    name = "Trump"

    mid = "," \
          "\n    data: [{" \
          "\n        type: \"line\"," \
          "\n        axisYType: \"secondary\"," \
          "\n        name: " + "\"" + name + "\"" + "," \
          "\n        showInLegend: " + show + "," \
          "\n        markerSize: " + marker_size.__str__() + "," \
          "\n        yValueFormatString: \"Sentiment ,\"," \
          "\n        dataPoints: ["

    for date in days:
        mid += "\n        {x: new Date(" + str(date.year) + ", " + str(date.month) + ", " + str(date.day) + "), y: " + str(date.sentiment) + "},"

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
            "\n    axisX: {" \
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
           "\n<body>" \
           "\n<form name=\"search\" action=\"RunFile.py\" method=\"get\">" \
           "\n<input type=\"text\" data_test=\"twitter_handle\" style=\"height: 50px; width: 50%; margin-left: 25%; margin-top: 5%;\">" \
           "\n</form>" \
           "\n  <div id=\"chartContainer\" style=\"height: 370px; width: 80%; margin-top: 10%; margin-left: 10%;\"></div>" \
           "\n	<script src=\"graph.js\"></script>" \
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
    def __init__(self,year, month, day, s):
        self.year = year
        self.month = month
        self.day = day
        self.sentiment = s


days = [Date(2019,1,1, .4), Date(2019,1,1,.2),Date(2019,1,2,-.3),Date(2019,1,3,.1),Date(2019,1,4,.6),Date(2019,1,4,-.3) \
    , Date(2019, 1, 5, -.8), Date(2019, 1, 6, .1), Date(2019, 1, 7, -.6),Date(2019,1,7,.2),Date(2019,1,7,.9)]

webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new_tab(get_file(days).name)

print(get_file(days))
