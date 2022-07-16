import pandas as pd


def read_in_chunks(file_object, chunk_size=1024, sep='*', header=None):
    csv_reader = pd.read_csv(
        file_object,
        sep=sep,
        iterator=True,
        chunksize=chunk_size,
        header=header
    )

    for line in csv_reader:
        chunk = pd.DataFrame(line)
        yield chunk
