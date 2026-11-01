"""엑셀 '장르 목록' 시트의 Suno 공유 링크를 읽어 samples.js 를 다시 만듭니다.

사용법:  python tools/excel_to_samples.py "장르샘플_제작가이드_Suno링크.xlsx"

- F열(샘플 ID)과 J열(Suno 공유 링크)을 읽습니다.
- https://suno.com/s/xxxx 같은 짧은 링크는 Suno에 접속해 실제 곡 ID로 바꿉니다.
- https://suno.com/song/<곡 ID> 형태는 그대로 곡 ID를 꺼냅니다.
"""
import json, re, sys, urllib.request, urllib.error
from pathlib import Path
from openpyxl import load_workbook

UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None

def song_id(link):
    link = link.strip()
    m = UUID.search(link)
    if m:
        return m.group(0)
    if "suno.com/s/" in link:
        opener = urllib.request.build_opener(NoRedirect)
        req = urllib.request.Request(link, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
        try:
            opener.open(req, timeout=15)
        except urllib.error.HTTPError as e:
            m = UUID.search(e.headers.get("Location", ""))
            if m:
                return m.group(0)
    return None

def main(xlsx):
    ws = load_workbook(xlsx)["장르 목록"]
    out, bad = {}, []
    for r in range(5, ws.max_row + 1):
        sid, link, name = ws.cell(r, 6).value, ws.cell(r, 10).value, ws.cell(r, 4).value
        if not sid or not link or not str(link).startswith("http"):
            continue
        sid_ = song_id(str(link))
        if sid_:
            out[sid] = sid_
        else:
            bad.append(f"{r}행 {name}: {link}")
    root = Path(__file__).resolve().parent.parent
    body = ",\n".join(f"  {json.dumps(k)}: {json.dumps(v)}" for k, v in out.items())
    (root / "samples.js").write_text(
        "/* Suno 장르 샘플 목록 (자동 생성 파일)\n"
        "   샘플 ID(장르 영문명 기준) : Suno 곡 ID\n"
        "   tools/excel_to_samples.py 로 '장르샘플_제작가이드_Suno링크.xlsx'에서 다시 만들 수 있습니다. */\n"
        "window.SUNO_SAMPLES = {\n" + body + "\n};\n", encoding="utf-8")
    print(f"샘플 {len(out)}개를 samples.js 에 저장했습니다.")
    if bad:
        print("곡 ID를 찾지 못한 링크:")
        print("\n".join("  " + b for b in bad))

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "장르샘플_제작가이드_Suno링크.xlsx")
