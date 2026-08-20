## The Problem

Sometimes we want to move the memory of an agent we're using over to a different agent. This usually comes up in situations like:

- The agent starts acting up, you can't tell where the problem is, and you want to try a reinstall to fix it

- You've run out of tokens on this agent and want to temporarily switch to another one to keep going

- You just don't want to use this agent anymore and want to switch to a different one

I looked around at what's out there, and it turns out there's no single unified way to import and export memory between agents. But it's not entirely hopeless either. Here's what I've found so far.

## Solutions

### Plugged-in memory

Tools like agentmemory and ai-memory work by having the agent not hold any memory of its own at all — the memory is entirely hosted in a third-party store (like Mem0 or Zep). Every time the agent works, it pulls the relevant memory from that external store and injects it into context; when new memory is produced, it writes it back to the store. The agent is just a "read/write client" for that memory, not its "owner." Switch to a different agent, and as long as it connects to the same store, it can read the same memory — no import/export needed, because the memory was never tied to any one agent in the first place.

### An agent's own backup tool

For reinstalling or migrating the same product, use its own backup tool. OpenClaw, for example, has a [Backup](https://docs.openclaw.ai/cli/backup) tool. If you're on OpenClaw, you can back up first, then restore.

```
# 1. Stop the gateway, back up, and verify
openclaw gateway stop
openclaw backup create --output ~/Backups/openclaw --verify

# 2. Uninstall/reinstall
# (For an in-place reinstall you usually don't need `openclaw uninstall` —
#  just overwrite with the new version. For a "delete and reinstall" scenario,
#  let it generate a fresh ~/.openclaw first; it'll get overwritten in the next step anyway.)

# 3. Restore into a fresh staging directory (NOT in place!)
openclaw backup restore <archive.tar.gz> --target ~/openclaw-restored

# 4. Manually move the contents recorded in manifest.json to the actual live path,
#    or just point OPENCLAW_STATE_DIR at this restored directory

# 5. Run a health check + restart
openclaw doctor
openclaw gateway restart
openclaw status
```

### An agent's migrate tool

If you want to switch to a different agent, check the **target** agent's official site for a migrate/import-from page. For example, if you want to move from Hermes Agent to OpenClaw, you can use the tool provided at [Migrate from OpenClaw](https://docs.openclaw.ai/install/migrating-hermes).

```
# 1. Do a dry run first to see what would be imported
hermes claw migrate --dry-run

# 2. Once you're satisfied, run the actual migration
#    (by default this doesn't bring secrets — it only imports user data/config)
hermes claw migrate

# To also bring along API keys, TTS credentials, etc., you must add this flag explicitly
# (--preset full alone does NOT bring secrets automatically)
hermes claw migrate --preset full --migrate-secrets

# 3. After migrating, restart the messaging service so the new config takes effect
systemctl --user restart hermes-gateway

# 4. WhatsApp uses QR-code pairing, so it's outside the scope of migration —
#    you'll need to re-pair it separately
hermes whatsapp

# 5. Once everything checks out, clean up the old directory
#    (rename it to .pre-migration/, don't delete it)
hermes claw cleanup
```

### Agent app export tools

If your agent isn't an always-on autonomous agent like OpenClaw or Hermes Agent, and isn't a coding agent like Claude Code either, but a pure chat product (desktop Claude, mobile ChatGPT), these products usually don't have a concept of "agent state" to migrate — the best you can do is use the account's built-in data export feature to get a **conversation history archive** (for example, ChatGPT's "Settings → Data controls → Export data," which sends the export to your registered email).

That output can't be directly reused by another agent — ChatGPT, for instance, produces a `conversations.json` file, and it's a fairly complex tree structure — but all the information is in there. You can have a different agent write a script to extract the useful parts out of it.

### Asking the agent to export its own context

If there's no official export feature at all, you can just tell the agent directly: "Please put together what you know about me — preferences, habits, background, how I like to work — into a structured Markdown document for me." You can also scope this to a specific project.

This document is something the agent **summarizes on the spot from the current conversation window** — it's not a full backup pulled from some persistent memory store. If the conversation is long and older content has already been compressed away, or the information is scattered across multiple different past conversations, this summary won't be able to reach those parts.

The advantage of this approach is that it's **fast** (no waiting for an official export to process, which for ChatGPT can take several days), but the trade-off is that it's incomplete.
