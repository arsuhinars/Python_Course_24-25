import pytest

from solution.task_5 import process_logs


@pytest.mark.parametrize(
    (
        "input_logs_path,"
        "expected_blocks,"
        "expected_players,"
        "expected_players_online,"
        "expected_players_blocks,"
        "expected_players_achievements"
    ),
    [
        (
            "tests/minicraft_logs.txt",
            41,
            ["Steve", "Alex", "Herobrine"],
            {"Steve": 1799, "Alex": 1365, "Herobrine": 1559},
            {"Steve": 15, "Alex": 12, "Herobrine": 14},
            {
                "Steve": {
                    "HotTopic",
                    "StoneAge",
                    "TheEnd",
                    "Enchanter",
                    "Benchmarking",
                    "DeliciousFish",
                },
                "Alex": {"GettingWood", "TakingInventory", "TimeToFarm"},
                "Herobrine": {
                    "Overkill",
                    "AcquireHardware",
                    "WeNeedToGoDeeper",
                    "TimeToMine",
                },
            },
        )
    ],
)
def test_process_logs(
    input_logs_path,
    expected_blocks,
    expected_players,
    expected_players_online,
    expected_players_blocks,
    expected_players_achievements,
):
    with open(input_logs_path) as f:
        logs = f.readlines()

    blocks_count, players, players_online, players_blocks, player_achievements = (
        process_logs(logs)
    )

    assert blocks_count == expected_blocks
    assert set(players) == set(expected_players)

    players_online_d = {nick: players_online[i] for i, nick in enumerate(players)}
    assert players_online_d == expected_players_online

    players_blocks_d = {nick: players_blocks[i] for i, nick in enumerate(players)}
    assert players_blocks_d == expected_players_blocks

    players_achievements_d = {
        nick: set(player_achievements[i]) for i, nick in enumerate(players)
    }
    assert players_achievements_d == expected_players_achievements
