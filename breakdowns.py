"""Structured breakdown of each case study, keyed by slug.

Every field here is *derived from that study's own page* in content/work/, the numbers, the steps and the chips are restatements of what the prose
already says, never additions to it. If a number changes in the markdown it
has to change here too; nothing in this file is a second source of truth.

Shape:
    question   one line: the thing the engagement had to answer
    sector     what the client sells
    buyer      who they sell to
    constraint the rule the work had to run inside
    metrics    two supporting numbers for the hero strip (the headline
               number stays in the markdown front matter)
    steps      (title, body, chip), the chip is the transformation, in caps
    value      what the client kept, one line each
    chips      short filter tags for the index page: discipline, market, technique
"""

BREAKDOWNS = {

    # ---------------------------------------------------------------- 01
    "list-source": {
        "chips": ["Measurement", "Investment banking", "List sourcing"],
        "question": "Was the other account's copy the thing worth copying, "
                    "or was it the list underneath it?",
        "sector": "Investment banking",
        "buyer": "Founder-led and mid-market companies raising $5M&ndash;$100M+",
        "constraint": "Regulated, securities-adjacent copy cannot promise "
                      "a raise closes, cannot promise returns, and does not quote fees",
        "metrics": [
            ("0.482%", "positive rate, against 0.053% from the incumbent vendor"),
            ("275", "calls booked for the account, via Calendly and Cal.com"),
        ],
        "steps": [
            ("Re-cut the qualification gate",
             "The ICP as written on the onboarding form filtered on headcount. An "
             "investment bank does not care how many people a company employs; it "
             "cares about revenue and raise size. Moving the gate turned "
             "qualification from something a list tool can filter into an "
             "enrichment step, which is the whole reason the experiment "
             "below was worth running.",
             "Headcount &rarr; revenue + raise size"),
            ("Read the instruction, then tested it",
             "The client asked to have his campaign modelled on a sister "
             "capital-markets account. Copying that account&rsquo;s copy was the "
             "obvious reading and a trap at the same time. What actually made that "
             "account work turned out to be somewhere else entirely.",
             "Copy the copy? &rarr; copy the list"),
            ("Mined the sister account&rsquo;s replies",
             "Its platform has no documented way to filter replies by disposition, "
             "but there is an undocumented status parameter on the replies "
             "endpoint. Fixed page size of fifteen and roughly nine seconds a page "
             "makes a serial pull a multi-hour job. Parallelised, it ran over lunch.",
             "505 campaigns &middot; 498,000 replies scanned"),
            ("Rebuilt them as a list, not an export",
             "Every row carried the lead&rsquo;s name, title, company, the cleaned "
             "text of what they had actually replied, the campaign that produced "
             "it, and 24 custom-variable columns. The evidence of why each person "
             "responded travelled with them.",
             "13,011 replies &rarr; 11,497 unique leads"),
            ("Held everything else constant",
             "Same client, same offer, same warmed inboxes, same sending window, "
             "same regulated-copy constraints. The only variable was where the "
             "list came from.",
             "One variable: the source"),
            ("Ranked the sources on positives",
             "Four sources across 146,772 sends, ranked on positive replies per "
             "contacted rather than on reply rate, which is the metric the "
             "next study in this set exists to discredit.",
             "4 sources &middot; 146,772 sends"),
        ],
        "value": [
            "An 11,497-lead intent list with each prospect&rsquo;s original reply attached",
            "A repeatable method for mining a sending platform&rsquo;s own reply history",
            "A ranked comparison of four list sources under identical copy",
            "The account became the highest-converting of thirteen",
        ],
    },

    # ---------------------------------------------------------------- 02
    "copy-segment-mismatch": {
        "chips": ["Diagnosis", "EdTech", "Segmentation"],
        "question": "Is a positive rate at half target a market-size problem, "
                    "or is the copy addressed to the wrong people?",
        "sector": "AI mock-interview software",
        "buyer": "Higher-ed career services and private-school college counsellors",
        "constraint": "New sending infrastructure built from zero, against a "
                      "target of 20 positive leads a month",
        "metrics": [
            ("30", "calls booked for the account, via Calendly and Cal.com"),
            ("75", "interested replies account-wide, against a target of 20 a month"),
        ],
        "steps": [
            ("Ruled out the cheap explanation first",
             "Before blaming the copy, blame the triage. 375 replies sampled by "
             "hand, of which 129 were genuine human inbox replies, and zero "
             "positive-signal replies had been left untagged. The copy genuinely "
             "was not converting.",
             "375 sampled &middot; 0 missed positives"),
            ("Found the controlled experiment already in the account",
             "Two campaigns were running byte-identical copy to different "
             "audiences. One produced 18 positives. The other returned zero across "
             "4,422 sends and 194 replies. An accidental experiment had been "
             "sitting there for weeks and nobody had read it as one.",
             "Same bytes &middot; 18 positives vs 0"),
            ("Read the replies for the reason",
             "The shared email opens on the recipient&rsquo;s career centre and "
             "proves with a college athletics case study. A K-8 head of school has "
             "neither. The recurring reply said so almost verbatim.",
             "Copy/segment mismatch, not copy quality"),
            ("Split all account volume by title bucket",
             "Career-readiness titles converted at 0.152% against 0.072% for "
             "administrators, and administrator titles were taking 56% of "
             "total volume.",
             "56% of volume aimed at the worse bucket"),
            ("Priced the proposed fix against the real one",
             "When positives were low the instinct was to buy more market. Canada "
             "adds roughly 10&ndash;15% to a 29,000-account US base, which at the "
             "account&rsquo;s measured rate projects to three or four extra "
             "positives per cycle. Fixing one campaign&rsquo;s copy was worth more "
             "than the entire build.",
             "+4,193 accounts &asymp; 3 positives / cycle"),
            ("Built it anyway, then put the arithmetic in writing",
             "The Canada build shipped because it was asked for. What it produced "
             "worth keeping was five ways a US school scraper is silently wrong "
             "north of the border, and a compliance blocker with penalties into "
             "eight figures.",
             "Built as asked &middot; arithmetic on the record"),
        ],
        "value": [
            "The shortfall isolated to copy rather than to list size or infrastructure",
            "A title-bucket split showing where 56% of volume was going",
            "Five documented ways a US school scraper fails silently in Canada",
            "An anti-spam-law blocker raised before anything sent north of the border",
        ],
    },


    # ---------------------------------------------------------------- 04
    "smb-data-acquisition": {
        "chips": ["Data acquisition", "Tax advisory", "Local SMB"],
        "question": "Where do you get sixty thousand owner-operated trades "
                    "businesses that no data vendor sells?",
        "sector": "CPA-led proactive tax strategy",
        "buyer": "Owner-operated trades and home services, $1M&ndash;$10M revenue, "
                 "1&ndash;50 employees",
        "constraint": "Regulated, no numeric savings guarantees, and "
                      "no booking link, so every call to action is reply-based",
        "metrics": [
            ("60,000", "trade companies sourced at zero list-vendor cost"),
            ("12", "calls booked for the account, via Calendly and Cal.com"),
        ],
        "steps": [
            ("Named the real problem",
             "A $3M family-run restoration company in a mid-size Texas city is in "
             "no vendor&rsquo;s database. It is in map data, a business bureau "
             "directory, a phone directory and a manufacturer&rsquo;s certification "
             "locator, in four inconsistent forms, and it is your job to work out "
             "that they are the same business.",
             "A copy brief wearing a data problem&rsquo;s clothes"),
            ("Densified adaptively instead of brute-forcing",
             "A trade-association locator caps one zip-and-radius query at roughly "
             "316 nearest results, and all 41,000 US zip codes is 95% redundant. "
             "Run a coarse national grid at 100 miles; any query returning under "
             "~300 is provably complete for its disk; densify only the cells that "
             "capped, 100 to 25 to 10 to 5, until nothing caps.",
             "480 requests instead of 41,000"),
            ("Got through a hard edge block",
             "Plain HTTP libraries return 403 and headless automation pins one "
             "residential IP per session, so once flagged everything blocks. A real "
             "Chrome TLS fingerprint through a proxy handing out a fresh exit per "
             "connection gets roughly 8% through; retry each page until one returns "
             "200 with real content, verified by an expected element in the body "
             "rather than by the status code.",
             "3 workers beat 6 &middot; verify the body, not the status"),
            ("Read a bug that looked like a broken proxy",
             "1,746 rows, 19 of 49 metros reported blocked, and a suspiciously "
             "consistent +60 per metro, exactly two pages of thirty "
             "listings. The harness was aborting an entire metro on a single "
             "blocked page. The proxy was fine the whole time.",
             "1,746 &rarr; 9,038 rows &middot; same proxy, same day"),
            ("Found the source that carried emails already",
             "For roofing the highest-yield source was not a directory at all. A "
             "major manufacturer&rsquo;s contractor locator runs on a hosted search "
             "index containing email addresses directly, 1,794 of 1,802 with "
             "an email, and 82% of those personal local-parts rather than generic "
             "inboxes.",
             "Email-ready coverage +33%"),
            ("Deduplicated against the live platform, not the files",
             "2,934 companies by domain plus 52 by email had already been "
             "contacted, roughly 30% of a supposedly net-new list. An "
             "earlier list had been loaded and sent months before, and nothing in a "
             "file-level merge knows that.",
             "30% of &ldquo;net-new&rdquo; already contacted"),
        ],
        "value": [
            "Roughly 60,000 trade companies and 27,000 attorneys at zero list-vendor cost",
            "Four reusable acquisition techniques, each with its failure mode documented",
            "Four data-quality traps caught before they reached a send",
            "A directory-domain blocklist specification, written from a failure that shipped",
        ],
    },

    # ---------------------------------------------------------------- 07
    "first-fold": {
        "chips": ["Personalisation", "DTC / e-commerce", "AI agents"],
        "question": "Why does a personalised opener written by an AI agent read "
                    "like a template to the person receiving it?",
        "sector": "Conversion-rate optimisation for DTC Shopify brands",
        "buyer": "DTC Shopify brands doing $100K+ a month",
        "constraint": "The agency&rsquo;s own pitch is that the first fold decides "
                      "cold paid traffic, so the outbound had to demonstrate that "
                      "claim rather than assert it",
        "metrics": [
            ("72", "calls booked across the current and legacy workspaces"),
            ("4:1", "offer-led angles beat observation-led ones, on the same account"),
        ],
        "steps": [
            ("Read the failure before rebuilding",
             "The flagship campaign asked an agent to review a prospect&rsquo;s "
             "whole store. It returned five observations that could have been "
             "written about any Shopify site, and prospects read them as a "
             "template because functionally they were one.",
             "Five vague findings &rarr; worse than none"),
            ("Narrowed the scope until the output had to be specific",
             "One weakness, in the first fold, at 390px mobile width, quoting the "
             "store&rsquo;s real hero text. There is only one hero headline, "
             "the agent either has something concrete to say about it or it does not.",
             "The store &rarr; the first fold at 390px"),
            ("Rendered mobile properly",
             "Resizing a desktop browser does not change the render viewport, so a "
             "desktop-rendered &ldquo;mobile&rdquo; screenshot shows the desktop "
             "layout at a narrow width, and produces confident observations "
             "about a layout the prospect has never seen.",
             "Real device emulation, not a narrow window"),
            ("Gave the agent permission to return nothing",
             "It skips when the fold is already strong, and is explicitly forbidden "
             "from manufacturing a nitpick, because manufacturing nitpicks is "
             "what killed the previous version. Live dry runs settled at roughly "
             "80% send, 20% skip.",
             "80% send &middot; 20% skip"),
            ("Routed the skipped fifth somewhere useful",
             "They go to a guarantee-led sequence needing no personalisation at all, "
             "so every lead is touched and nobody with a good first fold is told "
             "about a flaw the agent invented.",
             "No lead wasted &middot; no invented flaws"),
            ("Gated every launch on a sameness check",
             "Manual QA on the first twenty AI rows before each send. If twenty rows "
             "read alike the agent has drifted back into templating, and the campaign "
             "does not go out.",
             "20 rows checked before every launch"),
        ],
        "value": [
            "A personalisation step that fails safe instead of fabricating",
            "A reusable rule: narrow the task until the output cannot be generic",
            "A second offer for the prospects the agent deliberately skips",
            "An in-Slack mockup tool that renders the prospect&rsquo;s own product",
        ],
    },

    # ---------------------------------------------------------------- 08
    "query-axis": {
        "chips": ["Data acquisition", "Automotive", "Local SMB"],
        "question": "The buyer is buried under a long tail the filters cannot "
                    "separate. Change the filter, or change the question?",
        "sector": "VIN-level automotive marketing analytics",
        "buyer": "US franchise dealer rooftops spending $10K+ a month on digital ads",
        "constraint": "$1,200 per rooftop per month, month to month, against a "
                      "client target of 15 leads a month",
        "metrics": [
            ("0.239%", "positive rate on the best split, one of the strongest here"),
            ("1", "call booked, four campaigns, all paused, 6,021 sends is not a test"),
        ],
        "steps": [
            ("Named why the obvious search fails",
             "Searching a metro for the generic category buries franchise rooftops "
             "under small used-car lots, buy-here-pay-here operations and service "
             "centres. Filtering that tail out by business name is a losing battle.",
             "The filter was never going to win"),
            ("Changed the query axis instead",
             "Manufacturer brand crossed with metro, rather than category. 20 brands "
             "across 78 metros in the nine best-fit states, roughly 1,560 queries, "
             "one page each.",
             "Category &rarr; brand &times; metro"),
            ("Let the platform do the classification",
             "The platform&rsquo;s own type field is the franchise signal: a result "
             "typed as a given brand&rsquo;s dealer is, by its own classification, a "
             "franchise rooftop. Brand is recorded from that field and franchise "
             "status derived from it, never inferred from a company name.",
             "The type field is the signal"),
            ("Cleaned on structure, not on guesses",
             "Geo-fenced by state code parsed from the address. Non-dealer types "
             "dropped, plus a name-token blocklist for commercial-truck and "
             "powersports brands sharing showroom space. Deduplicated by place ID, "
             "then by root domain.",
             "Dedupe on place ID, then root domain"),
            ("Refused a qualification the source cannot support",
             "The stated ICP included independents at 50+ units. Unit volume is not "
             "in maps data, so those rows would have been unqualified guesses. They "
             "were scoped to a separate pass against a different source rather than "
             "quietly folded in.",
             "Scoped out, not shipped as guesses"),
            ("Found the shared classifier in the wrong place",
             "The house mail-provider classifier&rsquo;s canonical copy lived inside "
             "this client&rsquo;s assembly script and was reused everywhere. Its two "
             "gaps did not matter on car dealerships. They mattered enormously on a "
             "government-adjacent list later.",
             "Shared code, tested on one client&rsquo;s data"),
        ],
        "value": [
            "A franchise universe from a source that does not label franchises",
            "Brand recorded per rooftop, derived rather than guessed",
            "A documented reason half the stated ICP was not shipped",
            "The provider split shown to be a segmentation tool, not a rule",
        ],
    },

    # ---------------------------------------------------------------- 01
    "income-proxy": {
        "chips": ["Data acquisition", "Tax advisory", "Directory sourcing"],
        "question": "The ICP is defined by a number no database contains. "
                    "What do you filter on instead?",
        "sector": "Tax advisory and tax planning",
        "buyer": "Business owners with personal taxable income over $600,000",
        "constraint": "Regulated, no numeric savings guarantees, and "
                      "the client will not prospect its own industry",
        "metrics": [
            ("144", "calls booked for the account, via Calendly and Cal.com"),
            ("2.1&times;", "the profession proxy against the brief as literally written"),
        ],
        "steps": [
            ("Read what the form could not give",
             "Industry: &ldquo;most of them.&rdquo; Three overlapping size brackets "
             "and three overlapping revenue brackets, which narrow nothing. Five "
             "ideal customers, competitors and intent signals all answered with a "
             "deferral. Targeting had to be derived, not transcribed.",
             "A form that answers none of the list questions"),
            ("Named why the ICP was unbuildable",
             "Personal taxable income is not a field in any B2B database and never "
             "will be, because it is not public. Vendors sell headcount, company "
             "revenue, industry, technographics and funding events.",
             "$600K income &rarr; no vendor sells it"),
            ("Found an attribute that implies it and can be sourced",
             "A licensed profession whose partners and firm owners plausibly clear "
             "the threshold far more often than a randomly drawn business owner "
             ", and who are the right kind of owner for a pass-through tax "
             "strategy pitch.",
             "Income &rarr; profession + state"),
            ("Sourced it from directories, not vendors",
             "That profession is listed publicly, by profession, with geography "
             "attached, in trade directories and a state licensing roll. The "
             "population is enumerable without buying it, and enumerable by the "
             "exact filter that matters.",
             "An impossible list &rarr; a directory scrape"),
            ("Kept the literal brief running as a control",
             "An all-industries master campaign ran the ICP exactly as written: "
             "business owners across any industry, no proxy. Six campaigns and "
             "65,587 sends of it.",
             "65,587 sends of control volume"),
            ("Ranked both arms on positives, not replies",
             "87 of 92 campaigns count auto-replies in their statistics, so reply "
             "rate on this account is inflated by an unknown amount. Interested is "
             "a human flag set during triage, so it is the only comparable number.",
             "0.080% proxy vs 0.038% literal"),
        ],
        "value": [
            "A buildable list for an ICP that could not be bought",
            "A control arm that turns the claim into a measurement",
            "A sourcing pattern that transfers to any licensed profession",
            "The auto-reply defect documented against eleven months of history",
        ],
    },

    # ---------------------------------------------------------------- 05
    "client-seeded-lists": {
        "chips": ["Measurement", "In-house", "Lookalikes"],
        "question": "What do you target when nothing is imposed on you, and you "
                    "already know which engagements work?",
        "sector": "B2B outbound agency, selling itself",
        "buyer": "Companies resembling, or competing with, existing clients",
        "constraint": "No client constraints at all, no regulated copy, no "
                      "approval cycles, no inherited ICP",
        "metrics": [
            ("81", "calls booked, via Calendly and Cal.com"),
            ("1.3&times;", "client-seeded lists over cold vertical lists"),
        ],
        "steps": [
            ("Seeded lists off the client roster",
             "Once an account works, two lists fall out of it for nothing: "
             "companies that look like that client, and companies that compete "
             "with them. Both are pre-qualified by the fact that the motion "
             "already works for one of them.",
             "One signed client &rarr; two free lists"),
            ("Carried the proof into the first email",
             "A lookalike or competitor list comes with a case study you are "
             "allowed to reference, which is the one asset a cold vertical list "
             "can never supply.",
             "The case study ships with the list"),
            ("Ran cold vertical lists alongside",
             "A 109,000-row software list, an education list, a photography list, "
             "recently funded companies, and one campaign named, honestly, "
             "&ldquo;Spray and Pray.&rdquo;",
             "26 campaigns with no client relationship"),
            ("Measured the two against each other",
             "Client-seeded at 0.083% against cold vertical at 0.063%, on "
             "comparable volume. A real edge and a modest one.",
             "0.083% vs 0.063%"),
            ("Reported the result that undercuts the strategy",
             "The single largest campaign, an education list at 55,175 sends, "
             "returned 0.092%, above the account average, and a cold list "
             "rather than a seeded one. The pattern is a tendency, not a law.",
             "The biggest cold list beat the average"),
            ("Read the account as a control on the advice",
             "Every client engagement here argues list construction dominates "
             "copy. Applied with no constraints at all, the source effect is the "
             "smallest measured anywhere in the set.",
             "The weakest source effect in the book"),
        ],
        "value": [
            "A repeatable list motion that every signed client generates for free",
            "A measured comparison against lists built with no client relationship",
            "Evidence that sharper constraints produce sharper targeting",
            "An honest read: the in-house account converts below the client average",
        ],
    },

    # ---------------------------------------------------------------- 06
    "where-they-publish": {
        "chips": ["Measurement", "Creator economy", "List sourcing"],
        "question": "Four plausible ways to build a list against one market. "
                    "Which of them actually converts?",
        "sector": "Growth for creators, coaches and info-product businesses",
        "buyer": "Creators and course sellers in business, finance and career niches",
        "constraint": "84 of 95 campaigns count auto-replies in their statistics, "
                      "so reply rate is not a usable comparison on this account",
        "metrics": [
            ("145", "calls booked for the account, via Calendly and Cal.com"),
            ("26&times;", "spread between the best and worst list construction"),
        ],
        "steps": [
            ("Built the same market four different ways",
             "Platform creator directories, social-follower scrapes, the funnel and "
             "course tools this market runs on, and straight job-title pulls from a "
             "B2B database. All four ran at volume, same infrastructure, same window.",
             "One market &middot; four constructions"),
            ("Ranked on positives because replies were unusable",
             "84 of 95 campaigns count auto-replies in their statistics, so the "
             "1.50% reply rate is inflated by out-of-office traffic by an unknown "
             "amount. Interested is a human flag and unaffected.",
             "Positives per contacted, not reply rate"),
            ("Found the platform lists winning outright",
             "Creator directories and follower scrapes at 0.415% across 207,715 "
             "sends, the strongest construction on the account and the "
             "largest arm of it.",
             "0.415% on 207,715 sends"),
            ("Watched the clever proxy lose to the obvious one",
             "Targeting funnel and course-platform users is a good hypothesis and at "
             "0.228% it beat job titles comfortably. It still lost to going where the "
             "audience publishes, by nearly two to one.",
             "Proximity beat cleverness"),
            ("Let the job-title arm run too long",
             "An agency-owner list sent 38,663 emails for 6 interested, "
             "0.016%. At that rate it was knowable by ten thousand sends. There was "
             "no kill threshold.",
             "38,663 sends &rarr; 6 interested"),
            ("Left the finding unexploited",
             "Creator lists were 28 of 95 campaigns and produced the best rates on "
             "the account by a wide margin. Volume kept going into constructions "
             "that measurably converted worse.",
             "The best arm was never scaled"),
        ],
        "value": [
            "A four-way ranking of list constructions against one market",
            "The single best campaign in the portfolio, at 1.060%",
            "A rule that transfers: target where the buyer publishes",
            "A documented kill threshold that should have existed and did not",
        ],
    },
}
