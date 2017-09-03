import pandas
import os


def build_csv():
    DATA_DIR = "data"
    # String a formatear con los archivos de los datos
    filename = "properati-AR-{0}-{1}-01-properties-sell.csv"
    filepath = os.path.join(DATA_DIR, filename)

    data_frames = pandas.read_csv(filepath.format(
        str(2013), str(8).zfill(2)), low_memory=False)

    for year in range(2013, 2018):
        for month in range(1, 13):
            if year == 2013 and month < 8:
                continue
            try:
                tmp_df = pandas.read_csv(filepath.format(str(year),
                                         str(month).zfill(2)),
                                         low_memory=False)
                if 'image_thumbnail' in tmp_df:
                    del tmp_df['image_thumbnail']
                if 'properati_url' in tmp_df:
                    del tmp_df['properati_url']
                if 'description' in tmp_df:
                    del tmp_df['description']

                data_frames = pandas.concat([data_frames, tmp_df])
            except IOError:
                pass
    data_frames.to_csv("data/full_data.csv")

build_csv()
