import pandas as pd
import sqlite3

months = ['2015-01']

for month in months:
    connection = sqlite3.connect('{}.db'.format(month))
    c = connection.cursor()
    limit= 5000
    last_unix= 0
    cur_length = limit
    counter= 0
    test_done= False
    while cur_length == limit:
        df =pd.read_sql("SELECT * FROM parent_reply WHERE unix > {} AND parent NOT NULL AND score > 0 ORDER BY unix ASC\
                         limit {}". format(last_unix, limit), connection)
        last_unix = df.tail(1)['unix'].values[0]
        cur_length = len(df)
        if not test_done:
            with open("test.from", 'a', encoding='utf8') as f:
                for content in df['parent'].values:
                    f.write(content+'\n')
            with open("test.to", 'a', encoding='utf8') as f:
                for content in df['comment'].values:
                    f.write(content+'\n')
            #Trigger next step once the initial 5000 commits have been made, allowing for the train data to be established
            test_done= True
        
        else:
            with open("train.from", 'a', encoding='utf8') as f:
                for content in df['parent'].values:
                    f.write(content+ '\n')
            with open("train.to", 'a', encoding='utf8') as f:
                for content in df['comment'].values:
                    f.write(content+ '\n')

        counter += 1
        if counter % 20==0:
            print(counter*limit, 'rows completed')