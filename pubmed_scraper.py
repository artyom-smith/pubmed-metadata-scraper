from datetime import datetime as dt
from Bio import Entrez
import pandas as pd

def pubmed_articles_finder (search_value: str, count: int) -> None:
  """
    Queries PubMed database, processes metadata, and saves results to Excel.

    This function authenticates with the NCBI Entrez API, translates the search query, extracts relevant metadata (authors, title, journal, year, doi, etc.) for a specified number of articles, and formats the author list according to standard academic citation rules (truncating to 'et al.' if >= 6 authors).

    Args:
      search_value: The keywords, MeSH terms, or author names to search for.
      count: The maximum number of articles to retrieve.

    Returns:
      None. Saves the generated structured data into an Excel (.xlsx) file.
  """

  # API configuration
  Entrez.email = ''
  Entrez.api_key = ''
  Entrez.tool = "MyMedtechScraper"

  # Search for article IDs
  handle = Entrez.esearch(db='pubmed', term=search_value, retmax=count)
  result = Entrez.read(handle)
  handle.close()

  print('Input > ' + str(result['QueryTranslation']))

  # Fetch summaries for the retrieved IDs
  handle = Entrez.esummary(db='pubmed', id=result['IdList'])
  result = Entrez.read(handle)
  handle.close()

  articles_list = []

  # Process and format metadata
  for i in result:
    # Format authors: truncate to 'et al.' if there are 6 or more
    if len(i['AuthorList']) >= 6: author = str(', '.join(i['AuthorList'][0:5])) + ', et al.'
    else: author = ', '.join(i['AuthorList'])

    articles_list.append({
        'Author': author,
        'Title': i.get('Title', 'No Title'),
        'Journal': i.get('Source', 'Unknown Journal'),
        'Year': i.get('PubDate', '0000').split(' ')[0],
        'Issue': i.get('Issue') if i.get('Issue') else '-',
        'Volume': i.get('Volume') if i.get('Volume') else '-',
        'Pages': i.get('Pages') if i.get('Pages') else '-',
        'DOI': i.get('DOI', '-') if i.get('DOI') else '-'
    })

  # Export data to an Excel spreadsheet
  df = pd.DataFrame(articles_list)
  file_name = search_value.split()[0].strip() + ' | ' + str(dt.now().strftime("%Y-%m-%d")) + '.xlsx'
  df.to_excel(file_name, index=False)
  print('Done! Result saved in file ' + file_name)


search_value = input('Enter your search > ')

while True:
  try:
    count = int(input('Enter articles count > '))
    break
  except:
    print('Error! You need to enter integer!')
