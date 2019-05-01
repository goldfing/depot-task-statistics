CREATE KEYSPACE "depot_task_statistics" WITH REPLICATION = {'class': 'SimpleStrategy','replication_factor': 1};

USE "depot_task_statistics";


CREATE TABLE "depot_task_statistics"."daily_task_status_count" (
"task_date" DATE,
"depot" VARCHAR,
"task_status" VARCHAR,
"task_count" COUNTER,
PRIMARY KEY (task_date, depot, task_status)
);

CREATE TABLE "depot_task_statistics"."daily_task_status_list" (
"task_date" DATE,
"depot" VARCHAR,
"task_status" VARCHAR,
"task_no_list" LIST<text>,
PRIMARY KEY (task_date, depot, task_status)
);
