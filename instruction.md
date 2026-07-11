Analyze the access log located in a working directory /app/access/log. Parse the small access log, calculate and give summary statistics. Save the report as path /app/report.json 

The written report must be a JSON object include in its solution the following keys:
- total_requests (integer value): This is the total number of requests found in the access log
- unique_ips (integer value): The number of unique IP addresses found in the log.
- top_path (string): This is the address of the webpage (URL path) that was accessed the highest number of times across all requests. 

The following success criteria will be used to validate work done. 
1. Read all entries from access.log
2. The report must show the correct number matching total requests
3. The report should have the correct total number of unique IPs in the log
4. The absolute path /app/report.json is present and contains valid JSON
5. The report must state the single most requested URL path in the log
