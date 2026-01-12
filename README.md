# Phishing-URL-Detector
Machine Learning scanner to detect phishing URLs

This detector is using the RandomForestClassifier model trained against the Kaggle phishing URL dataset.

Example output:

Loading data... 

--- First 5 Rows ---

URL Label
                                                 
0  nobell.it/70ffb52d079109dca5664cce6f317373782/...   bad

1  www.dghjdgf.com/paypal.co.uk/cycgi-bin/webscrc...   bad

2  serviciosbys.com/paypal.cgi.bin.get-into.herf....   bad

3  mail.printakid.com/www.online.americanexpress....   bad

4  thewhiskeydregs.com/wp-content/themes/widescre...   bad




--- Extracting Features ---

URL  url_length  dot_count  has_suspicious_words Label

0  nobell.it/70ffb52d079109dca5664cce6f317373782/...         225          6                     1   bad

1  www.dghjdgf.com/paypal.co.uk/cycgi-bin/webscrc...          81          5                     0   bad

2  serviciosbys.com/paypal.cgi.bin.get-into.herf....         177          7                     1   bad

3  mail.printakid.com/www.online.americanexpress....          60          6                     0   bad

4  thewhiskeydregs.com/wp-content/themes/widescre...         116          1                     0   bad


  Label  target

0   bad       1

1   bad       1

2   bad       1

3   bad       1

4   bad       1

Training-data dimensions(Row, Column): (439476, 11)

Test-data dimensions(Rows, Columns): (109870, 11)

Overall Model Accuracy: 0.8565759533994721

--- Confusion Matrix ---

Safe Sites: 69521

Mistaken: 9064

Missing Sites (CRITICAL DANGER): 6694

Sites Caught: 24591

--- AI Clue Rankings ---

url_length: 0.2268

dot_count: 0.1069

has_suspicious_words: 0.1145

dash_count: 0.0937

at_count: 0.0035

slash_count: 0.1357

has_ip: 0.0198

is_https: 0.0000

subdomain_count: 0.0531

risky_tld: 0.0171

digit_count: 0.2288

Enter Suspicious URL:http://google.com.cust_login.ie

**
 ALERT >> PHISHING URL! 
**
