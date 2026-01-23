import dlt

@dlt.table()

def DimDate_stg():
    df = spark.readStream.table("spotify_cata.silver.dimdate")
    return df


dlt.create_streaming_table("dimdate")

dlt.create_auto_cdc_flow(
    target ="dimdate",
    source = "DimDate_stg",
    keys = ["date_key"],
    sequence_by = "date",
    once = False,
    stored_as_scd_type = 2
) 