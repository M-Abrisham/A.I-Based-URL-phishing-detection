import pandas as pd


def translator(Label):
    if Label == "bad":
       return 1
    else:
       return 0



# 1. Load Dataset
print("Loading data... ")
df = pd.read_csv('phishing_site_urls.csv')

# 2. check first rows
print("\n--- First 5 Rows ---")
print(df.head())

# 3. Create New data from URL
print("\n--- Extracting Features ---")

# Feature 1: URL Length 
df['url_length'] = df['URL'].apply(lambda x: len(str(x)))

# Feature 2: Number of dots
df['dot_count'] = df['URL'].apply(lambda x: str(x).count('.'))
df['target'] = df['Label'].apply(translator)

# Feature 3: Suspicious words
suspicious_words = ['secure', 'login', 'update', 'banking']
def check_suspicious(url):
    if str(url) == suspicious_words:
      return 1
    else:
      return 0

df['has_suspicious_words'] = df['URL'].apply(check_suspicious)

# 4. Result
print(df[['URL','url_length', 'dot_count', 'has_suspicious_words', 'Label']].head())
print(df[['Label' , 'target']].head())