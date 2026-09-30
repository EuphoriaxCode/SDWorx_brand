# CLAUDE.md — bouwen in de SD Worx-stijl

Deze repo is de **stijlbron** voor een hackathon-project voor SD Worx (HR-, payroll- en tijdsregistratiepartner).
Alles wat je bouwt (website, app, dashboard, slides, prototype) moet **er visueel en in toon uitzien alsof SD Worx het zelf gemaakt heeft**.
Lees dit bestand volledig vóór je UI schrijft. Achtergrond en onderbouwing staan in [`README.md`](README.md).

## Werkwijze (verplicht)

1. **Gebruik de tokens, verzin geen waarden.** Importeer `tokens/tokens.css` en `tokens/components.css` (of kopieer ze mee in het project). Gebruik `var(--sdw-*)`; geen losse hexcodes, font-sizes of radii als er een token bestaat.
2. **Start van `examples/index.html`** voor de paginastructuur (topbar → header → hero → kaarten → gradiënt/chips → donkere statistieksectie → footer) en hergebruik `sdw-*` klassen.
3. **Vergelijk visueel** met de referenties in `docs/` (`homepage-*.png` = huidige site, `press-2026-*.jpg` = nieuwe huisstijl juni 2026). Maak een screenshot van je resultaat (Playwright) en corrigeer tot het klopt.
4. **Verzin geen merkfeiten.** Gebruik enkel cijfers/claims uit README §1/§1b. Voor placeholders: duidelijk neutrale voorbeeldtekst, geen verzonnen klantnamen of statistieken die als echt overkomen.
5. Logo's uit `brand/logo/` — nooit zelf een logo tekenen, herkleuren, vervormen of nabootsen.

## Frameworkkeuze
Geen voorkeur opgelegd. Standaard: **statische HTML + de CSS uit `tokens/`**, of Vite/Next + dezelfde CSS-bestanden. In Tailwind: koppel `theme.extend` aan de `--sdw-*` variabelen, niet aan eigen kleuren. Zet de tokens nooit dubbel op (één bron: `tokens.css`).

## Snelle referentie

**Kleur** — één actiekleur: **SD Worx-blauw `#006DD8`** (`--sdw-action`; hover `#0087F3`, pressed `#005BBF`).
Logo-accenten: rood `#F1002F`, geel `#FFBE00` → **spaarzaam** (chips, kleine accenten, foto-props), nooit als vlakken/knoppen-standaard.
Tekst `#303642` (`--sdw-site-text`), koppen `#323334`, secundair `#5A5B5C`, kaarten `#FBFCFC`, rand `#EAEBED`, donker vlak marine `#001C52`, header-CTA `#040D14`.
Verhouding: ±80 % wit/licht, tekst donker, blauw als accent, rood/geel ≤ 2 %.

**Typografie** — koppen: **SD Worx Display** (`--sdw-font-heading`, variabel 100–900, meestal weight **500**); tekst/UI: **Inter** (`--sdw-font-body`, body **18px/24px**). Beide worden geladen via `@import` in `tokens.css` vanaf `cdn.sdworx.com` (CORS open, werkt op elke origin; vereist internet). Sentence case, geen ALL CAPS-koppen. Hero-kop: 120px/108px wit weight 500 (`--sdw-display-1`). 2026-look: mix gewichten in één kop (kernwoorden **bold**, rest regular/light).

**Vorm** — radius **4px** (knoppen, inputs, kaarten), 8–12px voor panelen, chips 16px. Dunne 1px randen. Schaduwen alleen `--sdw-elevation-1…4` (blauwgetint), spaarzaam. Motion 0.25s, subtiel, geen bounce.

**Layout** — container **1224px**, gutters 24px, breakpoints 576/768/992/1200/1440/1912. Header 80px + topbar 48px. Secties ruim: 64px mobiel / 96px desktop verticaal. Spacing enkel uit `--sdw-space-*`.

**Signatuurelementen** (gebruik er meerdere, dat maakt het "SD Worx"):
- **Diagonale sneden** (clip-path) op hero's/foto's, geïnspireerd op de logostrepen; **notch** onder kaartbeelden (`.sdw-card__img`).
- **Sticker-chips** (`.sdw-chip--blue|red|yellow`), schuin, over grote koppen heen.
- **Zachte lichtblauwe mesh-gradiënt** (`.sdw-mesh`) voor statement-secties; zwarte kop met **één woord in merkblauw**.
- **Gewichtsspel** Light→Bold (`.sdw-weights`).
- **Portretfotografie** van echte, diverse mensen op **blauw/blauwgrijs fond**, donkermarine kleding, **gele tablet/map** als kleurpop. Gebruik geen stockachtige gladde poses of illustraties in cartoonstijl. Zonder eigen foto's: gebruik een blauwe gradiënt-placeholder (`--sdw-site-hero-blue` #3777a5 voor hero, `--sdw-2026-photo-bg` / `--sdw-2026-mesh` voor 2026-look), hotlink geen SD Worx-foto's.
- **Iconen**: gevuld, blauw `#006DD8`; SD Worx' eigen `ignite-icons` font: `https://cdn.sdworx.com/ignite/visuals/v2/2.3.0/all.css` (`<i class="ig-icon-f-add">`), of een gevulde open-source set in dezelfde kleur.
- **Grafieken**: afgeronde staven in lichtblauw `#66B4FF` met de belangrijkste in `#006DD8`, gladde blauwe lijn, kleine grijze Inter-labels; multi-serie palet = `--sdw-dataviz-1…10` in volgorde.
- **Klantlogo's** monochroom grijs in een rij; **quotes** met naam, functie, bedrijf.

**Knoppen** — Inter 500, radius 4px: primair blauw (`.sdw-btn--primary`), wit op foto's (`--white`), zwarte header-CTA "Contact" (`--dark`), tekstlink met onderstreep + pijl ↗ (`.sdw-link`). Eén primaire knop per sectie.

## Toon & tekst (Nederlands standaard)
- **Je-vorm**, nooit u. Deskundig, kalm, concreet, geen hype of uitroeptekens.
- Kop 2–5 woorden + 1–2 zinnen + duidelijke CTA. Sentence case.
- Vertrouwde CTA's: "Ontdek alles", "Meer weten", "Contacteer ons", "Lees het klantverhaal", "Schrijf je in".
- Woorden: *vertrouwen/confidence, connected, backbone, clarity, Europe, complexiteit → vertrouwen*. Engelse merkzinnen blijven Engels: **"Trusted to make work work"**, **"HR, Pay & Time"**, *"Built for how Europe works."*, *"More connected."*
- Schrijf "hr" en "kmo" in kleine letters. Bewijs boven belofte: cijfers (100.000+ organisaties, 6 mln werknemers/maand, 19 payroll-systemen in Europa, 1,3 mld omzet 2025) en klantquotes.

## Toegankelijkheid & kwaliteit
- Contrast ≥ AA: tekst op wit `#303642`/`#323334`; lopende links `#005BBF` (niet `#006DD8` bij kleine tekst); wit op `#006DD8` alleen voor knoppen/groot.
- Zichtbare focus (`:focus-visible` staat in `components.css`), `alt`-teksten, semantische HTML, toetsenbordbedienbaar, `prefers-reduced-motion` respecteren voor animaties.
- Mobile-first; test op 375, 768 en 1440px. Geen horizontale scroll.
- `light-dark()` tokens werken automatisch met `color-scheme`; de SD Worx-site zelf is licht — zet donker enkel aan als het project erom vraagt.

## Niet doen
- ❌ Rood of geel als primaire knop-/vlakkleur, paarse/roze "AI-gradiënten", neon, glassmorphism-overload.
- ❌ Zware afronding (pills op knoppen), zware schaduwen, emoji als iconen, ALL CAPS koppen, u-vorm.
- ❌ Andere lettertypes (Roboto, Poppins, …). Fallback enkel `system-ui, sans-serif`.
- ❌ Het logo nabouwen/aanpassen, of beweren dat de site een officiële SD Worx-pagina is (zet bij demo's: "Hackathon-prototype in SD Worx-stijl").
- ❌ Merkassets (logo's, foto's uit `docs/`) publiceren buiten het hackathon-/interne gebruik zonder toestemming van SD Worx.

## Definition of done voor elke pagina
- [ ] Alleen `--sdw-*` tokens/`sdw-*` klassen voor kleur, type, spacing, radius
- [ ] Hero met display-kop (of duidelijke H1) + één primaire CTA
- [ ] Minstens 2 signatuurelementen (diagonale snede, chips, mesh-gradiënt, gewichtsspel, portretfoto)
- [ ] Logo correct (kleur op wit, wit op blauw/donker)
- [ ] Je-vorm, Nederlandse tekst zonder verzonnen feiten
- [ ] Screenshot vergeleken met `docs/`-referenties op 1440px én 375px
- [ ] Focus, alt-teksten en contrast gecontroleerd

## Repo-indeling
| Pad | Doel |
|---|---|
| `tokens/tokens.css`, `tokens.json` | Alle design tokens (`--sdw-*`) |
| `tokens/components.css` | Basiscomponenten (`.sdw-*`) |
| `brand/logo/` | Logo kleur + wit (SVG) |
| `examples/index.html` | Volledige referentiepagina; kopieer als startpunt |
| `docs/` | Referentiescreenshots huidige site + persbeelden 2026 |
| `README.md` | Volledige brand guide met bronnen en onzekerheden |

Bij twijfel over een waarde: `README.md` → dan de live site https://www.sdworx.be/nl-be (CSS: `cdn.sdworx.com/ignite/styling/v2/2.2.0/website/system.css`).
