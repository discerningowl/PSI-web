# Repeaters.json Data Schema Documentation

## Overview

`repeaters.json` is the single source of truth for all repeater information on the Peach State Intertie website. This file contains a complete database of all repeaters in the system, including full-time linked, part-time linked, and SKYWARN standby repeaters.

**Location:** `/repeaters.json`

**Used by:**
- `repeaters.js` - Dynamically renders repeater data on web pages
- `index.html` - Displays simplified repeater lists
- `repeaters.html` - Displays detailed repeater directory

---

## JSON Structure

The file contains a single root object with one property:

```json
{
  "repeaters": [ /* array of repeater objects */ ]
}
```

---

## Repeater Object Schema

Each repeater object in the `repeaters` array can contain the following fields:

### Required Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `id` | string | Unique identifier for the repeater (kebab-case) | `"repeater-irwinton-hub"` |
| `location` | string | Primary location name displayed to users | `"Irwinton (HUB)"` |
| `frequency` | string | Repeater output frequency in MHz | `"443.275"` |
| `offset` | string | Transmit offset direction | `"+"` or `"-"` |
| `tone` | string | CTCSS/PL tone in Hz | `"77.0"` |
| `callsign` | string | FCC callsign of the repeater | `"K4DBN"` |
| `status` | string | Current operational status | `"online"`, `"offline"`, or `"standby"` |
| `linkType` | string | Type of intertie connection | `"fulltime"`, `"parttime"`, or `"skywarn"` |

### Optional Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `locationDetail` | string | Additional location information | `"Byron Fire Dept"` |
| `locationShort` | string | Abbreviated location for compact displays | `"Warner Robins (HMC)"` |
| `coverage` | string | Geographic coverage description | `"Wilkinson County and surrounding areas"` |
| `sponsor` | string | Repeater sponsor/owner information | `"WB4NFG"` |
| `club` | string | Associated amateur radio club | `"Central Georgia Amateur Radio Club"` |
| `features` | string | Special features or notes | `"AllStarLink Node 48166"` |
| `statusText` | string | Custom status message | `"Online Soon"` |
| `toneText` | string | Override tone display text | `"No Tone"` |
| `isHub` | boolean | Indicates if this is the system hub repeater | `true` |
| `function` | string | Specific function (used for SKYWARN repeaters) | `"Primary link to NWS Peachtree City"` |
| `repeaterbookUrl` | string | RepeaterBook.com reference URL (not displayed on site) | `"https://www.repeaterbook.com/repeaters/index.php?state_id=13&freq=443.275"` |

---

## Field Details

### `id` (Required)
- **Purpose:** Unique identifier for database lookups and DOM element IDs
- **Format:** Lowercase with hyphens (kebab-case)
- **Naming Convention:**
  - Regular repeaters: `repeater-{location}`
  - SKYWARN repeaters: `skywarn-{location}`
- **Examples:**
  - `"repeater-irwinton-hub"`
  - `"repeater-macon"`
  - `"skywarn-fayetteville"`

### `location` (Required)
- **Purpose:** Primary display name shown on website
- **Format:** Proper case with optional parenthetical notes
- **Examples:**
  - `"Irwinton (HUB)"`
  - `"Macon"`
  - `"Warner Robins (Houston Medical Center)"`

### `locationDetail` (Optional)
- **Purpose:** Additional location context not needed in all views
- **When to use:** For specific building/site information
- **Example:** `"Byron Fire Dept"`

### `locationShort` (Optional)
- **Purpose:** Abbreviated form for space-constrained displays
- **When to use:** When full location name is too long
- **Example:** `"Warner Robins (HMC)"` instead of `"Warner Robins (Houston Medical Center)"`

### `frequency` (Required)
- **Purpose:** Repeater output frequency
- **Format:** String in MHz with appropriate decimal places
- **Examples:**
  - `"443.275"` (UHF)
  - `"147.240"` (VHF)
  - `"145.210"` (VHF)

### `offset` (Required)
- **Purpose:** Transmit frequency offset direction
- **Valid Values:**
  - `"+"` - Transmit above repeater frequency
  - `"-"` - Transmit below repeater frequency
- **Standard Offsets:**
  - VHF (2m): ±600 kHz
  - UHF (70cm): ±5 MHz

### `tone` (Required)
- **Purpose:** CTCSS (PL) access tone in Hz
- **Format:** String with one decimal place
- **Examples:**
  - `"77.0"`
  - `"88.5"`
  - `"123.0"`
  - `"131.8"`

### `toneText` (Optional)
- **Purpose:** Override tone display for special cases
- **When to use:** When repeater doesn't use standard tone
- **Example:** `"No Tone"`

### `callsign` (Required)
- **Purpose:** FCC-assigned station callsign
- **Format:** Standard amateur radio callsign format
- **Examples:**
  - `"K4DBN"`
  - `"WB4NFG"`
  - `"WX4EMA"`

### `status` (Required)
- **Purpose:** Current operational status
- **Valid Values:**
  - `"online"` - Repeater is operational
  - `"offline"` - Repeater is not operational
  - `"standby"` - Repeater is on standby (typically SKYWARN)
- **Display:** Renders as colored status indicator on website

### `statusText` (Optional)
- **Purpose:** Custom status message
- **When to use:** To provide additional status context
- **Example:** `"Online Soon"` for repeaters coming online

### `linkType` (Required)
- **Purpose:** Categorizes how repeater connects to intertie
- **Valid Values:**
  - `"fulltime"` - Permanently linked to the intertie
  - `"parttime"` - Automatically linked during events or linked on command
  - `"skywarn"` - Standby repeater for SKYWARN operations
- **Impact:** Determines which section of the website displays the repeater

### `coverage` (Optional)
- **Purpose:** Describes geographic coverage area
- **Format:** Free text description
- **Example:** `"Wilkinson County and surrounding areas"`
- **Display:** Shown in detailed view on repeaters.html

### `sponsor` (Optional)
- **Purpose:** Lists repeater sponsor(s) or owner(s)
- **Format:** Callsign(s) or organization name
- **Examples:**
  - `"WB4NFG"`
  - `"KD4UTQ and WB4NFG"`
  - `"WX4EMA (Macon/Bibb Emergency Management Agency)"`

### `club` (Optional)
- **Purpose:** Associated amateur radio club
- **Example:** `"Central Georgia Amateur Radio Club"`

### `features` (Optional)
- **Purpose:** Special capabilities, notes, or historical information
- **Format:** Free text, can be multiple sentences
- **Examples:**
  - `"AllStarLink Node 48166"`
  - `"Emergency power generator with automatic transfer switch"`
  - `"Historic Repeater - One of the oldest repeaters in Georgia"`

### `isHub` (Optional)
- **Purpose:** Flags the central hub repeater
- **Type:** Boolean
- **When to use:** Only for the main system hub
- **Example:** `true` (only on Irwinton 443.275+ repeater)

### `function` (Optional)
- **Purpose:** Describes specific role or function
- **When to use:** Primarily for SKYWARN repeaters
- **Examples:**
  - `"Primary link to NWS Peachtree City for SKYWARN operations"`
  - `"Backup link to NWS for redundancy"`
  - `"Alternate connection point for SKYWARN operations"`

### `repeaterbookUrl` (Optional)
- **Purpose:** Reference link to RepeaterBook.com for verifying repeater details and status
- **Format:** Full URL to RepeaterBook search by frequency
- **Usage:** Documentation and reference only - not displayed on website or used in JavaScript
- **URL Format:** `https://www.repeaterbook.com/repeaters/index.php?state_id=13&freq={frequency}`
  - `state_id=13` is Georgia
  - `freq={frequency}` is the repeater frequency
- **Examples:**
  - `"https://www.repeaterbook.com/repeaters/index.php?state_id=13&freq=443.275"`
  - `"https://www.repeaterbook.com/repeaters/index.php?state_id=13&freq=147.240"`
- **Why include this:** Provides quick reference for system administrators to verify repeater information and check current status on RepeaterBook

---

## Link Type Categories

### Full-Time Linked (`"fulltime"`)
Repeaters permanently connected to the Peach State Intertie network. Currently 12 repeaters in this category.

**Characteristics:**
- Always linked to the system hub (Irwinton 443.275+)
- Provide continuous wide-area coverage
- Appear in "Full Time Linked Repeaters" section

### Part-Time Linked (`"parttime"`)
Repeaters that connect automatically during events or can be linked on command. Currently 6 repeaters in this category.

**Characteristics:**
- Link during specific events (SKYWARN activations, nets, emergencies)
- Can be linked on command by authorized operators
- Appear in "Automatic Linked or Linked On Command" section

### SKYWARN Standby (`"skywarn"`)
Dedicated repeaters for SKYWARN severe weather operations. Currently 3 repeaters in this category.

**Characteristics:**
- On standby for severe weather activation
- Connect to National Weather Service Peachtree City
- Located at Irwinton Hub Site
- Appear in "Georgia SKYWARN Weather Link Repeaters" section

---

## Complete Example

```json
{
  "id": "repeater-irwinton-hub",
  "location": "Irwinton (HUB)",
  "frequency": "443.275",
  "offset": "+",
  "tone": "77.0",
  "callsign": "K4DBN",
  "status": "online",
  "linkType": "fulltime",
  "coverage": "Wilkinson County and surrounding areas",
  "sponsor": "WB4NFG",
  "features": "System Hub Repeater - All intertie traffic is processed through this UHF hub. Emergency power generator with automatic transfer switch",
  "isHub": true,
  "repeaterbookUrl": "https://www.repeaterbook.com/repeaters/index.php?state_id=13&freq=443.275"
}
```

---

## Minimal Example

```json
{
  "id": "repeater-sandersville",
  "location": "Sandersville",
  "frequency": "145.270",
  "offset": "-",
  "tone": "77.0",
  "callsign": "W4SAN",
  "status": "online",
  "linkType": "fulltime",
  "coverage": "Washington County and surrounding areas",
  "repeaterbookUrl": "https://www.repeaterbook.com/repeaters/index.php?state_id=13&freq=145.270"
}
```

---

## How Data is Used

### On index.html
- Displays simplified list view
- Shows: location, frequency, offset, tone, callsign, status
- Grouped by linkType: fulltime, parttime, skywarn
- Rendered by `renderSimpleListItem()` function in repeaters.js

### On repeaters.html
- Displays comprehensive detailed view
- **Quick Reference Table:** frequency, location, tone, callsign, status
- **Detailed Lists:** All available fields including coverage, sponsor, features
- Grouped by linkType with full descriptions
- Rendered by `renderTableRow()` and `renderDetailedListItem()` functions

---

## Adding a New Repeater

To add a new repeater to the system:

1. **Determine required information:**
   - Frequency, offset, tone
   - Location and callsign
   - Current operational status
   - Link type (fulltime/parttime/skywarn)

2. **Create unique ID:**
   - Format: `repeater-{location}` or `skywarn-{location}`
   - Use lowercase with hyphens

3. **Add to appropriate position in array:**
   - Place with other repeaters of the same linkType
   - Maintain logical geographic or frequency order

4. **Include optional fields as available:**
   - Coverage area
   - Sponsor information
   - Special features
   - Club affiliation

5. **Validate JSON syntax:**
   - Ensure proper comma placement
   - Verify all quotes are matched
   - Test that the file parses correctly

---

## Editing Existing Repeaters

### Updating Status
To mark a repeater offline or back online:
```json
"status": "offline"  // or "online" or "standby"
```

Optionally add status message:
```json
"statusText": "Temporary maintenance - back online soon"
```

### Changing Link Type
To change how a repeater connects:
```json
"linkType": "parttime"  // was "fulltime"
```

### Adding Features
To document new capabilities:
```json
"features": "AllStarLink Node 48166, IRLP Node 1234"
```

---

## Data Integrity Guidelines

1. **Always maintain valid JSON syntax**
   - Use a JSON validator before committing changes
   - Watch for missing/extra commas

2. **Keep IDs unique**
   - Never duplicate an `id` value
   - IDs should remain stable (don't change once created)

3. **Use consistent formatting**
   - Frequencies: Include appropriate decimal places
   - Tones: Always one decimal place (e.g., "77.0" not "77")
   - Callsigns: Uppercase

4. **Validate after changes**
   - Test both index.html and repeaters.html after editing
   - Verify all repeaters display correctly

5. **Required fields must always be present**
   - Never omit: id, location, frequency, offset, tone, callsign, status, linkType

---

*Last updated: January 2026*
*Schema version: 1.0*
