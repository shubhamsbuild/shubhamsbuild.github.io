/**
 * Make this Netlify site publicly reachable.
 *
 * Since July 2026 every new Netlify project is private by default: the deploy
 * succeeds, every file is on the CDN, and the URL still returns 401 with a
 * "Login Redirect" page.
 *
 * Netlify implements this as a site-level SSO-login requirement, not as a
 * visibility field. PATCHing `visibility`, `site_visibility`, `is_public`,
 * `private`, `access` or `edge_access` all return 200 and do nothing. There is
 * no CLI command for it and no entry in the bundled OpenAPI spec. The only
 * thing that works is `sso_login: false`.
 *
 * Side effect worth knowing: this also flips the team-level `account_sso_login`
 * to false.
 *
 * Usage:  node make-public.js
 */
const fs = require("fs");
const path = require("path");
const os = require("os");

function readToken() {
  const cfg = path.join(
    process.env.APPDATA || path.join(os.homedir(), ".config"),
    "netlify", "Config", "config.json"
  );
  if (!fs.existsSync(cfg)) {
    throw new Error(`Netlify config not found at ${cfg} — run \`netlify login\` first.`);
  }
  const json = JSON.parse(fs.readFileSync(cfg, "utf8"));
  // Token lives under a nested users.<id>.auth.token key.
  const stack = [json];
  while (stack.length) {
    const node = stack.pop();
    if (node && typeof node === "object") {
      if (node.auth && typeof node.auth.token === "string") return node.auth.token;
      if (typeof node.token === "string" && node.token.length >= 40) return node.token;
      for (const v of Object.values(node)) stack.push(v);
    }
  }
  throw new Error("No auth token found in the Netlify config.");
}

function readSiteId() {
  const state = path.join(__dirname, ".netlify", "state.json");
  if (!fs.existsSync(state)) {
    throw new Error("Not linked to a Netlify site — run `netlify link` first.");
  }
  return JSON.parse(fs.readFileSync(state, "utf8")).siteId;
}

(async () => {
  const token = readToken();          // held in a variable, never printed
  const siteId = readSiteId();

  const res = await fetch(`https://api.netlify.com/api/v1/sites/${siteId}`, {
    method: "PATCH",
    headers: {
      Authorization: `Bearer ${token}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ sso_login: false }),
  });

  if (!res.ok) {
    console.error(`PATCH failed: ${res.status} ${res.statusText}`);
    process.exit(1);
  }

  const site = await res.json();
  const url = site.ssl_url || site.url;
  console.log(`sso_login is now ${site.sso_login}`);
  console.log(`Verifying ${url} ...`);

  const check = await fetch(url, { redirect: "manual" });
  console.log(`  -> HTTP ${check.status}`);
  if (check.status === 200) {
    console.log(`\nLive and public: ${url}`);
  } else {
    console.log("\nStill gated. Give the CDN a minute, then re-run this script.");
  }
})().catch((e) => {
  console.error(e.message);
  process.exit(1);
});
