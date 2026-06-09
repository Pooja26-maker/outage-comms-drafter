"""
Test cases for Outage Comms Drafter (happy path)
Run: pytest tests/test_app.py -v
"""
import pytest
from unittest.mock import patch

# ── Test 1: get_tone_options returns 3 tones ──────────────────────────────────
def test_get_tone_options_returns_three():
    from mcp_tool import get_tone_options
    result = get_tone_options()
    assert "tones" in result
    assert len(result["tones"]) == 3

# ── Test 2: get_tone_options has correct names ────────────────────────────────
def test_get_tone_options_correct_names():
    from mcp_tool import get_tone_options
    result = get_tone_options()
    names = [t["name"] for t in result["tones"]]
    assert "empathetic" in names
    assert "calm" in names
    assert "concise" in names

# ── Test 3: get_severity_levels returns 3 levels ─────────────────────────────
def test_get_severity_levels_returns_three():
    from mcp_tool import get_severity_levels
    result = get_severity_levels()
    assert "levels" in result
    assert len(result["levels"]) == 3

# ── Test 4: get_severity_levels has correct names ────────────────────────────
def test_get_severity_levels_correct_names():
    from mcp_tool import get_severity_levels
    result = get_severity_levels()
    names = [l["name"] for l in result["levels"]]
    assert "low" in names
    assert "medium" in names
    assert "high" in names

# ── Test 5: generate_outage_message returns all keys ─────────────────────────
@patch("agent.ask_ai")
def test_generate_outage_message_returns_all_keys(mock_ask):
    mock_ask.return_value = "We are aware of an issue and working to resolve it."
    from mcp_tool import generate_outage_message
    result = generate_outage_message(
        technical_text="DB primary node failed",
        tone="empathetic"
    )
    assert "initial" in result
    assert "in_progress" in result
    assert "resolved" in result
    assert "detected_severity" in result
    assert "tone_used" in result

# ── Test 6: generate_outage_message tone is correct ──────────────────────────
@patch("agent.ask_ai")
def test_generate_outage_message_correct_tone(mock_ask):
    mock_ask.return_value = "Service is being restored shortly."
    from mcp_tool import generate_outage_message
    result = generate_outage_message(
        technical_text="Payment service timeout",
        tone="calm"
    )
    assert result["tone_used"] == "calm"
