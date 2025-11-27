# TCS HackQuest 10-Day Training Program

A comprehensive web application to prepare for TCS HackQuest cybersecurity competition with a structured 10-day training program.

## 🚀 Quick Start

### Prerequisites
- A modern web browser (Chrome, Firefox, Safari, Edge)
- Python 3 or PHP (built into macOS) for local server
- All resource files organized in proper folder structure

### Installation & Setup

1. **Download the Complete Package**
   ```
   TCS-HackQuest/
   ├── index.html
   ├── README.md
   ├── PDFs/
   │   ├── TCS-HackQuest-Previous-Years-Solutions.pdf
   │   ├── TCS-HackQuest-Complete-Preparation-Guide.pdf
   │   ├── TCS-HackQuest-Mock-Challenges-Walkthrough.pdf
   │   ├── TCS-HackQuest-Phase-by-Phase-Guide.pdf
   │   ├── TCS-HackQuest-50-Practice-Problems.pdf
   │   ├── TCS-HackQuest-Questions.pdf
   │   └── File-Navigation-Guide.pdf
   ├── Guides/
   │   ├── macos_security_setup_guide.md
   │   └── tcs_hackquest_10day_plan.csv
   └── Templates/
       ├── tcs_hackquest_report_template.md
       └── tcs_hackquest_cheatsheet.md
   ```
3. **Start Local Server**
   
   Open Terminal and navigate to the `TCS-HackQuest` folder:
    ```cd /path/to/TCS-HackQuest ```

   **Option 1: Python (Recommended)**
    ```python3 -m http.server 8000 ```

   **Option 2: PHP**
    ```php -S localhost:8000 ```

4. **Open in Browser**
    ```http://localhost:8000 ```

### Why Local Server is Required

Modern browsers block `file://` protocol from reading local files for security. A local server serves files over `http://` which allows:
- ✅ Markdown file viewer to work
- ✅ CSV table viewer to work
- ✅ Proper file loading without CORS errors

## 📖 How to Use the App

### Main Interface

#### 1. Progress Overview (Top Section)
- **Progress Bar**: Shows overall completion percentage
- **Statistics Cards**: 
  - Tasks Completed / Total Tasks
  - Days Completed
  - Hours Logged (auto-calculated)

#### 2. Day Navigation Tabs
- Click on **Day 1** through **Day 10** to switch between days
- Completed days show a ✓ checkmark
- Active day is highlighted in teal

#### 3. Task Management

**Each task card includes:**
- ☑️ **Checkbox**: Mark tasks as complete (progress auto-saves to browser)
- **Task Title & Description**: What you need to do
- **💡 Key Concepts**: Important learning points
- **📋 Steps**: Detailed instructions
- **🧪 Practice Labs**: Clickable cards leading to external platforms
- **📝 Previous Year Questions**: TCS-specific challenge references
- **⏱️ Time & Difficulty**: Estimated duration and skill level
- **Resource Links**: PDFs, guides, and external links

**Resource Types:**
- 📄 **PDF Links**: Open in new tab/browser
- 📝 **Markdown Files**: View directly in app with formatted viewer
- 📊 **CSV Files**: View as formatted tables in app
- 🔗 **External Links**: Open online resources

### Quick Access Buttons (Bottom Right)

1. **📚 All Resources**
   - View complete list of all PDFs, guides, and templates
   - Click to view markdown/CSV files in-app
   - Click to open PDFs in browser

2. **📊 My Progress**
   - See day-by-day completion breakdown
   - Progress bars for each day
   - Tasks completed per day

3. **🔄 Reset Progress**
   - Clear all saved progress
   - Start fresh (cannot be undone)

## 🎯 Training Workflow

### Recommended Usage Pattern

**Day 1-6: Skill Building**
1. Click on the day tab
2. Read **Learning Objectives** at the top
3. Work through tasks sequentially
4. Check off tasks as you complete them
5. Click resource links to:
   - View guides in-app (markdown/CSV)
   - Open PDFs in browser for study
   - Access external practice platforms

**Day 7: Challenge Day**
- Complete mixed challenges
- Practice time management
- Write reports using templates

**Day 8: Mock Competition**
- Full 6-hour simulated CTF
- Test all skills under pressure
- Analyze performance

**Day 9: Refinement**
- Focus on weak areas identified in Day 8
- Speed drills
- Finalize cheat sheet

**Day 10: Rest & Review**
- Light review only
- Mental preparation
- Tool verification

## 📂 File Navigation Tips

### Viewing Files In-App

**Markdown Files (.md):**
- Click any markdown resource link
- File opens in modal viewer with formatted content
- Supports headers, lists, code blocks, links, tables

**CSV Files (.csv):**
- Click CSV resource link
- Opens as formatted table with:
  - Sticky headers
  - Alternating row colors
  - Hover effects

**Example:**
Templates/tcs_hackquest_cheatsheet.md → Click → View formatted cheatsheet
Guides/tcs_hackquest_10day_plan.csv → Click → View as table

### Opening PDFs

PDFs open in new browser tab:
- Click PDF resource link
- Browser opens PDF viewer
- Use browser PDF controls (zoom, search, download)

## 💾 Progress Tracking

### Auto-Save Features
- ✅ Task completion saved to browser localStorage
- ✅ Progress persists across sessions
- ✅ No login required
- ✅ Works offline once loaded

### Progress Data
- Completed tasks tracked by ID
- Overall completion percentage
- Estimated hours logged
- Day-by-day breakdown

### Resetting Progress
1. Click 🔄 button (bottom right)
2. Confirm reset dialog
3. All progress cleared
4. Page reloads fresh

## 🛠️ Troubleshooting

### File Loading Errors

**Error: "Could not load [filename]"**

**Solution:**
1. Verify file exists in correct folder
2. Check folder structure matches setup
3. Ensure local server is running
4. Check Terminal for server errors

**Common Issues:**
# If port 8000 already in use
python3 -m http.server 8001  # Try different port
# Then access: http://localhost:8001

### Markdown/CSV Not Displaying

**Check:**
1. ✅ Local server is running
2. ✅ File path is correct
3. ✅ File has .md or .csv extension
4. ✅ Opened via `http://` not `file://`

### Progress Not Saving

**Browser localStorage required:**
- ✅ Not in private/incognito mode
- ✅ Cookies/localStorage enabled
- ✅ Sufficient browser storage

## 🎨 Features

### Interactive Elements
- ✨ **Checkbox Tracking**: Click to mark complete
- ✨ **Day Tabs**: Quick navigation between days
- ✨ **Lab Cards**: Hover effects, click to open platforms
- ✨ **Progress Bars**: Animated completion tracking
- ✨ **Modal Viewers**: In-app file viewing
- ✨ **Responsive Design**: Works on mobile, tablet, desktop

### Smart Resource Detection
- Automatically detects file types
- Markdown/CSV → Opens in-app viewer
- PDFs → Opens in new tab
- External links → Opens in new tab

## 📱 Mobile Usage

App is fully responsive:
- Day tabs scroll horizontally
- Cards stack vertically
- Touch-friendly buttons
- Modal viewers optimized for mobile

## ⚡ Performance Tips

1. **Keep Server Running**: Don't close Terminal while using app
2. **Modern Browser**: Use latest Chrome/Firefox for best performance
3. **Clear Cache**: If files don't load, clear browser cache
4. **Stable Connection**: For external lab links

## 🔗 External Resources

The app links to many external platforms:
- **PicoCTF**: Practice challenges
- **HackTheBox**: Advanced labs
- **TryHackMe**: Guided rooms
- **PortSwigger Academy**: Web security labs
- **CryptoHack**: Cryptography challenges

**Note:** These require separate accounts/registration.

## 🎓 Study Strategy

### Effective Use
1. **Follow Sequential Order**: Days 1-10 build on each other
2. **Complete Tasks Fully**: Don't rush ahead
3. **Use Resources**: Click and read all linked materials
4. **Track Progress**: Check tasks as you finish
5. **Review Progress Modal**: Monitor day-by-day completion
6. **Practice Labs**: Actually do the external challenges
7. **Write Reports**: Use templates for practice

### Time Management
- Each day has estimated time allocation
- Individual tasks show duration
- Plan your schedule accordingly
- Take breaks between intensive sessions

## 🆘 Support & Feedback

**Created by:** [psypherion](https://github.com/psypherion)

**Repository:** Check GitHub for updates and issues

## 📋 Checklist: Before Starting

- [ ] Downloaded complete package with all folders
- [ ] Verified folder structure is correct
- [ ] Started local server (Terminal running)
- [ ] Opened `http://localhost:8000` in browser
- [ ] Can see Day 1 content
- [ ] Can click and view a markdown file
- [ ] Can click and view the CSV file
- [ ] Progress tracking works (check a task, refresh page, still checked)
- [ ] All resource links load properly

## 🚦 Getting Started Quick Guide

### First 5 Minutes
1. ✅ Start local server: `python3 -m http.server 8000`
2. ✅ Open: `http://localhost:8000`
3. ✅ Click **Day 1** tab
4. ✅ Read Learning Objectives
5. ✅ Click first task checkbox to test tracking
6. ✅ Click 📚 button to see all resources
7. ✅ Click a markdown file to test viewer
8. ✅ Click 📊 to see progress modal

### Ready to Train!
You're all set! Follow the 10-day program day by day, marking tasks complete as you go. Good luck with TCS HackQuest! 🚀

---

**Competition Date:** December 7, 2025

**Total Tasks:** 60+ tasks across 10 days

**Total Resources:** 10 PDFs + 3 markdown guides + 1 CSV plan + external labs

**Estimated Total Time:** 100+ hours of focused preparation
