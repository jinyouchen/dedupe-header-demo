from app.app import dedupe_header  # 注意导入路径：从app目录的app.py导入


def test_unique_columns():
    """测试无重复列名的场景"""
    assert dedupe_header(["id", "name", "age"]) == ["id", "name", "age"]


def test_duplicate_columns():
    """测试同一列名多次重复的场景"""
    assert dedupe_header(["id", "id", "id"]) == ["id", "id.1", "id.2"]


def test_mixed_columns():
    """测试重复与非重复列名混合的场景（文档示例）"""
    cols = ["id", "name", "id", "name", "name"]
    expected = ["id", "name", "id.1", "name.1", "name.2"]
    assert dedupe_header(cols) == expected


def test_empty_columns():
    """测试空列表输入的场景"""
    assert dedupe_header([]) == []


def test_single_column():
    """测试单个列名的场景"""
    assert dedupe_header(["email"]) == ["email"]


def test_special_characters():
    """测试含特殊字符的列名重复场景"""
    cols = ["id#", "id#", "name@", "id#"]
    expected = ["id#", "id#.1", "name@", "id#.2"]
    assert dedupe_header(cols) == expected


def test_case_sensitive():
    """测试大小写区分（不同大小写视为不同列名）"""
    cols = ["Name", "name", "NAME"]
    expected = ["Name", "name", "NAME"]  # 无后缀，因大小写不同
    assert dedupe_header(cols) == expected