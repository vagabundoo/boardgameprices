# Create a pandas dataframe with demo data:
import pandas as pd
demodata_csv = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
df = pd.read_csv(demodata_csv)
import

from relevantstats import dfc
dfc = dfc[:100]

# Pretty print the dataframe as an html table to a file
intermediate_html = '../input/intermediate.html'
# to_html_pretty(dfc,intermediate_html,'Iris Data')
# if you do not want pretty printing, just use pandas:
dfc.to_html(index=False, columns=['rank', 'names', 'year', 'avgPrice'])

# Convert the html file to a pdf file using weasyprint
import weasyprint
out_pdf= '/home/edu/Downloads/test.pdf'
weasyprint.HTML(intermediate_html).write_pdf(out_pdf)

