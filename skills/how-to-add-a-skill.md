# How to add a skill to your AI tool

A skill is a text file of instructions. You give it to your AI tool once, and it follows them. This page shows how in Claude, Google Gemini and ChatGPT.

I checked these steps in October 2026. AI tools move their menus around a lot. If yours look different, use [Any AI tool](#any-ai-tool) at the bottom. It always works.

## First, get the file

1. Open the skill's `SKILL.md` file on GitHub.
2. Near the top right of the file there are two small buttons:
   - **Copy raw file** (two overlapping squares) copies all the text.
   - **Download raw file** (an arrow pointing down) saves the file to your computer.

Each section below says which one you need.

## Claude

### Save it as a skill (Pro, Max, Team and Enterprise plans)

1. Download `SKILL.md`.
2. Make a new folder and give it the skill's name, for example `intent-mirror`. Put `SKILL.md` inside it.
3. Zip the folder.
   - **Mac:** right-click the folder and choose **Compress**.
   - **Windows:** right-click the folder and choose **Compress to ZIP file** (or **Send to > Compressed (zipped) folder**).
4. In Claude, open **Customize**, then **Skills**. In some versions it's under **Settings > Capabilities**, in the Skills section.
5. Upload the zip file, then turn the skill on.
6. Start a new chat. Claude uses the skill when your message fits. You can also say "use intent mirror".

If uploading fails, check that **Code execution and file creation** is turned on in the same settings.

### Or put it in a project

If your plan has Projects: make a new project, open its instructions, paste the copied text and save. Every chat in that project follows it.

## Google Gemini

Gems work on every Gemini plan, including free.

1. On a computer, go to [gemini.google.com](https://gemini.google.com).
2. In the left panel, click **Explore Gems**, then **New Gem**.
3. Give it a name, like **Intent mirror**.
4. Paste the copied text into **Instructions**.
5. Click **Save**.
6. Open your Gem from your Gems list whenever you want to use it. It also shows up in the Gemini phone app.

If the instructions are too long, download the file instead. Add it under **Knowledge > Add files**, and in **Instructions** write: "Follow the instructions in SKILL.md for every message."

You can only make or change Gems on the website, not in the phone app.

## ChatGPT

### Save it as a skill (Business, Enterprise and Edu plans)

1. In the left sidebar, click **Plugins**, then the **Skills** tab.
2. Click **Create**, then **Upload from your computer**, and choose the downloaded `SKILL.md`. If it asks for a zip file, use the zipped folder from the Claude steps above.
3. ChatGPT checks the skill before it's ready to use. Once it is, ChatGPT uses it when your message fits.

### Or put it in a project

If your plan has Projects:

1. In the left sidebar, click **Projects**, then **New project**.
2. Open the project's instructions (the gear icon or **Add instructions**).
3. Paste the copied text and save.
4. Start your chats inside that project.

ChatGPT's general **Custom instructions** in Settings are too short for most skills, so use a project instead.

## Any AI tool

This works everywhere, on any plan:

1. Start a new chat.
2. Paste the copied text as your first message and send it.
3. Send your real message next.

You'll need to do this at the start of each new chat.

## Using more than one skill

Tools with a skills feature (Claude, and ChatGPT on business plans) can hold lots of skills at once. They pick the right one for each message.

In Gemini Gems and in projects, each Gem or project holds one set of instructions. Make one for each skill, or paste two skills into the same instructions if you always use them together.

Some skills work as a first step for the others. [Intent mirror](intent-mirror/) checks what you mean, then names the skill that should do the work. If you don't have one that fits, it tells you what kind of skill would help.
