import pytest
from config.config import Config


def run_tests():
    # 设置环境
    Config().set_value("GLOBAL_CONFIG", "test_env", "https://api.apifox.com")

    # 运行pytest
    pytest.main([
        "-v",
        "--self-contained-html",
        "testcases/",
        "--alluredir",
        "reports/result"
    ])


if __name__ == "__main__":
    run_tests()