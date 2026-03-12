#!/usr/bin/env node
"use strict";

const { spawn } = require("child_process");
const path = require("path");

const serverPath = path.join(__dirname, "..", "server.py");

// Try python3 first, then python
const pythonCandidates = ["python3", "python"];

function trySpawn(candidates) {
  const cmd = candidates.shift();
  if (!cmd) {
    console.error(
      "Error: Python 3.10+ is required but not found.\n" +
      "Install Python from https://www.python.org/downloads/\n" +
      "Also install the MCP SDK: pip install mcp"
    );
    process.exit(1);
  }

  const child = spawn(cmd, [serverPath], {
    stdio: "inherit",
    env: { ...process.env },
  });

  child.on("error", () => {
    trySpawn(candidates);
  });

  child.on("exit", (code) => {
    process.exit(code ?? 0);
  });
}

trySpawn([...pythonCandidates]);
