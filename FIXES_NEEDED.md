# Site Issues to Fix Later

## 1. Unused Images in /images Directory

Out of 13 image files, only 4 are currently in use. The following 9 images appear to be leftover from an older version of the site:

### Unused Images (Safe to Delete)
- `bg_all.jpg`
- `conbg.jpg`
- `header.jpg`
- `ls.png`
- `mainbot.png`
- `maintop.png`
- `menubg.png`
- `textbg.jpg`
- `title_right.jpg`

### Currently Used Images
- `skywarn_center.jpg` (used in index.html)
- `skywarn_right.jpg` (used in index.html)
- `ARES.JPG` (used in index.html)
- `ALL FAILS.jpg` (used in index.html)

**Action:** Review unused images and delete if confirmed unnecessary.

---

## 2. Repeater Information Inconsistencies

### A. Spelling Discrepancy - Bolingbroke/Bollingbroke
- **index.html** (line 124): "Bolingbroke/Forsyth"
- **repeaters.html** (line 122): "BOLLINGBROKE"

**Action:** Verify correct spelling and standardize across both files.

---

### B. Thomaston Frequency Offset Conflict
**index.html** lists Thomaston with TWO different offsets:
- Line 174: Part-time repeater - `147.390+ (131.8 Tone)` - Online
- Line 195: Standby alternate remote - `147.390- (131.8 Tone)` - Standby

**repeaters.html** only shows:
- Line 129: Part-time repeater - `147.390+ (131.8 Tone)`

**Issue:** Different offsets (+ vs -) on the same frequency is unusual. This needs clarification.

**Action:** Verify which is correct:
- Is it 147.390+ or 147.390-?
- Are there actually two different Thomaston repeaters?
- Should the standby alternate remote entry be removed?

---

### C. Content Differences Between Pages

**index.html** includes information NOT on repeaters.html:
1. **Status indicators:** Online, Offline, Online Soon
   - Eastman 145.210- shows as **Offline** (index.html line 116)
   - Milledgeville 147.135+ shows as **Online Soon** (index.html line 141)
2. **AllStarLink Node:** Warner Robins 443.150+ lists "AllStarLink Node 48166" (index.html line 159)

**repeaters.html** includes information NOT on index.html:
1. Sponsor callsigns and club names
2. Coverage area details
3. Special notes (emergency power, historical info)

**Action:** Decide if:
- Status information should be added to repeaters.html
- AllStarLink node info should be added to repeaters.html
- Both pages should have consistent technical details

---

## 3. General Recommendations

### Page Purposes (Current State)
- **index.html:** Quick reference with real-time status
- **repeaters.html:** Detailed information about each repeater

### Suggested Actions
1. Reconcile the Bolingbroke/Bollingbroke spelling
2. Clarify the Thomaston frequency situation
3. Consider if repeaters.html should show status information
4. Review if both pages need to be kept in sync or serve different purposes
5. Delete unused images to clean up repository

---

*Document created: January 2026*
*Issues identified during site review*
