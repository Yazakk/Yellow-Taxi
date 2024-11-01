-- 1.Total Revenue Calculation
SELECT SUM(fare_amount + extra + improvement_surcharge + congestion_surcharge + airport_fee) AS tpep_revenue
FROM "NYC_Yellow_Taxi_Trip_20203_01"
WHERE payment_type IN (1, 2, 5)
  AND tpep_dropoff_datetime BETWEEN 
      (SELECT MAX(tpep_dropoff_datetime) - INTERVAL '30 days' FROM "NYC_Yellow_Taxi_Trip_20203_01")
      AND (SELECT MAX(tpep_dropoff_datetime) FROM "NYC_Yellow_Taxi_Trip_20203_01");

-- Result 65357329.3400042

-- 2.Top 3 Pickup Locations

SELECT "PULocationID", 
       SUM(fare_amount + extra + improvement_surcharge + congestion_surcharge + airport_fee) AS tpep_revenue
FROM "public"."NYC_Yellow_Taxi_Trip_20203_01"
WHERE payment_type IN (1, 2, 5)
  AND tpep_dropoff_datetime BETWEEN 
      (SELECT MAX(tpep_dropoff_datetime) - INTERVAL '30 days' FROM "public"."NYC_Yellow_Taxi_Trip_20203_01")
      AND (SELECT MAX(tpep_dropoff_datetime) FROM "public"."NYC_Yellow_Taxi_Trip_20203_01")
GROUP BY "PULocationID"
ORDER BY tpep_revenue DESC
LIMIT 3;
/* Result
 PULocationID |   tpep_revenue    
--------------+-------------------
          132 | 9201855.03999997
          138 | 4199235.310000007
          161 | 2564209.50999999
*/