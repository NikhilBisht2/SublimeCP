import sublime
import sublime_plugin
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

INPUT_PATH = r"PATH HERE"
OUTPUT_PATH = r"PATH HERE"
EXPECTED_PATH = r"PATH HERE"
SOLVE_CPP_PATH = r"PATH HERE"
PORT = 10045

SOLVE_CPP_TEMPLATE = """#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define endl '\\n'
#define YES cout << "YES" << endl
#define NO cout << "NO" << endl
#define all(a) a.begin(), a.end()
#define rall(a) a.rbegin(), a.rend()
#define vi vector<long long>
#define vvi vector<vi>
#define pii pair<ll, ll>
#define vpi vector<pair<ll, ll>>
#define pci pair<char, ll>
#define fo(i, x, n) for (ll i = x; i < n; i++)
#define pb push_back
#define pqx priority_queue
#define umap unordered_map
#define setbits(x) __builtin_popcountll(x)
constexpr ll mod = 1e9 + 7, inf = 1e18;
//---------------------------------------------------//
void solve() {}
//---------------------------------------------------//
int32_t main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
#ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  ll t = 1;
  cin >> t;
  while (t--)
    solve();
  return 0;
}
"""

server_instance = None

class CCRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_len = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_len).decode('utf-8')

            data = json.loads(body)

            tests = data.get("tests", [])

            if len(tests) == 0:
                print("CompetitiveHelper: No tests received")
                return

            input_data = tests[0].get("input", "")
            expected_output = tests[0].get("output", "")

            with open(INPUT_PATH, "w", encoding="utf-8") as f:
                f.write(input_data)

            with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
                f.write("")

            with open(EXPECTED_PATH, "w", encoding="utf-8") as f:
                f.write(expected_output)

            with open(SOLVE_CPP_PATH, "w", encoding="utf-8") as f:
                f.write(SOLVE_CPP_TEMPLATE)

            print("CompetitiveHelper: Test case and solve.cpp saved!")

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
        except Exception as e:
            print("CompetitiveHelper: ERROR -> {}".format(e))


class StartCcServerCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        global server_instance

        if server_instance:
            print("CompetitiveHelper: Server already running.")
            return

        def server_thread():
            global server_instance
            server_instance = HTTPServer(('127.0.0.1', PORT), CCRequestHandler)
            print("CompetitiveHelper: Listening on 127.0.0.1:{}".format(PORT))
            server_instance.serve_forever()

        thread = threading.Thread(target=server_thread, daemon=True)
        thread.start()
        print("CompetitiveHelper: Server started")
