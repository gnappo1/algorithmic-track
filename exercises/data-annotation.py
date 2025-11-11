import requests
from bs4 import BeautifulSoup  # (pip install beautifulsoup4)

def render_secret_message(url: str) -> str:
    html = requests.get(url, timeout=20).text
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table")
    if not table:
        raise ValueError("No table found")

    rows = table.find_all("tr")
    headers = [th.get_text(strip=True).lower() for th in rows[0].find_all(["th", "td"])]
    xi, yi, ci = headers.index("x-coordinate"), headers.index("y-coordinate"), headers.index("character")

    points = {}
    max_x = max_y = 0
    for tr in rows[1:]:
        cells = [td.get_text(strip=True) for td in tr.find_all(["td", "th"])]
        # if not cells: 
        #     continue
        x, y, ch = int(cells[xi]), int(cells[yi]), cells[ci] or " "
        points[(x, y)] = ch
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    width, height = max_x + 1, max_y + 1
    grid = [[" "] * width for _ in range(height)]
    for (x, y), ch in points.items():
        grid[y][x] = ch

    art = "\n".join("".join(row) for row in grid)
    print(art)
    return art

render_secret_message("https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub")




# import csv
# import io
# import requests
# import re

# try:
#     from bs4 import BeautifulSoup 
# except ImportError:
#     BeautifulSoup = None

# def render_secret_message(url: str) -> str:
#     """
#     Fetches a published Google Doc (CSV/TSV-like) listing characters with x,y,
#     then prints and returns the fixed-width graphic.
#     Expected columns (case-insensitive): char, x, y
#     """
#     resp = requests.get(url, timeout=20)
#     resp.raise_for_status()
#     raw = resp.text
#     content_type = resp.headers.get("Content-Type", "")

#     rows = []

#     if "html" in content_type.lower() or raw.lstrip().lower().startswith("<!doctype"):
#         if BeautifulSoup is None:
#             raise RuntimeError(
#                 "This URL returns HTML. Please `pip install beautifulsoup4` "
#                 "or convert the document to CSV/TSV."
#             )
#         rows = _parse_html_table(raw)
#     else:
#         rows = _parse_csv_tsv(raw)

#     points = {}
#     max_x = max_y = 0

#     for r in rows:
#         keymap = {k.strip().lower(): (v if v is not None else "") for k, v in r.items()}
#         ch = keymap.get("char") or keymap.get("character") or keymap.get("unicode") or " "
#         x_key = _match_key(keymap.keys(), r"^x\b")
#         y_key = _match_key(keymap.keys(), r"^y\b")
        
#         if x_key is None or y_key is None:
#             continue
#         x = int(keymap[x_key])
#         y = int(keymap[y_key])

#         points[(x, y)] = ch
#         if x > max_x: 
#             max_x = x
#         if y > max_y: 
#             max_y = y

#     width, height = max_x + 1, max_y + 1
#     grid = [[" "] * width for _ in range(height)]

#     for (x, y), ch in points.items():
#         if 0 <= x < width and 0 <= y < height:
#             grid[y][x] = ch

#     art = "\n".join("".join(row) for row in grid)
#     print(art)
#     return art

# def _parse_csv_tsv(raw: str):
#     try:
#         sample = "\n".join(raw.splitlines()[:3]) or "char,x,y"
#         dialect = csv.Sniffer().sniff(sample)
#     except csv.Error:
#         dialect = csv.get_dialect("excel")
#     reader = csv.DictReader(io.StringIO(raw), dialect=dialect)
#     return [row for row in reader if any((row or {}).values())]

# def _parse_html_table(html: str):
#     soup = BeautifulSoup(html, "html.parser")
#     table = soup.find("table")
#     if not table:
#         raise ValueError("No table found in the provided HTML document.")

#     header_cells = table.find("tr").find_all(["th", "td"])
#     headers = [cell.get_text(strip=True) for cell in header_cells]
#     rows = []

#     for tr in table.find_all("tr")[1:]:
#         cells = tr.find_all(["td", "th"])
#         if not cells:
#             continue
#         vals = [cell.get_text(strip=True) for cell in cells]

#         if len(vals) < len(headers):
#             vals += [""] * (len(headers) - len(vals))
#         elif len(vals) > len(headers):
#             vals = vals[:len(headers)]
#         rows.append(dict(zip(headers, vals)))
#     return rows

# def _match_key(keys, pattern: str):
#     prog = re.compile(pattern, re.I)
#     for k in keys:
#         if prog.search(k):
#             return k
#     return None

# render_secret_message(
#     "https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub"
# )