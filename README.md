CompetitiveHelper

CompetitiveHelper is a Sublime Text plugin that integrates with the Competitive Companion browser extension to automatically fetch problem input/output and prepare a ready-to-use C++ template for competitive programming.

Features

Automatically receives test cases from Competitive Companion.

Writes to the following files:

input.txt → problem input

output.txt → your solution output

e-output.txt → expected output

solve.cpp → ready-to-go C++ template

Customizable file paths.

Configurable port for Competitive Companion communication (default: 10045).

Compatible with Sublime Text 4 (Python 3.3).

Installation
1. Clone Repository

Clone this repository into Sublime Text's Packages directory:

Windows default path:

%APPDATA%\Sublime Text\Packages

git clone https://github.com/NikhilBisht2/SublimeCP.git CompetitiveHelper


Make sure the folder name inside Packages is CompetitiveHelper.

2. Configure Paths

Open CompetitiveHelper.py and set your file paths:

INPUT_PATH = r"<path_to_your_input_file>"
OUTPUT_PATH = r"<path_to_your_output_file>"
EXPECTED_PATH = r"<path_to_your_expected_output_file>"
SOLVE_CPP_PATH = r"<path_to_your_solve_cpp_file>"


Replace <path_to_your_...> with the files where you want Sublime to read/write problem data.
Ensure these files exist or Sublime can create them automatically.

3. Configure Custom Port

Open CompetitiveHelper.py and set the port:

PORT = 10045


Open the Competitive Companion browser extension → Settings → Custom Port → set 10045.

This ensures the extension communicates correctly with the plugin.

4. Start the Listener in Sublime

Press Ctrl+Shift+P (or Cmd+Shift+P on Mac).

Search for Competitive Helper: Start Listener and select it.

The plugin will now listen for problems from Competitive Companion.

5. Fetch Problem Data

Open a competitive programming problem in your browser (e.g., Codeforces, AtCoder, HackerEarth).

Click the Competitive Companion extension icon.

The plugin automatically writes:

input.txt → problem input

output.txt → your solution output (cleared)

e-output.txt → expected output

solve.cpp → your C++ template

You can immediately start coding in solve.cpp using the template.

solve.cpp Template
#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define endl '\n'
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

Usage Example

Start listener in Sublime.

Open a problem in the browser → click Competitive Companion.

Open solve.cpp → start coding with test cases preloaded from input.txt.

Run your solution and compare with e-output.txt.

Troubleshooting

Plugin not showing in Command Palette

Ensure CompetitiveHelper.py is inside Packages/CompetitiveHelper/.

Restart Sublime Text.

No data received

Check Competitive Companion port matches PORT in CompetitiveHelper.py.

Make sure listener is running before clicking the extension.

SyntaxError

Ensure you are using Sublime Text 4 (Python 3.3). The plugin uses .format() instead of f-strings for compatibility.
