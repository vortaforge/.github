#!/usr/bin/env python3
"""Arşivi geri alma aracı.

Kullanım (hiçbir şey yazmadan önce `--apply` şart):

  python3 restore.py --list
  python3 restore.py --unarchive --apply                  # arşivi kaldır
  python3 restore.py --visibility public --apply          # herkese aç
  python3 restore.py --meta --apply                       # açıklama/topics/ayarlar
  python3 restore.py --transfer-back --apply              # eski sahibine geri taşı
  python3 restore.py --all --apply                        # hepsi sırayla
  python3 restore.py --unarchive hardtools --apply        # tek depo

Token: GITHUB_TOKEN ortam değişkeni ya da --token-file <yol>.
`repo` + `admin:org` kapsamları gerekir. Token hiçbir yere yazılmaz, çıktıya basılmaz.
"""
import argparse, json, os, sys, urllib.error, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
API = "https://api.github.com"


def token(args):
    if args.token_file:
        return open(args.token_file).read().strip()
    t = os.environ.get("GITHUB_TOKEN", "").strip()
    if not t:
        sys.exit("GITHUB_TOKEN yok (ya da --token-file ver).")
    return t


def call(tok, path, method="GET", body=None):
    req = urllib.request.Request(API + path, method=method,
                                 data=json.dumps(body).encode() if body else None,
                                 headers={"accept": "application/vnd.github+json",
                                          "authorization": f"Bearer {tok}",
                                          "x-github-api-version": "2022-11-28",
                                          "user-agent": "hardtools-restore"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, (json.load(r) if r.status != 204 else {})
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.load(e)
        except Exception:
            return e.code, {}


def load():
    exports = os.path.join(HERE, "exports")
    index = json.load(open(os.path.join(exports, "index.json")))
    rows = []
    for entry in index["repos"]:
        rec = json.load(open(os.path.join(exports, entry["name"] + ".json")))
        plan = None
        for item in json.load(open(os.path.join(HERE, "transfer-plan.json")))["items"]:
            if item["target_name"] == entry["name"]:
                plan = item
                break
        rows.append({"rec": rec, "plan": plan, "name": entry["name"],
                     "origin": (plan or {}).get("source", "")})
    return rows


def pick(rows, names):
    return rows if not names else [r for r in rows if r["name"] in names or r["origin"] in names]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("names", nargs="*", help="depo adları (boşsa hepsi)")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--unarchive", action="store_true")
    ap.add_argument("--archive", action="store_true")
    ap.add_argument("--visibility", choices=["public", "private"])
    ap.add_argument("--meta", action="store_true")
    ap.add_argument("--transfer-back", dest="transfer_back", action="store_true")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--apply", action="store_true", help="yaz; yoksa yalnız plan gösterilir")
    ap.add_argument("--token-file")
    args = ap.parse_args()

    rows = pick(load(), args.names)
    if args.list or not any([args.unarchive, args.archive, args.visibility, args.meta, args.transfer_back, args.all]):
        for r in rows:
            rec = r["rec"]
            print(f"{r['name']:<34} eski={r['origin']:<34} private={rec.get('private')} archived={rec.get('archived')}")
        return
    if args.all:
        args.unarchive = args.meta = args.transfer_back = True
    tok = token(args)
    org = "tickwarden-archived"
    for r in rows:
        name, rec, plan = r["name"], r["rec"], r["plan"] or {}
        full = f"{org}/{name}"
        acts = []
        if args.unarchive or args.all:
            code, _ = call(tok, f"/repos/{full}", "PATCH", {"archived": False})
            acts.append(f"unarchive:{code}")
        if args.archive:
            code, _ = call(tok, f"/repos/{full}", "PATCH", {"archived": True})
            acts.append(f"archive:{code}")
        if args.visibility:
            code, _ = call(tok, f"/repos/{full}", "PATCH", {"private": args.visibility == "private"})
            acts.append(f"visibility:{code}")
        if args.meta:
            body = {k: rec[k] for k in ("description", "homepage", "has_issues", "has_wiki", "has_projects") if rec.get(k) is not None}
            if rec.get("topics"):
                body["topics"] = rec["topics"]
            code, _ = call(tok, f"/repos/{full}", "PATCH", body)
            acts.append(f"meta:{code}")
        if args.transfer_back and plan.get("source"):
            owner, orig = plan["source"].split("/")
            body = {"new_owner": owner}
            if plan.get("renamed"):
                body["new_name"] = orig
            code, _ = call(tok, f"/repos/{full}/transfer", "POST", body)
            acts.append(f"transfer->{owner}:{code}")
        print(f"{name:<34} {' '.join(acts) if args.apply else 'PLAN: ' + ','.join(k for k in
              (['unarchive'] if args.unarchive else []) + (['archive'] if args.archive else []) +
              ([f'visibility={args.visibility}'] if args.visibility else []) +
              (['meta'] if args.meta else []) + (['transfer-back'] if args.transfer_back else []))}")


if __name__ == "__main__":
    main()
