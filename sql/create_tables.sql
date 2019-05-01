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
