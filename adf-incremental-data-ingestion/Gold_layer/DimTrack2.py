import dlt

@dlt.table()

def DimTrack_stg():
    df = spark.readStream.table("spotify_cata.silver.dimtrack")
    return df


dlt.create_streaming_table("dimtrack")

dlt.create_auto_cdc_flow(
    target ="dimtrack",
    source = "DimTrack_stg",
    keys = ["track_id"],
    sequence_by = "updated_at",
    once = False,
    stored_as_scd_type = 2
) 