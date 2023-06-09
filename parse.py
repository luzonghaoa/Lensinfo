import re
import csv

dicts = [{'Name': 'XF14mmF2.8 R', 'Weight': '235g'}, {'Name': 'XF16mmF1.4 R WR', 'Weight': '375g'}, {'Name': 'XF16mmF2.8 R WR', 'Weight': '155g'}, {'Name': 'XF18mmF1.4 R LM WR', 'Weight': '370g'}, {'Name': 'XF18mmF2 R', 'Weight': '116g'}, {'Name': 'XF23mmF1.4 R', 'Weight': '300g'}, {'Name': 'XF23mmF1.4 R LM WR', 'Weight': '375g'}, {'Name': 'XF23mmF2 R WR', 'Weight': '180g'}, {'Name': 'XF27mmF2.8 R WR', 'Weight': '84g'}, {'Name': 'XF30mmF2.8 R LM WR Macro', 'Weight': '195g'}, {'Name': 'XF33mmF1.4 R LM WR', 'Weight': '360g'}, {'Name': 'XF35mmF1.4 R', 'Weight': '187g'}, {'Name': 'XF35mmF2 R WR', 'Weight': '170g'}, {'Name': 'XF50mmF1.0 R WR', 'Weight': '845g'}, {'Name': 'XF50mmF2 R WR', 'Weight': '200g'}, {'Name': 'XF56mmF1.2 R WR', 'Weight': '445g'}, {'Name': 'XF56mmF1.2 R APD', 'Weight': '405g'}, {'Name': 'XF60mmF2.4 R Macro', 'Weight': '215g'}, {'Name': 'XF80mmF2.8 R LM OIS WR Macro', 'Weight': '750g'}, {'Name': 'XF90mmF2 R LM WR', 'Weight': '540g'}, {'Name': 'XF200mmF2 R LM OIS WR', 'Weight': '2,265g'}, {'Name': 'XC35mmF2', 'Weight': '130g'}, {'Name': 'XF8-16mmF2.8 R LM WR', 'Weight': '805g'}, {'Name': 'XF10-24mmF4 R OIS WR', 'Weight': '385g'}, {'Name': 'XF16-55mmF2.8 R LM WR', 'Weight': '655g'}, {'Name': 'XF16-80mmF4 R OIS WR', 'Weight': '440g'}, {'Name': 'XF18-55mmF2.8-4 R LM OIS', 'Weight': '310g'}, {'Name': 'XF18-120mmF4 LM PZ WR', 'Weight': '460g'}, {'Name': 'XF18-135mmF3.5-5.6 R LM OIS WR', 'Weight': '490g'}, {'Name': 'XF50-140mmF2.8 R LM OIS WR', 'Weight': '995g'}, {'Name': 'XF55-200mmF3.5-4.8 R LM OIS', 'Weight': '580g'}, {'Name': 'XF70-300mmF4-5.6 R LM OIS WR', 'Weight': '580g'}, {'Name': 'XF100-400mmF4.5-5.6 R LM OIS WR', 'Weight': '1,375g'}, {'Name': 'XF150-600mmF5.6-8 R LM OIS WR', 'Weight': '1,605g'}, {'Name': 'XC15-45mmF3.5-5.6 OIS PZ', 'Weight': '135g'}, {'Name': 'XC50-230mmF4.5-6.7 OIS II'}]

pattern = r"(\d+(?:-\d+)?)(?:mm)?F([\d.-]+)"
for d in dicts:
    tmp = d['Name'].split(' ')
    name = tmp[0]
    match = re.search(pattern, name)
    #focal_length = match.group(1)
    #aperture = match.group(2)
    d['Focal_length'] = match.group(1) + 'mm'
    d['Aperture'] = 'F' + match.group(2)
    if 'LM' in tmp:
        d['LM'] = True
    else:
        d['LM'] = False
    if 'OIS' in tmp:
        d['OIS'] = True
    else:
        d['OIS'] = False
    if 'WR' in tmp:
        d['WR'] = True
    else:
        d['WR'] = False

print(dicts)
field_names = dicts[0].keys()
output_file = "output.csv"
with open(output_file, mode="w+", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=field_names)

    # Write the header row
    writer.writeheader()

    # Write the data rows
    writer.writerows(dicts)