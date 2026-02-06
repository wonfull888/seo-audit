#!/usr/bin/env bun
/**
 * Convert Claude Code session (JSONL) to OpenCode import format (JSON)
 * Usage: bun convert-claude-to-opencode.ts <input.jsonl> <output.json>
 */

import { readFileSync, writeFileSync } from "fs"

// Generate OpenCode-style IDs
function generateId(prefix: string): string {
  const timestamp = Date.now().toString(16)
  const random = Math.random().toString(36).substring(2, 15)
  return `${prefix}_${timestamp}${random}`
}

// Parse command line args
const inputFile = process.argv[2] || `${process.env.HOME}/.claude/projects/-Users-lanren/66b82ec7-b3d7-47db-876e-f0b8b1cf3fd4.jsonl`
const outputFile = process.argv[3] || "/tmp/claude-session-converted.json"

console.log(`Reading: ${inputFile}`)

// Read JSONL file
const content = readFileSync(inputFile, "utf-8")
const lines = content.trim().split("\n").filter(Boolean)

// Parse all messages
const rawMessages: any[] = []
for (const line of lines) {
  try {
    const parsed = JSON.parse(line)
    rawMessages.push(parsed)
  } catch (e) {
    console.error(`Failed to parse line: ${line.substring(0, 100)}...`)
  }
}

console.log(`Parsed ${rawMessages.length} raw entries`)

// Filter to user/assistant messages only
const messages = rawMessages.filter(m => m.type === "user" || m.type === "assistant")
console.log(`Found ${messages.length} user/assistant messages`)

// Get session metadata from first message
const firstMsg = messages[0]
const sessionId = generateId("ses")
const baseTimestamp = new Date(firstMsg?.timestamp || Date.now()).getTime()

// Create session info
const sessionInfo = {
  id: sessionId,
  slug: "imported-claude-session",
  version: "1.1.50",
  projectID: "global",
  directory: firstMsg?.cwd || process.cwd(),
  title: `Imported from Claude Code - ${new Date(baseTimestamp).toISOString()}`,
  time: {
    created: baseTimestamp,
    updated: baseTimestamp,
    archived: 0
  },
  summary: {
    additions: 0,
    deletions: 0,
    files: 0
  }
}

// Convert messages
const convertedMessages: any[] = []
let prevMsgId: string | null = null

for (let i = 0; i < messages.length; i++) {
  const msg = messages[i]
  const msgId = generateId("msg")
  const msgTimestamp = new Date(msg.timestamp).getTime()
  
  // Extract text content
  let textContent = ""
  if (msg.message?.content) {
    if (typeof msg.message.content === "string") {
      textContent = msg.message.content
    } else if (Array.isArray(msg.message.content)) {
      for (const block of msg.message.content) {
        if (block.type === "text") {
          textContent += (textContent ? "\n" : "") + block.text
        } else if (block.type === "tool_use") {
          textContent += (textContent ? "\n" : "") + `[Tool: ${block.name}]`
        } else if (block.type === "tool_result") {
          textContent += (textContent ? "\n" : "") + `[Tool Result]`
        }
      }
    }
  }
  
  // Skip empty messages
  if (!textContent.trim()) {
    continue
  }
  
  // Message info
  const msgInfo: any = {
    id: msgId,
    sessionID: sessionId,
    role: msg.type === "user" ? "user" : "assistant",
    time: {
      created: msgTimestamp,
      completed: msgTimestamp
    },
    agent: "sisyphus",
    path: {
      cwd: msg.cwd || sessionInfo.directory,
      root: "/"
    }
  }
  
  if (prevMsgId) {
    msgInfo.parentID = prevMsgId
  }
  
  if (msg.type === "assistant") {
    msgInfo.modelID = msg.message?.model || "claude-sonnet-4-5"
    msgInfo.providerID = "anthropic"
    msgInfo.mode = "sisyphus"
    msgInfo.cost = 0
    msgInfo.tokens = {
      input: msg.message?.usage?.input_tokens || 0,
      output: msg.message?.usage?.output_tokens || 0,
      reasoning: 0,
      cache: { read: 0, write: 0 }
    }
    msgInfo.finish = msg.message?.stop_reason || "stop"
  }
  
  // Create parts
  const parts: any[] = []
  
  // For user messages, just add text part
  if (msg.type === "user") {
    parts.push({
      id: generateId("prt"),
      sessionID: sessionId,
      messageID: msgId,
      type: "text",
      text: textContent
    })
  } else {
    // For assistant messages, add step-start, text, step-finish
    parts.push({
      id: generateId("prt"),
      sessionID: sessionId,
      messageID: msgId,
      type: "step-start"
    })
    
    parts.push({
      id: generateId("prt"),
      sessionID: sessionId,
      messageID: msgId,
      type: "text",
      text: textContent,
      time: {
        start: msgTimestamp,
        end: msgTimestamp
      }
    })
    
    parts.push({
      id: generateId("prt"),
      sessionID: sessionId,
      messageID: msgId,
      type: "step-finish",
      reason: "stop",
      cost: 0,
      tokens: msgInfo.tokens || { input: 0, output: 0, reasoning: 0, cache: { read: 0, write: 0 } }
    })
  }
  
  convertedMessages.push({
    info: msgInfo,
    parts: parts
  })
  
  prevMsgId = msgId
}

console.log(`Converted ${convertedMessages.length} messages`)

// Build export data
const exportData = {
  info: sessionInfo,
  messages: convertedMessages
}

// Write output
writeFileSync(outputFile, JSON.stringify(exportData, null, 2))
console.log(`Written to: ${outputFile}`)
console.log(`\nTo import: opencode import ${outputFile}`)
