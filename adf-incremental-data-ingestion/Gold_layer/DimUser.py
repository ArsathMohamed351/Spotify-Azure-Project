import dlt

expectation = {
    "rule_1" : "user_id IS NOT NULL"
}
@dlt.table()
@dlt.expect_all_or_drop(expectation)

def DimUser_stg():
    df = spark.readStream.table("spotify_cata.silver.dimuser")
    return df


dlt.create_streaming_table("dimuser")

dlt.create_auto_cdc_flow(
    target ="dimuser",
    source = "DimUser_stg",
    keys = ["user_id"],
    sequence_by = "updated_at",
    once = False,
    stored_as_scd_type = 2
) 