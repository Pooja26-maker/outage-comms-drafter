"""
Test cases for OutageComms AI (happy path)
Run: pytest tests/test_app.py -v
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pytest
from unittest.mock import patch

# ── Test 1: Agent loop returns all 3 stages ───────────────────────────────────
@patch("agent.ask_ai")
def test_agent_loop_returns_all_stages(mock_ask):
    mock_ask.return_value = "We are aware of an issue and working to resolve it."
    from agent import agent_loop
    results, severity = agent_loop("DB primary node failed", "empathetic")
    assert "initial" in results
    assert "in-progress" in results
    assert "resolved" in results

# ── Test 2: Agent loop auto detects severity ──────────────────────────────────
@patch("agent.ask_ai")
def test_agent_loop_auto_detects_severity(mock_ask):
    mock_ask.return_value = "medium"
    from agent import agent_loop
    results, severity = agent_loop("Payment gateway timeout", "calm", None)
    assert severity is not None
    assert len(severity) > 0

# ── Test 3: Severity detection returns valid value ────────────────────────────
@patch("agent.ask_ai")
def test_detect_severity_returns_valid(mock_ask):
    mock_ask.return_value = "high"
    from agent import detect_severity
    result = detect_severity("Critical DB failure affecting all users")
    assert result in ["low", "medium", "high"]

# ── Test 4: Generate message returns a string ─────────────────────────────────
@patch("agent.ask_ai")
def test_generate_message_returns_string(mock_ask):
    mock_ask.return_value = "We are aware of an issue."
    from agent import generate_message
    result = generate_message("DB failure", "empathetic", "high", "initial")
    assert isinstance(result, str)
    assert len(result) > 0

# ── Test 5: Empathetic tone request works ─────────────────────────────────────
@patch("agent.ask_ai")
def test_agent_loop_empathetic_tone(mock_ask):
    mock_ask.return_value = "We understand this is frustrating and we are working on it."
    from agent import agent_loop
    results, severity = agent_loop("Server down", "empathetic", None)
    assert "initial" in results

# ── Test 6: Calm tone request works ───────────────────────────────────────────
@patch("agent.ask_ai")
def test_agent_loop_calm_tone(mock_ask):
    mock_ask.return_value = "Service disruption detected. Team is investigating."
    from agent import agent_loop
    results, severity = agent_loop("API timeout errors", "calm", None)
    assert "resolved" in results
