import json
from pathlib import Path


def test_report_exists():
    """1) The agent produces a report file and writes it to absolute path /app/report.json."""
    assert Path("/app/report.json").exists(), "no report.json found"


def test_total_requests():
    """2) The report should contain total number of counted requests."""
    assert Path("/app/report.json").exists(), "report.json is not found"
    with open("/app/report.json") as f:
        data = json.load(f)
    assert data.get("total_requests") == 6, f"expected total_counted_requests to be 6, got {data.get('total_requests')}"


def test_unique_ips():
    """3) The report should contain the correct counted unique IP addresses."""
    assert Path("/app/report.json").exists(), "report.json is not found"
    with open("/app/report.json") as f:
        data = json.load(f)
    assert data.get("unique_ips") == 3, f"expected unique_IPs to be 3, got {data.get('unique_ips')}"


def test_top_path():
    """4) The report should specify the most request URL path."""
    assert Path("/app/report.json").exists(), "report.json is not found"
    with open("/app/report.json") as f:
        data = json.load(f)
    assert data.get("top_path") == "/index.html", f"expected top_path to be '/index.html', got {data.get('top_path')}"
