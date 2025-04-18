"""
测试 geo-city-locator 包是否能正常导入和使用
"""
print("测试 geo-city-locator 包导入")
try:
    import geo_city_locator
    print(f"成功导入 geo_city_locator 包！")
    print(f"版本: {geo_city_locator.__version__}")
    
    # 测试功能
    print("\n测试基本功能:")
    city = geo_city_locator.get_nearest_city(40.7128, -74.0060)
    print(f"纽约坐标附近的城市: {city}")
    
except Exception as e:
    print(f"导入错误: {e}")
    import sys
    print(f"Python 路径: {sys.path}") 