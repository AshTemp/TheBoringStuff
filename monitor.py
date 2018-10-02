import subprocess

partition_usage_threshold = 5
df_cmd = subprocess.check_output(["df", "-k"])
# print df_cmd
lines = df_cmd.splitlines()
# print lines
for line in lines[1:]:
    columns = line.split()
    used_percentage = columns[4]
    used_percentage = used_percentage.replace("%", "")
    if int(used_percentage) >= partition_usage_threshold:
        print("partitions {1}s is beyond threshold at {2}s").format(
            columns[0], columns[4]
        )
