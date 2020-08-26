import pandas as pd
import glob


def concat_csv(directory, output_file_name):

    files = glob.glob(directory + '/*.csv')

    combined_csv = pd.concat([pd.read_csv(f) for f in files])

    combined_csv.to_csv(directory + '/' + output_file_name + '.csv',
                        index=False,
                        encoding='utf-8-sig')
